from libs.filerm import filerm
from libs.printwith import *
from libs.defines import Colors

def fetcherm():
    printlnWithBold(Colors.TGRN, "\nWelcome to Fetcherm")

    hostUser = f"{Colors.TGRN}{Colors.BOLD}[{Colors.TLGN}{Colors.BOLD}{filerm.user}{Colors.TRED}{Colors.BOLD}@{Colors.TLBL}{Colors.BOLD}{filerm.host}{Colors.TGRN}{Colors.BOLD}]{Colors.TNRM}"
    print(hostUser)
    for i in range(len(f"[{filerm.user}@{filerm.host}]")):
        print("-", end='')

    printWithBold(Colors.TYLW, f"\nOS:  {Colors.TWHT}{filerm.getOS('os-name')}")
    printWithBold(Colors.TYLW, f"Kernel: {Colors.TWHT}{filerm.getOS('kernel')}")
    printWithBold(Colors.TYLW, f"Shell: {Colors.TWHT}{filerm.getOS('shell')}")
    printWithBold(Colors.TYLW, f"DE: {Colors.TWHT}{filerm.getOS('desktop-env')}")
    printWithBold(Colors.TYLW, f"WM: {Colors.TWHT}{filerm.getOS('window-mngr').capitalize()}")
    printWithBold(Colors.TYLW, f"Theme: {Colors.TWHT}{filerm.ReadTheme()}")

    printWithBold(Colors.TYLW, f"CPU: {Colors.TWHT}{filerm.ReadCPU()}")
    printWithBold(Colors.TYLW, f"GPU: {Colors.TWHT}{filerm.ReadGPU()}")
    printWithBold(Colors.TYLW, f"Memory: {Colors.TWHT}{filerm.CurrentRam() + ' / ' + filerm.ReadMemory('mb')}")
    printWithBold(Colors.TYLW, f"Disk size: {Colors.TWHT}{filerm.ReadDisk()}\n")