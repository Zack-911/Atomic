import discord
from termcolor import colored
import pyfiglet
from colorama import init, Fore, Style
import json

# Load the configuration file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Access the settings
Token = config['Token']

print("Token Loaded")

# Initialize Colorama
init()

# Create ASCII art using pyfiglet
ascii_art = pyfiglet.figlet_format("SELFBOTX")

# Print ASCII art with color
print(Fore.RED + ascii_art + Style.RESET_ALL)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

client = MyClient()
client.run(Token)  # Use the actual token variable here
