# TP Exercice 4 - Agent Conversationnel

**Autrice :** Anaïs BERNARD

Ce projet est réalisé dans le cadre d'un TP de cours et vise à développer un agent conversationnel de réservation de restaurant en utilisant le framework Rasa. L'agent est conçu pour gérer les interactions de réservation, l'annulation, et fournir des informations utiles aux utilisateurs. Nous avons également exploré l'intégration du bot avec Discord pour permettre une interaction en temps réel dans un contexte de messagerie.

## Objectifs du TP

- Apprendre à configurer un agent conversationnel avec Rasa.
- Structurer les intentions, entités, réponses, et histoires pour des conversations cohérentes.
- Explorer les interactions basées sur des règles et des histoires pour le dialogue.
- Intégrer le bot avec Discord en utilisant l'API de Discord.
- Comprendre les défis courants et les limitations dans le développement d'agents conversationnels.

## Table des matières

- [Schéma initial](#schéma-initial)
- [Installation](#installation)
- [Configuration du Bot Rasa](#configuration-du-bot-rasa)
- [Intégration avec Discord](#intégration-avec-discord)
- [Exécution du Bot](#exécution-du-bot)
- [Difficultés Rencontrées](#difficultés-rencontrées)
- [Conclusion](#conclusion)

## Schéma initial

![Schéma intéractions](images/TP_Agent_Conv.jpg)

## Installation

### Prérequis

Avant de commencer, assurez-vous d'avoir :

- **Python 3.10** (compatible avec les bibliothèques utilisées)
- **pip** pour gérer les packages Python
- Un environnement virtuel Python (recommandé pour isoler les dépendances)
- **Un token de bot Discord** (à créer sur le [Discord Developer Portal](https://discord.com/developers/applications))

### Étapes d'installation

1. **Cloner le dépôt du projet**

   ```bash
   git clone https://github.com/AnBrnd/Rendu-tp-exercice-4-agent-conv.git
   cd tp-exercice-4-agent-conv
   ```

2. **Créer et activer l'environnement virtuel**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
   
3. **Installer les dépendances**

   ```bash
    pip install -r requirements.txt
    ```
S'assurer que les bibliothèques suivantes sont installées :
- rasa
- discord.py

## Configuration du bot Rasa
### Fichiers de configuration

Nous avons configuré plusieurs fichiers essentiels dans Rasa pour permettre au bot 
de répondre correctement aux intentions de réservation, d'annulation, et de demande 
d'informations.

1. *domain.yml* : Ce fichier définit les intentions, les entités, les réponses, et les 
slots utilisés par le bot. 
Exemple de structure :
   ```bash
   intents:
   - greet
   - demander_reservation
   - fournir_date
   - fournir_nombre_personnes
     ...

   responses:
   utter_greet:
   - text: "Bonjour ! Que puis-je faire pour vous ?"
    ```

2. *nlu.yml* : Nous avons ajouté des exemples d'expressions pour chaque intention (salutation,
demande de réservation, etc.) afin de permettre à Rasa de mieux comprendre les intentions des
utilisateurs.

3. *stories.yml* : Ce fichier contient les histoires, qui sont des exemples de conversations 
typiques. Elles servent à entraîner le modèle pour gérer les dialogues de manière fluide et 
cohérente.

4. *rules.yml* : Ce fichier contient des règles spécifiques pour des interactions prédéfinies. 
Par exemple, répondre avec un remerciement lorsqu'un utilisateur dit "merci".

5. *credentials.yml* : Ce fichier configure les canaux de communication, y compris Discord.

### Entraînement du modèle
Avant de tester ou d'exécuter le bot, nous devons entraîner le modèle. Pour cela, nous utilisons la commande :
```bash
rasa train
```
Cette commande entraîne le modèle en utilisant les données fournies dans les fichiers de configuration.

## Intégration avec Discord
Pour ce TP, nous avons exploré l'intégration de notre bot Rasa avec Discord pour rendre l'interaction 
plus accessible. Cela implique la création d'un fichier discord_channel.py pour configurer le client Discord.

### Fichier *discord_channel.py*
Ce fichier contient les fonctions nécessaires pour gérer les interactions avec Discord. Il utilise la
bibliothèque discord.py pour se connecter au serveur Discord et envoyer/recevoir des messages.

### Exécution et tests du bot
1. Pour démarrer le serveur d'actions :
```bash
rasa run actions
```
2. Pour démarrer le serveur Rasa :
```bash
rasa run -m models --enable-api --cors "*" --debug
```
3. Pour tester le bot dans le terminal :
```bash
rasa shell
```
4. Pour tester le bot sur Discord :
```bash
python actions/discord_channel.py
```

## Difficultés Rencontrées
Au cours de ce TP, j'ai rencontré plusieurs difficultés, notamment :
- **Intégration Discord** : Bien que la bibliothèque discord.py soit installée, 
des erreurs d'importation persistent dans l'éditeur de code. Cela pourrait être lié 
aux paramètres de l'environnement virtuel ou aux versions de Python.
- **Configuration des règles et des histoires** : Des conflits peuvent surgir si les règles 
et les histoires ne sont pas parfaitement alignées, entraînant des comportements inattendus du bot.

## Conclusion
Ce TP m'a permis de mieux comprendre le processus de développement d'un agent conversationnel, 
en particulier avec Rasa. J'ai appris à structurer les données, à entraîner le modèle, et à gérer
les interactions avec les utilisateurs. L'intégration avec Discord a également été une expérience
intéressante pour explorer de nouveaux canaux de communication, même si je n'ai pas réussi à le faire fonctionner.