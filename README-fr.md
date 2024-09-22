---

[![Version française](https://img.shields.io/badge/Lire%20en-Fran%C3%A7ais-blue?style=for-the-badge&logo=appveyor)](https://github.com/Zack-911/SelfBotX/blob/main/README-fr.md)

# 🌌 SelfBotX
### Un puissant Selfbot Discord conçu en Python en utilisant [discord.py-self](https://github.com/dolfies/discord.py-self) !

<div align="center">
  <img src="https://github.com/user-attachments/assets/72bbd0f7-5de7-4479-b57d-5c696c9b36d3" alt="icon" width="50%" height="50%">

  [![GitHub release (latest by date)](https://img.shields.io/github/v/release/Sitois/Nuclear-V2.svg?style=flat)](https://github.com/Zack-911/SelfBotX/releases)
  [![GitHub downloads](https://img.shields.io/github/downloads/Sitois/Nuclear-V2/total.svg?style=flat)](https://github.com/Zack-911/SelfBotX/releases)
  [![GitHub stars](https://img.shields.io/github/stars/Sitois/Nuclear-V2.svg?style=flat)](https://github.com/Zack-911/SelfBotX/stargazers)
  [![GitHub watchers](https://img.shields.io/github/watchers/Sitois/Nuclear.svg?style=flat)](https://github.com/Zack-911/SelfBotX/watchers)
  [![GitHub issues](https://img.shields.io/github/issues/Sitois/Nuclear-V2.svg?style=flat)](https://github.com/Zack-911/SelfBotX/issues)
</div>

## ⛔ Avertissement
**Veuillez noter que les SelfBots Discord sont contraires aux Conditions d'Utilisation de Discord et peuvent entraîner des bannissements de compte. Utilisez ce logiciel à vos propres risques à des fins éducatives uniquement.**

## 📖 Table des matières
1. [💾 Installation](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#-installation)
2. [🔧 Configuration](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#-config)
3. [🌟 Fonctionnalités](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#-features)
4. [📜 Comment récupérer un jeton utilisateur](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#-how-to-get-a-user-token)
5. [👀 Aperçu](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#-preview)
6. [☣️ Problèmes](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#%EF%B8%8F-issues)
7. [🛠️ Version de Développement](https://github.com/Zack-911/SelfBotX#%EF%B8%8F-developement-version)
8. [❓ Comment Contribuer](https://github.com/Zack-911/SelfBotX#-how-to-contribute)
9. [⭐ Contributeurs](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#-contributors)
10. [🫂 Support](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#support)

## 💾 Installation
1. Téléchargez la dernière version dans la section [Releases](https://github.com/Zack-911/SelfBotX/releases) sur GitHub.
2. Assurez-vous d’avoir [Python](https://www.python.org/downloads/) installé.
3. Ouvrez votre terminal et accédez au dossier SelfBotX avec la commande `cd`.
4. Installez les dépendances avec : `pip install -r requirements.txt`
5. Exécutez le programme avec : `python main.py`
6. Commencez en tapant `&help` !

## 🔧 Configuration
Modifiez `config_selfbot.py` avec un éditeur de texte et entrez votre [jeton utilisateur](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#-how-to-get-a-user-token).

## 🌟 Fonctionnalités
* Modèles RPC personnalisés
* Créez votre propre RPC
* Commandes vocales
* Commandes de raid
* DM massif (DM tous)
* Nitro Sniper
* Commandes de spam et de flood
* Commande Snipe
* Et bien plus ! Consultez la commande `Help` pour plus de détails.

## 📜 Comment récupérer un jeton utilisateur
1. Accédez à [Discord Web](https://discord.com/app).
2. Appuyez sur `CTRL + SHIFT + I` et allez dans l'onglet `Console`.
3. Collez le code suivant :
   ```js
   window.webpackChunkdiscord_app.push([
     [Math.random()],
     {},
     req => {
       if (!req.c) return;
       for (const m of Object.keys(req.c)
         .map(x => req.c[x].exports)
         .filter(x => x)) {
         if (m.default && m.default.getToken !== undefined) {
           return copy(m.default.getToken());
         }
         if (m.getToken !== undefined) {
           return copy(m.getToken());
         }
       }
     },
   ]);
   console.log('%cWorked!', 'font-size: 50px');
   console.log(`%cVous avez maintenant votre jeton dans le presse-papiers !`, 'font-size: 16px');
   ```
4. Si le collage échoue, tapez `allow pasting` et réessayez.
5. Collez votre jeton dans `config_selfbot.py`.

## 👀 Aperçu
<div align="center">
  <img src="https://github.com/user-attachments/assets/0ebb7a06-948f-4e7d-aa3c-1cfa78ce525a" alt="aperçu" width="">
</div>
<br>

## ☣️ Problèmes
Actuellement, il n'y a aucun problème connu. Si vous en rencontrez, veuillez consulter notre [Support](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#support) !

## 🛠️ Version de Développement
1. Ouvrez votre terminal et accédez au dossier souhaité avec `cd`.
2. Clonez le dépôt avec : `git clone https://github.com/Zack-911/SelfBotX`
   **ou**
   Cliquez sur le bouton vert "Code" en haut du README.

## ❓ Comment Contribuer
🖤 Montrez votre soutien en ajoutant une étoile au projet !  
🧷 Aidez à traduire le selfbot en utilisant `langs.py` !  
Vous pouvez également aider sur ma liste d'éléments "besoin d'aide" :
  - Captcha : Consultez les commentaires dans `main.py`.

## ⭐ Contributeurs
<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/MRHACKER7788">
        <img src="https://avatars.githubusercontent.com/u/134154007?s=64&v=4" alt="MRHACKER7788" width="80px" height="80px" style="border-radius: 50%;">
        <br>
        MRHACKER7788
      </a>
    </td>
  </tr>
</table>

# Support
- Rejoignez notre serveur Discord : [SelfBotX](https://discord.gg/gFrFx8T6qX)

<br>

---
Merci d'utiliser SelfBotX !!
----