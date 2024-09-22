---
[![Version française](https://img.shields.io/badge/Lire%20en-Fran%C3%A7ais-blue?style=for-the-badge&logo=appveyor)](https://github.com/Zack-911/SelfBotX/blob/main/README-fr.md)


# 🌌 SelfBotX
### A powerful Discord Selfbot crafted in Python using [discord.py-self](https://github.com/dolfies/discord.py-self)!

<div align="center">
  <img src="https://github.com/user-attachments/assets/72bbd0f7-5de7-4479-b57d-5c696c9b36d3" alt="icon" width="50%" height="50%">

  [![GitHub release (latest by date)](https://img.shields.io/github/v/release/Sitois/Nuclear-V2.svg?style=flat)](https://github.com/Zack-911/SelfBotX/releases)
  [![GitHub downloads](https://img.shields.io/github/downloads/Sitois/Nuclear-V2/total.svg?style=flat)](https://github.com/Zack-911/SelfBotX/releases)
  [![GitHub stars](https://img.shields.io/github/stars/Sitois/Nuclear-V2.svg?style=flat)](https://github.com/Zack-911/SelfBotX/stargazers)
  [![GitHub watchers](https://img.shields.io/github/watchers/Sitois/Nuclear.svg?style=flat)](https://github.com/Zack-911/SelfBotX/watchers)
  [![GitHub issues](https://img.shields.io/github/issues/Sitois/Nuclear-V2.svg?style=flat)](https://github.com/Zack-911/SelfBotX/issues)
</div>


## ⛔ Disclaimer
**Please note that Discord SelfBots are against Discord's Terms of Service and may result in account bans. Use this software at your own risk for educational purposes only.**

## 📖 Table of Contents
1. [💾 Installation](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#-installation)
2. [🔧 Configuration](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#-config)
3. [🌟 Features](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#-features)
4. [📜 How to Retrieve a User Token](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#-how-to-get-a-user-token)
5. [👀 Preview](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#-preview)
6. [☣️ Issues](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#%EF%B8%8F-issues)
7. [🛠️ Development Version](https://github.com/Zack-911/SelfBotX#%EF%B8%8F-developement-version)
8. [❓ How to Contribute](https://github.com/Zack-911/SelfBotX#-how-to-contribute)
9. [⭐ Contributors](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#-contributors)
10. [🫂 Support](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#support)

## 💾 Installation
1. Download the latest version from the [Releases](https://github.com/Zack-911/SelfBotX/releases) section on GitHub.
2. Ensure you have [Python](https://www.python.org/downloads/) installed.
3. Open your terminal and navigate to the SelfBotX folder using `cd`.
4. Install dependencies with: `pip install -r requirements.txt`
5. Run the program using: `python main.py`
6. Get started by typing `&help`!

## 🔧 Configuration
Edit `config_selfbot.py` using any text editor and input your [user token](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#-how-to-get-a-user-token).

## 🌟 Features
* Custom RPC templates
* Build your own RPC
* Voice commands
* Raid commands
* Massive DM (DM All)
* Nitro Sniper
* Spam and Flood commands
* Snipe command
* And more! Check the `Help` command for details.

## 📜 How to Retrieve a User Token
1. Navigate to [Discord Web](https://discord.com/app).
2. Press ``CTRL + SHIFT + I`` and go to the `Console` tab.
3. Paste the following code:
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
   console.log(`%cYou now have your token in the clipboard!`, 'font-size: 16px');
   ```
4. If pasting fails, type `allow pasting` and try again.
5. Paste your token into `config_selfbot.py`.

## 👀 Preview
<div align="center">
  <img src="https://github.com/user-attachments/assets/0ebb7a06-948f-4e7d-aa3c-1cfa78ce525a" alt="preview" width="">
</div>
<br>

## ☣️ Issues
Currently, there are no known issues. If you encounter any, please visit our [Support](https://github.com/Zack-911/SelfBotX?tab=readme-ov-file#support)!

## 🛠️ Development Version
1. Open your terminal and navigate to the desired folder using `cd`.
2. Clone the repository with: `git clone https://github.com/Zack-911/SelfBotX`
   **or**
   Click the green "Code" button above the README.

## ❓ How to Contribute
🖤 Show your support by starring the project!  
🧷 Help translate the selfbot using `langs.py`!  
You can also assist with items on my "need help" list:
  - Captcha: Check comments in `main.py`.

## ⭐ Contributors
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
- Join our Discord server: [SelfBotX](https://discord.gg/gFrFx8T6qX)

<br>

---
Thank you for using SelfBotX!!

--- 