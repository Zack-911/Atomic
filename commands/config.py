import discord
from discord.ext import commands
import asyncio
from colorama import Fore, Style, Back


import config_selfbot
import langs

class ConfigCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.nitro_sniper = config_selfbot.nitro_sniper

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if self.nitro_sniper and not ctx.author.id == self.bot.user.id:
            if "discord.gift/" in ctx.content:
                try:
                    gift_code = ctx.content.split("discord.gift/")[1].split()[0]

                    # Prevent from claiming a promotionnal link
                    if "-" in gift_code: 
                        return

                    if isinstance(ctx.channel, discord.DMChannel) or isinstance(ctx.channel, discord.GroupChannel):
                        print(f"{Fore.LIGHTYELLOW_EX}[~] {Fore.YELLOW}Nitro Sniper: discord.gift/{gift_code}", Style.RESET_ALL)
                    else:
                        print(f"{Fore.LIGHTYELLOW_EX}[~] {Fore.YELLOW}Nitro Sniper: discord.gift/{gift_code} | Channel: {ctx.channel.name}({ctx.channel.id}) | Guild: {ctx.guild.name}({ctx.guild.id})", Style.RESET_ALL)
                    gift = await self.bot.fetch_gift(gift_code)
                    await gift.redeem(channel=ctx.channel)
                    print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.GREEN}discord.gift/{gift_code} {langs.nitro_sniper_valid[config_selfbot.lang]}", Style.RESET_ALL)
                except discord.NotFound:
                    print(f"{Fore.LIGHTRED_EX}[!] {Fore.RED}discord.gift/{gift_code} {langs.nitro_sniper_invalid_code[config_selfbot.lang]}", Style.RESET_ALL)
                except discord.HTTPException:
                    print(f"{Fore.LIGHTRED_EX}[!] {Fore.RED}discord.gift/{gift_code} {langs.nitro_sniper_claimed[config_selfbot.lang]}", Style.RESET_ALL)

    @commands.command()
    async def nitrosniper(self, ctx):
        if not self.nitro_sniper:
            self.nitro_sniper = True
            await ctx.message.edit("🟢 Nitro Sniper **On**.")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        else:
            self.nitro_sniper = False
            await ctx.message.edit("🔴 Nitro Sniper **Off**.")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()

    @commands.command()
    async def lang(self, ctx):
        if config_selfbot.lang == "fr":
            config_selfbot.lang = "en"
            await ctx.message.edit("🟢 Language set to **English**.")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()
        else:
            config_selfbot.lang = "fr"
            await ctx.message.edit("🟢 Langue changé en **Français**.")
            await asyncio.sleep(config_selfbot.deltime)
            await ctx.message.delete()