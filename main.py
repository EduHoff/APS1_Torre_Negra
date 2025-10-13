from auxiliar import clear, controle_main_loop
from caminhos import caminho_mago, caminho_guerreiro, caminho_dragao

def main() -> None:
    while True:
        clear()
        print("Por favor, escolha uma classe:")
        escolha: str = input("0 | mago \n1 | lutador \n2 | dragão \n\n|| ")

        match escolha:
            case '0':
                caminho_mago()
                break
            case '1':
                caminho_guerreiro()
                break
            case '2':
                caminho_dragao()
                break
            case _:
                print("Opção inválida! Tente novamente.")
                input("\nPressione Enter para continuar...")

    controle_main_loop()

if __name__ == "__main__":
    main()