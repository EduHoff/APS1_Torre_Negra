from auxiliar.clear import clear

def caminho_guerreiro() -> None:

    #variáveis booleanas para evitar muitos alinhamentos de if dentro de outros if o que deixaria muito dificil a construção da história
    cidade:bool=False
    torre:bool=False

    continua_explorando:bool=False

    descansar:bool=False

    tatica:bool=False
    desviar:bool=False

    atacar:bool=False
    fugir:bool=False

    enfrentar:bool=False

    explorar:bool=False
    avancar:bool=False

    lava:bool=False
    gelo:bool=False
    outra:bool=False

    lutar:bool=False
    ignorar:bool=False

    continuar:bool=False
    procurar:bool=False

    bola:bool=False

    #todas as ramificações começam logo abaixo. os nomes das váriaveis usados nas estruturas IF indica quais ações foram tomadas para alcançar esse ponto da história, por tanto não há necessiadade de comentar cada um deles
    while True:
        clear()
        print("Era mais um dia normal em uma das principais cidades do reino, até que um homem chegou, ele usava uma roupa preta e tinha uma aura de maldade ao seu redor, dois dias depois uma enorme torre negra foi erguida no centro da cidade, vários monstros surgiram e tomaram a cidade, você morava ali na região numa casa solitária na floresta, você era um lenhador que usava as próprias mãos pra pegar madeira, de qualquer forma o que você fará agora?")
        escolha: str = input("1 | ir pra cidade \n2 | ir pra torre \n\n|| ")

        match escolha:
            case '1':
                cidade=True
                break
            case '2':
                torre=True
                break
            case _:
                print("Opção inválida! Tente novamente.")
                input("\nPressione Enter para continuar...")
    
    if cidade:
        while True:
            clear()
            print("Você vai em direção a cidade procurando ajudar as pessoas, você enfrenta vários monstros e consegue salvar varias pessoas evacuando uma grande parte das pessoas da cidade, durante essa evacuação você consegue salvar um soldado da cidade da morte certa, ele decide se juntar a você o que fará agora?")
            escolha: str = input("1 | continua explorando \n2 | ir para torre \n\n|| ")

            match escolha:
                case '1':
                    continua_explorando=True
                    break
                case '2':
                    torre=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")

    if torre and not(cidade):
        while True:
            clear()
            print("Você decide ir diretamente para torre sozinho, no meio do caminho aparecem muitos monstros:")
            escolha: str = input("1 | lutar \n2 | ignorar \n\n|| ")

            match escolha:
                case '1':
                    lutar=True
                    break
                case '2':
                    ignorar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if torre and cidade:
        while True:
            clear()
            print("Vocês decidem ir diretamente para torre, no meio do caminho aparecem muitos monstros:")
            escolha: str = input("1 | lutar \n2 | ignorar \n\n|| ")

            match escolha:
                case '1':
                    lutar=True
                    break
                case '2':
                    ignorar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if torre and ignorar:
        clear()
        print("Você ignora os diversos monstros e vai direto até a torre. O problema é que quando você chega tem uma enorme armadura viva na porta. Com tantos inimigos ao mesmo tempo você não tem como lidar com todos e morre. Parabéns, você morreu por negligência.")
        input("\nPressione Enter para continuar...")
        return
    
    if torre and lutar:
        while True:
            clear()
            print("Você luta contra eles e percebe que sem uma arma dificilmente vai ser capaz de limpar a torre sozinho, felizmente um dos monstros estava carregando uma espada adequada pra você, o que fara agora?")
            escolha: str = input("1 | continuar \n2 | procurar \n\n|| ")

            match escolha:
                case '1':
                    continuar=True
                    break
                case '2':
                    procurar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if torre and lutar and procurar: #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        while True:
            clear()
            print("Você procura por mais alguma coisa entre os corpos dos monstros que possa ser útil e encontra uma pequena esfera de metal, pode ser útil como arremessavel, um escudo pequeno e um capacete que mal cabe na sua cabeça, mas é melhor que nada. Você então vai até a torre chegando lá voce encontra uma armadura viva, que havia acabado de matar um homem na frente da entrada. O que fara?")
            escolha: str = input("1 | enfrentar \n2 | bola \n3 | fugir \n\n|| ")

            match escolha:
                case '1':
                    enfrentar=True
                    break
                case '2':
                    bola=True
                    break
                case '3':
                    fugir=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")

    if torre and lutar and procurar and enfrentar:
        while True:
            clear()
            print("Você luta valorosamente contra os inumeros inimigos e graças ao escudo você até que consegue matar todos, mas isso te cansa enormemente. O que fara agora?")
            escolha: str = input("1 | avançar \n2 | explorar \n\n|| ")

            match escolha:
                case '1':
                    avancar=True
                    break
                case '2':
                    explorar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if torre and lutar and procurar and enfrentar and explorar:
        clear()
        print("Você olha em volta do andar procurando por algo até que você acha uma pequena chave preta. Você pega ela e guarda no bolso onde esta carregando a bola, imediatamente você morre. Final buraco negro.")
        input("\nPressione Enter para continuar...")
        return
    

    #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    if torre and lutar and continuar:
        while True:
            clear()
            print("Você segue indo até a torre e encontra uma armadura viva enorme e um soldado vindo também. O que fara?")
            escolha: str = input("1 | atacar \n2 | fugir \n\n|| ")

            match escolha:
                case '1':
                    atacar=True
                    break
                case '2':
                    fugir=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if torre and lutar and continuar and fugir:
        clear()
        print("Você tenta fugir da armadura, o soldado fica sozinho enfrentando ela e ele morre, porém logo a armadura vai atrás de você, mas ela nem precisa chegar em você, diversos monstros te atacam enquanto você corre. Parabéns, você morreu como um covarde.")
        input("\nPressione Enter para continuar...")
        return
    
    #ponto de encontro: código A (apenas para me ajudar a identificar)
    if torre and lutar and continuar and atacar:
        while True:
            clear()
            print("Vocês dois enfrentam a armadura juntos, graças a sua espada é relativamente fácil, vocês logo lidam com a armadura e fazem um tipo de amizade, vocês entram dentro da torre e encontram um enorme numero de monstros. O que farão?")
            escolha: str = input("1 | fugir \n2 | enfrentar \n\n|| ")

            match escolha:
                case '1':
                    fugir=True
                    break
                case '2':
                    enfrentar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if cidade and continua_explorando:
        while True:
            clear()
            print("Vocês continuam explorando a cidade e ajudando as ultimas pessoas a saírem além de limparem grande parte dos monstros que estavam ali, vocês então podem finalmente ir até a torre porém vocês estão meio desgastados:")
            escolha: str = input("1 | descansar \n2 | ir para torre \n\n|| ")

            match escolha:
                case '1':
                    descansar=True
                    break
                case '2':
                    torre=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
        
    if cidade and continua_explorando and torre:
        while True:
            clear()
            print("Sem descansar vocês avançam até a torre, quando chegam na porta uma grande armadura viva abre a porta, pelo cansaço vocês não tem reação contra essa coisa que rapidamente mata o seu companheiro:")
            escolha: str = input("1 | atacar \n2 | fugir \n\n|| ")

            match escolha:
                case '1':
                    atacar=True
                    break
                case '2':
                    fugir=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if cidade and continua_explorando and torre and atacar:
        clear()
        print("Você tenta remover a cabeça da armadura porem você não tem força o suficiente pra isso nesse momento, a armadura usa sua espada pra te matar, parabéns você morreu.")
        input("\nPressione Enter para continuar...")
        return
    
    
    
    if cidade and continua_explorando and descansar:
        while True:
            clear()
            print("Vocês encontram um lugar para descansar e conseguem recuperar suas energias e logo vão até a porta da torre, quando vocês chegam na torre a porta abre por si mesma uma enorme armadura viva ali andando em direção a vocês:")
            escolha: str = input("1 | tática \n2 | desviar \n\n|| ")

            match escolha:
                case '1':
                    tatica=True
                    break
                case '2':
                    desviar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if cidade and continua_explorando and descansar and tatica:
        clear()
        print("Vocês tentam usar uma tática, você aguenta um ataque da armadura pra deixar com que seu colega arranque sua cabeça, ele desmontando completamente, porem o ataque não é algo que você consiga sobreviver parabéns você morreu.")
        input("\nPressione Enter para continuar...")
        return
    
    if cidade and continua_explorando and descansar and desviar:
        while True:
            clear()
            print("Você desvia do ataque da armadura o que abre a  oportunidade pra algo:")
            escolha: str = input("1 | atacar \n2 | fugir \n\n|| ")

            match escolha:
                case '1':
                    atacar=True
                    break
                case '2':
                    fugir=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if cidade and continua_explorando and (descansar or torre) and fugir:
        clear()
        print("Você corre até uma construção que estava pegando fogo e quase caindo a armadura te perseguindo, você derruba ela depois da armadura entrar, você volta até a torre e tem muitas criaturas lá você é incapaz de fazer qualquer coisa contra eles pois está muito cansado, parabéns você morreu.")
        input("\nPressione Enter para continuar...")
        return
    
    #ponto de encontro: código A (apenas para me ajudar a identificar)
    if cidade and continua_explorando and descansar and desviar and atacar:
        while True:
            clear()
            print("Vocês aproveitam a oportunidade pra atacar a armadura, removendo o capacete o que desmonta a armadura inteira, vocês entram pra dentro da torre e existem inúmeros inimigos ali dentro:")
            escolha: str = input("1 | fugir \n2 | enfrentar \n\n|| ")

            match escolha:
                case '1':
                    fugir=True
                    break
                case '2':
                    enfrentar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")

    if ((cidade and continua_explorando and descansar and desviar and atacar) or (torre and lutar and continuar and atacar)) and enfrentar:
        clear()
        print("Vocês tentam enfnretar todos os monstros ao mesmo tempo. Apesar de individualmente serem fracos, juntos os monstros são capazes de te derrotar. Parabéns, vocês morreram brutalmente.")
        input("\nPressione Enter para continuar...")
        return
    
    if ((cidade and continua_explorando and descansar and desviar and atacar) or (torre and lutar and continuar and atacar)) and fugir:
        while True:
            clear()
            print("Vocês percebem que não é possível enfrentar todos os monstros ao mesmo tempo então escolhem atrair os monstros para uma armadilha, uma construção que estava pegando fogo, quando os monstros entram vocês saem derrubando a casa e matando todos, vocês então vão de volta até a torre o que vão fazer?")
            escolha: str = input("1 | explorar \n2 | avançar \n\n|| ")

            match escolha:
                case '1':
                    explorar=True
                    break
                case '2':
                    avancar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if ((cidade and continua_explorando and descansar and desviar and atacar) or (torre and lutar and continuar and atacar)) and fugir and avancar:
        clear()
        print("Vocês chegam em um lugar com duas portas uma de gelo e outra de lava, infelizmente você não tem como abrir nenhuma delas, só que nenhum de vocês sabem disso ja que não são magos, encostando nas portas pra tentar entender como abrir vocês dois morrem parabéns.")
        input("\nPressione Enter para continuar...")
        return

    if ((cidade and continua_explorando and descansar and desviar and atacar) or (torre and lutar and continuar and atacar)) and fugir and explorar:
        while True:
            clear()
            print("Você encontra uma chave preta, e nada mais que seja útil, subindo na torre vocês encontram duas portas uma de lava e outra de gelo")
            escolha: str = input("1 | porta de lava \n2 | porta de gelo \n3 | outra \n\n|| ")

            match escolha:
                case '1':
                    lava=True
                    break
                case '2':
                    gelo=True
                    break
                case '3':
                    outra=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if ((cidade and continua_explorando and descansar and desviar and atacar) or (torre and lutar and continuar and atacar)) and fugir and explorar and lava:
        clear()
        print("Você usa a chave pra abrir a porta de lava, a chave some e você consegue entrar num lugar com o dragão o soldado fala que vai trazer ajuda pra você, e você fica responsável por enfrentar o dragão enquanto a cavalaria não chega, mas você provavelmente já sabe como isso acaba, final mortis.")
        input("\nPressione Enter para continuar...")
        return
    
    if ((cidade and continua_explorando and descansar and desviar and atacar) or (torre and lutar and continuar and atacar)) and fugir and explorar and gelo:
        clear()
        print("Você usa a chave pra abrir a porta de gelo, a chave some e você consegue entrar numa enorme biblioteca cheia de itens mágicos das maiores variedades, você encontra um cajado de gelo que provavelmente pode ser usado para abrir a porta de lava, uma pena que a maldição desse lugar desceu sobre você, afinal você não é um paladino, você mata o soldado que lhe acompanhou até agora, parabéns você virou um escravo do rei demônio e ira defender essa torre, final moderatus")
        input("\nPressione Enter para continuar...")
        return
    
    if ((cidade and continua_explorando and descansar and desviar and atacar) or (torre and lutar and continuar and atacar)) and fugir and explorar and outra:
        clear()
        print("Você usa a chave preta na parede, abrindo pra um lugar completamente negro, vocês entram mas não tem nada lá, porem você fica preso pelo resto da eternidade sozinho nessa escuridão, final obscuris.")
        input("\nPressione Enter para continuar...")
        return
    
    
    
    