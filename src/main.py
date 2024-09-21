import discord
from termcolor import colored
import pyfiglet
from colorama import init, Fore, Style
import os

# Initialize Colorama
init()

# Create ASCII art using pyfiglet
ascii_art = pyfiglet.figlet_format("Hello, World!")

# Print ASCII art with color
print(Fore.RED + ascii_art + Style.RESET_ALL)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

client = MyClient()
client.run('')