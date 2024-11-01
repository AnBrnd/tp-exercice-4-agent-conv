import discord
from discord import Intents
from discord.ext import commands
from rasa.core.channels.channel import UserMessage, OutputChannel, InputChannel
from sanic import Blueprint
import asyncio
import logging

class DiscordOutput(OutputChannel):
    def __init__(self, client: discord.Client):
        self.client = client

    async def send_text_message(self, recipient_id: str, text: str, **kwargs):
        try:
            user = await self.client.fetch_user(recipient_id)
            await user.send(text)
        except discord.HTTPException as e:
            logging.error(f"Erreur lors de l'envoi du message à {recipient_id}: {e}")

class DiscordInput(InputChannel):
    def __init__(self, token: str):
        self.token = token
        self.on_new_message = None
        self.discord_client = None

    @classmethod
    def name(cls):
        return "discord"

    @classmethod
    def from_credentials(cls, credentials):
        return cls(credentials.get("token"))

    async def _handle_message(self, message, output_channel, sender_id):
        if self.on_new_message:
            try:
                user_message = UserMessage(
                    text=message.content,
                    output_channel=output_channel,
                    sender_id=str(sender_id)  # Convertir en chaîne
                )
                await self.on_new_message(user_message)
            except Exception as e:
                logging.error(f"Erreur lors du traitement du message : {e}")

    def blueprint(self, on_new_message):
        self.on_new_message = on_new_message
        intents = Intents.default()
        intents.message_content = True

        # Utilisation de commands.Bot pour plus de flexibilité
        self.discord_client = commands.Bot(command_prefix='!', intents=intents)

        @self.discord_client.event
        async def on_ready():
            print(f"Logged in as {self.discord_client.user}")
            print(f"ID: {self.discord_client.user.id}")

        @discord_client.event
        async def on_ready():
            print(f"Bot {discord_client.user} est en ligne !")


        @self.discord_client.event
        async def on_message(message):
            # Ignorer les messages du bot lui-même et les messages de bot
            if message.author.bot:
                return

            # Créer un canal de sortie
            output_channel = DiscordOutput(self.discord_client)

            # Gérer le message
            await self._handle_message(message, output_channel, message.author.id)

            # Permettre le traitement des commandes si nécessaire
            await self.discord_client.process_commands(message)

        # Ajout d'un gestionnaire d'erreurs global
        @self.discord_client.event
        async def on_command_error(ctx, error):
            logging.error(f"Erreur de commande : {error}")
            await ctx.send("Une erreur est survenue lors du traitement de votre commande.")

        # Démarrage du client de manière asynchrone
        async def start_discord_client():
            await self.discord_client.start(self.token)

        return Blueprint("discord", __name__)

    def run(self):
        """
        Méthode pour démarrer le client Discord
        """
        try:
            asyncio.run(self.discord_client.start(self.token))
        except Exception as e:
            logging.error(f"Erreur lors du démarrage du client Discord : {e}")

