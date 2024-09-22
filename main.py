import subprocess
try:
    import sys, os, platform
    import ctypes
    import datetime, time
    import threading
    import random
    import config_selfbot
    import langs
    import rpc
    from commands import *
    from colorama import Fore, Style, Back
    import requests
    #import twocaptcha
    import discord
    from discord.ext import commands
except ImportError:
    import sys, os
    if os.name == 'nt':
        subprocess.check_call([sys.executable, "-m", "pip", "install", '-r' , 'requirements.txt'])
    else:
        subprocess.check_call([sys.executable, "-m", "pip", "install", '-r' , 'requirements.txt'])
    import platform
    import ctypes
    import datetime, time
    import threading
    import random
    import config_selfbot
    import langs
    import rpc
    from commands import *
    from colorama import Fore, Style, Back
    import requests
    #import twocaptcha
    import discord
    from discord.ext import commands

os.system('cls' if os.name == 'nt' else 'clear')

Atomic_version = "v1.00"

print(fr"""{Fore.LIGHTCYAN_EX}
 █████╗ ████████╗ ██████╗ ███╗   ███╗██╗ ██████╗
██╔══██╗╚══██╔══╝██╔═══██╗████╗ ████║██║██╔════╝
███████║   ██║   ██║   ██║██╔████╔██║██║██║     
██╔══██║   ██║   ██║   ██║██║╚██╔╝██║██║██║     
██║  ██║   ██║   ╚██████╔╝██║ ╚═╝ ██║██║╚██████╗
╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝

                                                                   {Atomic_version}{Style.RESET_ALL}""")

def set_terminal_title(title):
    system = platform.system()
    if system == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    elif system == 'Darwin':
        subprocess.run(['osascript', '-e', f'tell application "Terminal" to set custom title of front window to "{title}"'])
    elif system == 'Linux':
        sys.stdout.write(f"\x1b]2;{title}\x07")
        sys.stdout.flush()

try:
    set_terminal_title("| Atomic |")
except Exception as e:
    print(f"Error while trying to change the terminal name: {e}")

if config_selfbot.token == "":
    config_selfbot.token = input("Token: ")

if config_selfbot.lang == "":
    print("""Language Choice / Choix de la langue:
fr: Français
en: English""")
    config_selfbot.lang = input("fr / en: ")

if config_selfbot.prefix == "":
    config_selfbot.prefix = input("Prefix: ")

if config_selfbot.selfbot_name == "":
    config_selfbot.selfbot_name = input("Selfbot name: ")

