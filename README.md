# TP Exercice 4 - Agent Conversationnel

Ce projet est réalisé dans le cadre d'un TP de cours et vise à développer un agent conversationnel de réservation de restaurant en utilisant le framework Rasa. L'agent est conçu pour gérer les interactions de réservation, l'annulation, et fournir des informations utiles aux utilisateurs. Nous avons également exploré l'intégration du bot avec Discord pour permettre une interaction en temps réel dans un contexte de messagerie.

## Objectifs du TP

- Apprendre à configurer un agent conversationnel avec Rasa.
- Structurer les intentions, entités, réponses, et histoires pour des conversations cohérentes.
- Explorer les interactions basées sur des règles et des histoires pour le dialogue.
- Intégrer le bot avec Discord en utilisant l'API de Discord.
- Comprendre les défis courants et les limitations dans le développement d'agents conversationnels.

## Table des matières

- [Installation](#installation)
- [Configuration du Bot Rasa](#configuration-du-bot-rasa)
- [Intégration avec Discord](#intégration-avec-discord)
- [Exécution du Bot](#exécution-du-bot)
- [Difficultés Rencontrées](#difficultés-rencontrées)
- [Conclusion](#conclusion)

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
   git clone <url-du-repo>
   cd tp-exercice-4-agent-conv
