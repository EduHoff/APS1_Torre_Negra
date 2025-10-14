from .clear import clear

def controle_main_loop() -> None:
    from main import main

    while True:
        clear()
        print("Por favor, escolha se deseja continuar ou não o jogo:")
        escolha: str = input("1 | sair \n2 | reiniciar\n\n|| ")
        match escolha:
            case '1':
                break
            case '2':
                main()
                break
            case _:
                print("Opção inválida! Tente novamente.")
                input("\nPressione Enter para continuar...")