def check_latest_version(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
    response = requests.get(url)
    
    if response.status_code == 200:
        release_info = response.json()
        latest_version = release_info['tag_name']
        return latest_version
    else:
        return None

def call_check_repo():
    global Atomic_version
    repo_owner = "Atomic-911"
    repo_name = "Atomic"
    while True:
        latest_version = check_latest_version(repo_owner, repo_name)
        if latest_version:
            if not latest_version == Atomic_version:
                print(f"{Fore.BLUE}[INFO] {langs.error_check_version_one[config_selfbot.lang]} ({latest_version}) {langs.error_check_version_two[config_selfbot.lang]} https://github.com/Atomic-911/Atomic/releases/tag/{latest_version}")
                print(f"{langs.error_check_version_three[config_selfbot.lang]} {Atomic_version}{Style.RESET_ALL}")
            time.sleep(3600)

def run_in_background():
    thread = threading.Thread(target=call_check_repo, daemon=True)
    thread.start()

try:
    run_in_background()
except Exception as e:
    print(f"Error while trying to check the last Atomic version: {e}")

print(f"{Fore.LIGHTYELLOW_EX}[#] {Fore.YELLOW}{langs.start_text[config_selfbot.lang]}{Style.RESET_ALL}")

####################
#  start           #
#   setup     !!!  #
####################
assets = config_selfbot.assets
today_date = datetime.datetime.today()

"""
API_KEY = 'YOUR_API_KEY'

solver = twocaptcha.TwoCaptcha(API_KEY)

async def handle_captcha(exc: discord.CaptchaRequired, bot: commands.Bot) -> str:
    result = solver.solve_captcha(site_key=exc.sitekey, page_url="https://discord.com/")
    return result['code']
"""

bot = commands.Bot(command_prefix=config_selfbot.prefix, self_bot=True, help_command=None) #, captcha_handler=handle_captcha)

start_time = time.time()

@bot.event
async def on_ready():
    global today_date
    global start_time
    print(f"{Fore.YELLOW}------------------{Style.RESET_ALL}")

    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal

    print(fr"""{Fore.LIGHTCYAN_EX}
 
     █████╗ ████████╗ ██████╗ ███╗   ███╗██╗ ██████╗
    ██╔══██╗╚══██╔══╝██╔═══██╗████╗ ████║██║██╔════╝
    ███████║   ██║   ██║   ██║██╔████╔██║██║██║     
    ██╔══██║   ██║   ██║   ██║██║╚██╔╝██║██║██║     
    ██║  ██║   ██║   ╚██████╔╝██║ ╚═╝ ██║██║╚██████╗
    ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
                                                

                                                                {Atomic_version}{Style.RESET_ALL}""")
    

    # Cogs !!
    try:
        await bot.add_cog(HelpCommands(bot))
        print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}HelpCommands: {langs.cog_success[config_selfbot.lang]}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] {Fore.LIGHTRED_EX}HelpCommands: {langs.cog_fail[config_selfbot.lang]} {e}{Style.RESET_ALL}")
    try:
        await bot.add_cog(FunCommands(bot))
        print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}FunCommands: {langs.cog_success[config_selfbot.lang]}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] {Fore.LIGHTRED_EX}FunCommands: {langs.cog_fail[config_selfbot.lang]} {e}{Style.RESET_ALL}")
    try:
        await bot.add_cog(UtilsCommands(bot))
        print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}UtilsCommands: {langs.cog_success[config_selfbot.lang]}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] {Fore.LIGHTRED_EX}UtilsCommands: {langs.cog_fail[config_selfbot.lang]} {e}{Style.RESET_ALL}")
    try:
        await bot.add_cog(VoiceCommands(bot))
        print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}VoiceCommands: {langs.cog_success[config_selfbot.lang]}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] {Fore.LIGHTRED_EX}VoiceCommands: {langs.cog_fail[config_selfbot.lang]} {e}{Style.RESET_ALL}")
    try:
        await bot.add_cog(ConfigCommands(bot))
        print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}ConfigCommands: {langs.cog_success[config_selfbot.lang]}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] {Fore.LIGHTRED_EX}ConfigCommands: {langs.cog_fail[config_selfbot.lang]} {e}{Style.RESET_ALL}")
    try:
        await bot.add_cog(RaidCommands(bot))
        print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}RaidCommands: {langs.cog_success[config_selfbot.lang]}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] {Fore.LIGHTRED_EX}RaidCommands: {langs.cog_fail[config_selfbot.lang]} {e}{Style.RESET_ALL}")
    try:
        await bot.add_cog(ToolsCommands(bot))
        print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}ToolsCommands: {langs.cog_success[config_selfbot.lang]}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] {Fore.LIGHTRED_EX}ToolsCommands: {langs.cog_fail[config_selfbot.lang]} {e}{Style.RESET_ALL}")
    try:
        await bot.add_cog(TemplatesCommands(bot))
        print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}TemplatesCommands: {langs.cog_success[config_selfbot.lang]}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] {Fore.LIGHTRED_EX}TemplatesCommands: {langs.cog_fail[config_selfbot.lang]} {e}{Style.RESET_ALL}")
    try:
        await bot.add_cog(RichPresenceCommands(bot))
        print(f"{Fore.GREEN}[+] {Fore.LIGHTGREEN_EX}RichPresenceCommands: {langs.cog_success[config_selfbot.lang]}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[-] {Fore.LIGHTRED_EX}RichPresenceCommands: {langs.cog_fail[config_selfbot.lang]} {e}{Style.RESET_ALL}")

    print(f"{Fore.RED}[!] {Fore.LIGHTRED_EX}{langs.ready_text[config_selfbot.lang]} @{bot.user.name} ({bot.user.id}), {langs.ready_text_two[config_selfbot.lang]} {round(time.time()) - round(start_time)} {langs.ready_text_three[config_selfbot.lang]}", Style.RESET_ALL)
    print(f"{Fore.MAGENTA}------------------{Style.RESET_ALL}")

    # Your code for setting assets and activity...
    assets = {
        "large_image": config_selfbot.assets["large_image"] if rpc.read_variable_json("large_image") == "VOID" else rpc.read_variable_json("large_image"),
        "large_text": config_selfbot.assets["large_text"] if rpc.read_variable_json("large_text") == "VOID" else rpc.read_variable_json("large_text"),
        "small_image": config_selfbot.assets["small_image"] if rpc.read_variable_json("small_image") == "VOID" else rpc.read_variable_json("small_image"),
        "small_text": config_selfbot.assets["small_text"] if rpc.read_variable_json("small_text") == "VOID" else rpc.read_variable_json("small_text")
    }
    activity = discord.Activity(type=discord.ActivityType.playing,
                                 name=config_selfbot.activity_name if rpc.read_variable_json("activity_name") == "VOID" else rpc.read_variable_json("activity_name"),
                                 details=config_selfbot.activity_details if rpc.read_variable_json("activity_details") == "VOID" else rpc.read_variable_json("activity_details"),
                                 state=config_selfbot.activity_state if rpc.read_variable_json("activity_state") == "VOID" else rpc.read_variable_json("activity_state"),
                                 timestamps={"start": time.time()},
                                 assets=assets,
                                 application_id=config_selfbot.application_id,
                                 buttons=[config_selfbot.activity_button_one if rpc.read_variable_json("activity_button_one") == "VOID" else rpc.read_variable_json("activity_button_one"),
                                          config_selfbot.activity_button_two if rpc.read_variable_json("activity_button_two") == "VOID" else rpc.read_variable_json("activity_button_two")])
    
    await bot.change_presence(status=discord.Status.idle,
                              activity=activity,
                              afk=True,
                              idle_since=datetime.datetime(today_date.year, today_date.month, today_date.day))

