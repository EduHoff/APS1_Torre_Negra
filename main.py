from auxiliar import clear, controle_main_loop
from caminhos import caminho_mago, caminho_guerreiro, caminho_dragao

#programa principal onde o usuário pode escolher sua classe e por consequência sua jornada
def main() -> None:
    while True:
        clear()
        print("Por favor, escolha uma classe:")
        escolha: str = input("1 | mago \n2 | guerreiro \n3 | dragão \n\n|| ")

        match escolha:
            case '1':
                caminho_mago()
                break
            case '2':
                caminho_guerreiro()
                break
            case '3':
                caminho_dragao()
                break
            case _:
                print("Opção inválida! Tente novamente.")
                input("\nPressione Enter para continuar...")

    controle_main_loop() #função que vai requisitar ao usuário se ele vai querer reiniciar o rpg ou sair do programa

if __name__ == "__main__":
    main()