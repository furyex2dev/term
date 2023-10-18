import os
import moduls.shell as shell
from libs.defines import *
from libs.printwith import *

import shutil

if os.path.isfile(".term_config"):
    pass
else:
    open(".term_config", "w+").close()

    with open(".term_config", "a") as f:
        f.truncate(0)

def prepareConfig():
    shutil.copy(".term_config", f"/home/{User.username}/")
    os.rename(f"/home/{User.username}/.term_config", f"/home/{User.username}/.old_term_config")
    printlnWithBold(Colors.GREEN, Colors.BOLD, f"Old configuration file copied to /home/{User.username}/.old_term_config")
    with open(".term_config", "a") as f:
            f.truncate(0)

def startConfig():
    _sconfig = input("Are you sure to reconfigure Term? (y | n): ")
    if _sconfig == "y":
        prepareConfig()
    else:
        return
    with open(".term_config", "a") as f:
        #for command input
        cmdColorTo = input("Plese choose color (colors: 'help'): ")
        welcomeColorTo = input("Welcome text: ")
        pcInfoColor = input("PC Info text color: ")
        showPc = input("Show PC Info on startup (1: yes, 0: no): ")
        emoji = input("Choose an emoji (for emojis: help emojis): ")
        f.write(f"INPUT_COLOR: {cmdColorTo}\n")
        f.write(f"WELCOME_TEXT: {welcomeColorTo}\n")
        f.write(f"PC_INFO_COLOR: {pcInfoColor}\n")
        f.write(f"SHOW_PC_INFO: {showPc}\n")
        f.write(f"WELCOME_EMOJI: {emoji}")
        input("You can do more customization in .term_config soon.\n")
        f.close()
        shell.runShellCommandsExternal("restart", Paths.main_path)

with open(".term_config", "r") as f:
    getColor = f.readline()
    getWelcome = f.readline()
    getPcInfo = f.readline()
    getShowPc = f.readline()
    getEmoji  = f.readline()
    _welcomeText = getWelcome.replace("\n", "")[14:]
    registeredColor = getColor.replace("\n", "")[13:]
    _pcInfoColor = getPcInfo.replace("\n", "")[15:]
    _showPc = getShowPc.replace("\n", "")[14:]
    _emoji = getEmoji.replace("\n", "")[15:]