def restart_selfbot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

@bot.command()
async def restart(ctx):
    await ctx.message.edit(langs.restart_command[config_selfbot.lang])
    time.sleep(2)
    await ctx.message.delete()
    restart_selfbot()

@bot.command()
async def stop(ctx):
    await ctx.message.edit(langs.stop_command[config_selfbot.lang])
    time.sleep(2)
    await ctx.message.delete()
    await bot.close()
    exit()

#############
#############

####################
# start the        #
#      selfbot !!  #
####################

def fix_aiohttp():
    """
    This error is from discord.py==1.7.3(it's the last version of discord.py that works with user account) that use an old version of aiohttp.
    This should fix this problem and restart the selfbot :).
    """
    if os.name == 'nt':
        subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "aiohttp"])
        time.sleep(3)
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "aiohttp"])
    else:
        subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "aiohttp"])
        time.sleep(3)
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "aiohttp"])

    print(f"{Fore.LIGHTGREEN_EX}[INFO] {Fore.GREEN}{langs.aihottp_success[config_selfbot.lang]}{Style.RESET_ALL}")
    time.sleep(3)

    restart_selfbot()

try:
    bot.run(config_selfbot.token)
except discord.LoginFailure:
    print(f"{Fore.LIGHTRED_EX}[CRITICAL] {Fore.RED}{langs.token_error[config_selfbot.lang]}{Style.RESET_ALL}")
except Exception as e:
    if "400, message='Can not decode content-encoding: br'" in str(e):
        print(f"{Fore.LIGHTYELLOW_EX}[WARNING] {Fore.YELLOW} {langs.aihottp_error[config_selfbot.lang]}{Style.RESET_ALL}")
        fix_aiohttp()
    else:
        print(f"{Fore.LIGHTRED_EX}[CRITICAL] {Fore.RED}{langs.weird_error[config_selfbot.lang]} {e} {Style.RESET_ALL}")
