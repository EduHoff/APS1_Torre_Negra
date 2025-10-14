from auxiliar.clear import clear

def caminho_dragao() -> None:

    auxilio:bool=False

    questionar_homem:bool=False
    matar:bool=False

    questionar_homem_novamente:bool=False

    mandar_homem_embora:bool=False

    seguir_homem:bool=False
    dormir:bool=False

    destruir:bool=False
    dominar:bool=False
    fugir:bool=False

    porta_frente:bool=False
    parede:bool=False



    clear()
    nome:str=input("Escolha o seu nome: ")
    if nome.lower() == "auxilio":
        auxilio=True
    
    if not(auxilio):
        while True:
            clear()
            print("Você é um dragão qualquer, você estava vivendo uma vida tranquila na sua caverna em sua pilha de tesouros, você vê um homem chegando na entrada da caverna:")
            escolha: str = input("1 | questionar \n2 | matar \n\n|| ")

            match escolha:
                case '1':
                    questionar_homem=True
                    break
                case '2':
                    matar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if questionar_homem:
        while True:
            clear()
            print("Você pergunta o que ele estava buscando, o homem não responde e tenta te atacar porem ele é apenas um homem, nada que ele faz consegue te machucar o que você faz?")
            escolha: str = input("1 | revidar \n2 | questionar \n\n|| ")

            match escolha:
                case '1':
                    matar=True
                    break
                case '2':
                    questionar_homem_novamente=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if questionar_homem and questionar_homem_novamente:
        while True:
            clear()
            print("Você pergunta denovo, ele continua sem responder até ele se cansar de te atacar sem parar e cair no chão, ele fala que estava em busca do seu tesouro mas que não esperava que você fosse tão resistente, o que fara com ele?")
            escolha: str = input("1 | mandar embora \n2 | matar \n\n|| ")

            match escolha:
                case '1':
                    mandar_homem_embora=True
                    break
                case '2':
                    matar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if matar:
        clear()
        print("Você decide matar o homem, verdadeiramente um tolo por tentar enfrentar um dragão sozinho, você volta a dormir, porem seu sono é interrompido por um grande exército, você luta valorosamente contra eles porem eles te pegaram em um lugar onde a vantagem é deles, parabéns você morreu.")
        input("\nPressione Enter para continuar...")
        return
    
    if questionar_homem and questionar_homem_novamente and mandar_homem_embora:
        while True:
            clear()
            print("Você manda ele embora, não ha nescessidade de matar um ser tão fraco assim, ele foge assim que você ordena, o que fará?")
            escolha: str = input("1 | seguir \n2 | dormir \n\n|| ")

            match escolha:
                case '1':
                    seguir_homem=True
                    break
                case '2':
                    dormir=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if questionar_homem and questionar_homem_novamente and mandar_homem_embora and dormir:
        clear()
        print("Você volta ao seu sono de beleza, infelizmente durante seu sono você é atacado, não por um unico homem mas sim por um enorme exército preparado pra lhe eliminar, sua morte é brutal, parabéns.")
        input("\nPressione Enter para continuar...")
        return
    
    if questionar_homem and questionar_homem_novamente and mandar_homem_embora and seguir_homem:
        while True:
            clear()
            print("Você espera um pouco depois dele sair pra seguir ele você encontra um enorme exército do lado de fora da sua caverna com todos os tipos de armas, eles vieram pra lhe matar o que fara?")
            escolha: str = input("1 | destruir \n2 | dominar \n3 | fugir \n\n|| ")

            match escolha:
                case '1':
                    destruir=True
                    break
                case '2':
                    dominar=True
                    break
                case '3':
                    fugir=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if questionar_homem and questionar_homem_novamente and mandar_homem_embora and seguir_homem and fugir:
        clear()
        print("Você não quer lidar com todo esse problema honestamente é muito cansativo, então você só pega a parte da montanha com sua caverna e vai para outro lugar onde você possa viver em paz, final vida tranquila.")
        input("\nPressione Enter para continuar...")
        return
    
    if questionar_homem and questionar_homem_novamente and mandar_homem_embora and seguir_homem and dominar:
        clear()
        print("Você decide que ira fazer eles se arrependerem disso, você devasta o exército e logo em seguida vai até o reino de onde estes soldados haviam vindo, você facilmente mata o rei e se torna o novo rei, instaurando uma ditadura onde todos sofrem, final dominador.")
        input("\nPressione Enter para continuar...")
        return
    
    if questionar_homem and questionar_homem_novamente and mandar_homem_embora and seguir_homem and destruir:
        clear()
        print("Você sem piedade alguma mata todos do exército, mesmo estando preparados eles não estavam esperando te enfrentar assim, você consegue matar todos mas somente isso não é bastante para apaziguar sua furia, você decide destruir o reino de onde eles haviam vindo, e qualquer outro resquicio de civilização que encontra no seu caminho, você é a tormenta final destrutivo.")
        input("\nPressione Enter para continuar...")
        return
    
    if auxilio:
        while True:
            clear()
            print("Você é o rei dragão, o mais poderoso dentre todos os dragões, há muito tempo atrás quando você ainda era jovem você enfrentou o rei demonio, ele infelizmente venceu contra você, e te aprisionou em um limbo, porem sua força cresceu demais, ele teve que te colocar numa torre em alguma cidade aleatória, e foi aprisionado lá, se algum mago surgisse ele poderia usar das magias guardadas para lhe matar, felizmente o mago que lhe encontrou não era um desses, ele decidiu conversar, diferente dos outros soldados que haviam entrado anteriormente, graças a ele você foi verdadeiramente libertado, agora mais poderoso que nunca é hora de enfrentar o rei demonio, com um auxilio, você aproveita pra entregar para o mago todo conhecimento magico que você poderia entregar a um mortal, para ele poder lhe ajudar verdadeiramente na luta, e tambem usou sua magia para aprimorar a ursa, com os dois nas suas costas você voou até o castelo do rei demonio como entrara na torre?")
            escolha: str = input("1 | porta da frente \n2 | parede \n\n|| ")

            match escolha:
                case '1':
                    porta_frente=True
                    break
                case '2':
                    parede=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")