import os
import platform

#função que detecta se o SO é um windows ou algo baseado no UNIX para limpar a tela do terminal
def clear() -> None:
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")