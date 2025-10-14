from auxiliar.clear import clear

def caminho_dragao() -> None:

    auxilio:bool=False

    questionar:bool=False
    matar:bool=False

    clear()
    nome:str=input("Escolha o seu nome: ")
    if nome == "auxilio":
        auxilio=True
    
    if not(auxilio):
        while True:
            clear()
            print("Você é um dragão qualquer, você estava vivendo uma vida tranquila na sua caverna em sua pilha de tesouros, você vê um homem chegando na entrada da caverna:")
            escolha: str = input("1 | questionar \n2 | matar \n\n|| ")

            match escolha:
                case '1':
                    questionar=True
                    break
                case '2':
                    matar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")