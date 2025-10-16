from auxiliar.clear import clear

def caminho_guerreiro() -> None:

    #variáveis booleanas para evitar muitos alinhamentos de if dentro de outros if o que deixaria muito dificil a construção da história
    cidade:bool=False
    torre:bool=False

    continua_explorando_cidade:bool=False

    descansar:bool=False

    tatica:bool=False
    desviar:bool=False

    fugir:bool=False

    explorar:bool=False
    avancar:bool=False

    lava:bool=False
    gelo:bool=False
    outra:bool=False

    ignorar:bool=False

    continuar_torre:bool=False
    procurar:bool=False

    bola:bool=False

    lutar_armadura:bool=False
    lutar_grupo_inimigos_A:bool=False
    lutar_grupo_inimigos_B:bool=False

    #todas as ramificações começam logo abaixo. os nomes das váriaveis usados nas estruturas IF indica quais ações foram tomadas para alcançar esse ponto da história, por tanto não há necessiadade de comentar cada um deles
    while True:
        clear()
        print("Era mais um dia normal em uma das principais cidades do reino até que um homem chegou. Ele usava uma roupa preta e tinha uma aura de maldade ao seu redor. Dois dias depois uma enorme torre negra foi erguida no centro da cidade. Vários monstros surgiram e tomaram a cidade. Você morava ali na região numa casa solitária na floresta. Você era um lenhador que usava as próprias mãos pra pegar madeira. De qualquer forma, o que você fará agora?")
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
            print("Você vai em direção a cidade procurando ajudar as pessoas. Você enfrenta vários monstros e consegue salvar várias pessoas evacuando uma grande parte das pessoas da cidade. Durante essa evacuação você consegue salvar um soldado da cidade da morte certa. Ele decide se juntar a você. O que fará agora?")
            escolha: str = input("1 | continua explorando \n2 | ir para torre \n\n|| ")

            match escolha:
                case '1':
                    continua_explorando_cidade=True
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
            print("Você decide ir diretamente para torre sozinho. No meio do caminho aparecem muitos monstros:")
            escolha: str = input("1 | lutar \n2 | ignorar \n\n|| ")

            match escolha:
                case '1':
                    lutar_grupo_inimigos_A=True
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
            print("Vocês decidem ir diretamente para torre. No meio do caminho aparecem muitos monstros:")
            escolha: str = input("1 | lutar \n2 | ignorar \n\n|| ")

            match escolha:
                case '1':
                    lutar_grupo_inimigos_A=True
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
    
    if torre and lutar_grupo_inimigos_A:
        while True:
            clear()
            print("Você luta contra eles e percebe que sem uma arma dificilmente vai ser capaz de limpar a torre sozinho. Felizmente um dos monstros estava carregando uma espada adequada pra você. O que fara agora?")
            escolha: str = input("1 | continuar \n2 | procurar \n\n|| ")

            match escolha:
                case '1':
                    continuar_torre=True
                    break
                case '2':
                    procurar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if torre and lutar_grupo_inimigos_A and procurar:
        while True:
            clear()
            print("Você procura por mais alguma coisa entre os corpos dos monstros que possa ser útil e encontra uma pequena esfera de metal, pode ser útil como arremessavel. Um escudo pequeno e um capacete que mal cabe na sua cabeça, mas é melhor que nada. Você então vai até a torre. Chegando lá você encontra uma armadura viva que havia acabado de matar um homem na frente da entrada. O que fara?")
            escolha: str = input("1 | enfrentar \n2 | bola \n3 | fugir \n\n|| ")

            match escolha:
                case '1':
                    lutar_armadura=True
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
    
    if torre and lutar_grupo_inimigos_A and procurar and bola:
        while True:
            clear()
            print("Você arremessa a bola de metal contra a armadura. Para sua surpresa a esfera solta um brilho azul no momento em que encosta na armadura e a armadura cai em pedaços. Você pega devolta a esfera pois ela pode ter alguma utilidade. O que fará agora?")
            escolha: str = input("1 | seguir \n2 | descansar \n\n|| ")

            match escolha:
                case '1':
                    continuar_torre=True
                    break
                case '2':
                    descansar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if torre and lutar_grupo_inimigos_A and procurar and bola and descansar:
        clear()
        print("Você descansa um pouco afinal não está se sentindo tão bem assim. Você percebe algumas coisas: a dor de cabeça piorando, uma tontura, seu cabelo caindo. Em algum momento você mal tem força pra se mover e depois de mais um tempo você morre. Parabéns, você morreu de envenenamento por radiação.")
        input("\nPressione Enter para continuar...")
        return
    
    if torre and lutar_grupo_inimigos_A and procurar and bola and continuar_torre:
        while True:
            clear()
            print("Você sente uma leve dor de cabeça, mas não deve ser problema. Você segue em frente pra dentro da torre e encontra mais inimigos:")
            escolha: str = input("1 | atacar \n2 | bola \n3 | fugir \n\n|| ")

            match escolha:
                case '1':
                    lutar_grupo_inimigos_B=True
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
    
    if torre and lutar_grupo_inimigos_A and procurar and bola and continuar_torre and lutar_grupo_inimigos_B:
        clear()
        print("Você enfrenta todos os monstros. Com o escudo e a espada você realmente consegue lidar com todos. Quando você termina você tá completamente exausto até que você vomita e percebe um pouco de sangue. Você se sente tonto e cai no chão mal conseguindo se levantar leva. Mais algum tempo até você finalmente morrer. Parabéns, você morreu de envenenamento por radiação.")
        input("\nPressione Enter para continuar...")
        return
    
    if torre and lutar_grupo_inimigos_A and procurar and bola and continuar_torre and fugir:
        clear()
        print("Você tenta fugir e até que consegue, mas você é pego por outros monstros que você não eliminou e eles te matam. Parabéns, você morreu por preguiça.")
        input("\nPressione Enter para continuar...")
        return
    
    if torre and lutar_grupo_inimigos_A and procurar and bola and continuar_torre:
        clear()
        print("Você usa a bola mais uma vez e quando ela acerta algo de metal aquele brilho azul acontece dessa vez você consegue ver os ossos pela pele dos monstros. Isso não parece afetar eles tanto assim, já você começa a vomitar ali mesmo e se sente fraco. Infelizmente os monstros te matam antes que consiga se recuperar, porém eles também morrem ao longo dos proximos dias graças aos poderes dessa bola de metal. Parabéns, você morreu.")
        input("\nPressione Enter para continuar...")
        return

    if torre and lutar_grupo_inimigos_A and procurar and lutar_armadura:
        while True:
            clear()
            print("Você ataca a armadura aproveitando esse momento em que ela esta meio distraida para acertar um ataque certeiro que derruba sua cabeça fazendo ela se desmontar completamente. Agora você entra na torre só para se deparar com um enorme grupo de inimigos. O que fara agora?")
            escolha: str = input("1 | enfrentar \n2 | bola \n3 | fugir \n\n|| ")

            match escolha:
                case '1':
                    lutar_grupo_inimigos_B=True
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
    
    if torre and lutar_grupo_inimigos_A and procurar and lutar_armadura and bola:
        clear()
        print("Você usa a bola e manda ela contra os inimigos ela acaba ricocheteando e entrando dentro de uma lata de metal, um brilho azul cega você e seus inimigos, por alguns segundos só parece ser isso mas começa a ficar quente e você começa a se sentir tonto, não só você mas como todos seus inimigos também. Rapidamente todos caem no chão morrendo dolorosamente. Parabéns, vocês morreram de envenenamento por radiação.")
        input("\nPressione Enter para continuar...")
        return

    if torre and lutar_grupo_inimigos_A and procurar and lutar_armadura and lutar_grupo_inimigos_B:
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
    
    if torre and lutar_grupo_inimigos_A and procurar and lutar_armadura and lutar_grupo_inimigos_B  and explorar:
        clear()
        print("Você olha em volta do andar procurando por algo até que você acha uma pequena chave preta. Você pega ela e guarda no bolso onde esta carregando a bola. Imediatamente você morre. Final buraco negro.")
        input("\nPressione Enter para continuar...")
        return
    
    if torre and lutar_grupo_inimigos_A and procurar and lutar_armadura and lutar_grupo_inimigos_B and avancar:
        while True:
            clear()
            print("Você sobe a torre chegando de frente a duas portas. Uma de lava outra de gelo:")
            escolha: str = input("1 | porta de lava \n2 | porta de gelo \n\n|| ")

            match escolha:
                case '1':
                    lava=True
                    break
                case '2':
                    gelo=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if torre and lutar_grupo_inimigos_A and procurar and lutar_armadura and lutar_grupo_inimigos_B and avancar and lava:
        clear()
        print("Você vai até a porta de lava e não tem muita certeza de como abrir ela até que decide usar a bola afinal ela tem que ser útil para alguma coisa. No momento em que a bola toca a lava uma enorme explosão acontece. Tudo num raio de 200 metros é deletado da face da terra. Final explosão nuclear.")
        input("\nPressione Enter para continuar...")
        return
    
    if torre and lutar_grupo_inimigos_A and procurar and lutar_armadura and lutar_grupo_inimigos_B and avancar and gelo:
        clear()
        print("Você vai até a porta de gelo e não tem muita certeza de como abrir ela até que você decide usar a bola afinal ela tem que ser útil para alguma coisa. No momento em que você encosta a bola na porta nada acontece, mas seu dedo acaba encostando na porta o que te congela por inteiro e te mata. Final congelamento")
        input("\nPressione Enter para continuar...")
        return

    if torre and lutar_grupo_inimigos_A and continuar_torre:
        while True:
            clear()
            print("Você segue indo até a torre e encontra uma armadura viva enorme e um soldado vindo também. O que fara?")
            escolha: str = input("1 | atacar \n2 | fugir \n\n|| ")

            match escolha:
                case '1':
                    lutar_armadura=True
                    break
                case '2':
                    fugir=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if torre and lutar_grupo_inimigos_A and continuar_torre and fugir:
        clear()
        print("Você tenta fugir da armadura, o soldado fica sozinho enfrentando ela e  morre, porém logo a armadura vai atrás de você, mas ela nem precisa chegar em você, diversos monstros te atacam enquanto você corre. Parabéns, você morreu como um covarde.")
        input("\nPressione Enter para continuar...")
        return
    
    #ponto de encontro: código A (apenas para me ajudar a identificar)
    if torre and lutar_grupo_inimigos_A and continuar_torre and lutar_armadura:
        while True:
            clear()
            print("Vocês dois enfrentam a armadura juntos e graças a sua espada é relativamente fácil. Vocês logo lidam com a armadura e fazem um tipo de amizade. Vocês entram dentro da torre e encontram um enorme número de monstros. O que farão?")
            escolha: str = input("1 | fugir \n2 | enfrentar \n\n|| ")

            match escolha:
                case '1':
                    fugir=True
                    break
                case '2':
                    lutar_grupo_inimigos_B=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if cidade and continua_explorando_cidade:
        while True:
            clear()
            print("Vocês continuam explorando a cidade e ajudando as últimas pessoas a saírem além de limparem grande parte dos monstros que estavam ali. Vocês então podem finalmente ir até a torre, porém vocês estão meio desgastados:")
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
        
    if cidade and continua_explorando_cidade and torre:
        while True:
            clear()
            print("Sem descansar, vocês avançam até a torre. Quando chegam na entrada, uma grande armadura viva abre a porta. Pelo cansaço vocês não tem reação contra essa coisa que rapidamente mata o seu companheiro:")
            escolha: str = input("1 | atacar \n2 | fugir \n\n|| ")

            match escolha:
                case '1':
                    lutar_armadura=True
                    break
                case '2':
                    fugir=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if cidade and continua_explorando_cidade and torre and lutar_armadura:
        clear()
        print("Você tenta remover a cabeça da armadura, porém você não tem força o suficiente pra isso nesse momento. A armadura usa sua espada para te matar. Parabéns, você morreu.")
        input("\nPressione Enter para continuar...")
        return
    
    if cidade and continua_explorando_cidade and descansar:
        while True:
            clear()
            print("Vocês encontram um lugar para descansar e conseguem recuperar suas energias e logo vão até a porta da torre. Quando vocês chegam na torre a porta abre por si só e uma enorme armadura viva aparece ali andando em direção a vocês:")
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
    
    if cidade and continua_explorando_cidade and descansar and tatica:
        clear()
        print("Vocês tentam usar uma tática, você aguenta um ataque da armadura para deixar com que seu colega arranque sua cabeça. Ele desmonta completamente, porém o ataque não é algo que você consiga sobreviver. Parabéns, você morreu.")
        input("\nPressione Enter para continuar...")
        return
    
    if cidade and continua_explorando_cidade and descansar and desviar:
        while True:
            clear()
            print("Você desvia do ataque da armadura o que abre a  oportunidade pra algo:")
            escolha: str = input("1 | atacar \n2 | fugir \n\n|| ")

            match escolha:
                case '1':
                    lutar_armadura=True
                    break
                case '2':
                    fugir=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if cidade and continua_explorando_cidade and (descansar or torre) and fugir:
        clear()
        print("Você corre até uma construção que estava pegando fogo e quase caindo a armadura te perseguindo. Você derruba ela depois da armadura entrar. Você volta até a torre e tem muitas criaturas lá. Você é incapaz de fazer qualquer coisa contra eles pois está muito cansado. Parabéns, você morreu.")
        input("\nPressione Enter para continuar...")
        return
    
    #ponto de encontro: código A (apenas para me ajudar a identificar)
    if cidade and continua_explorando_cidade and descansar and desviar and lutar_armadura:
        while True:
            clear()
            print("Vocês aproveitam a oportunidade pra atacar a armadura, removendo o capacete o que desmonta a armadura inteira. Vocês entram para dentro da torre e existem inúmeros inimigos ali dentro:")
            escolha: str = input("1 | fugir \n2 | enfrentar \n\n|| ")

            match escolha:
                case '1':
                    fugir=True
                    break
                case '2':
                    lutar_grupo_inimigos_B=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")

    if ((cidade and continua_explorando_cidade and descansar and desviar and lutar_armadura) or (torre and lutar_grupo_inimigos_A and continuar_torre and lutar_armadura)) and lutar_grupo_inimigos_B:
        clear()
        print("Vocês tentam enfnretar todos os monstros ao mesmo tempo. Apesar de individualmente serem fracos, juntos os monstros são capazes de te derrotar. Parabéns, vocês morreram brutalmente.")
        input("\nPressione Enter para continuar...")
        return
    
    if ((cidade and continua_explorando_cidade and descansar and desviar and lutar_armadura) or (torre and lutar_grupo_inimigos_A and continuar_torre and lutar_armadura)) and fugir:
        while True:
            clear()
            print("Vocês percebem que não é possível enfrentar todos os monstros ao mesmo tempo então escolhem atrair os monstros para uma armadilha, uma construção que estava pegando fogo. Quando os monstros entram vocês saem derrubando a casa e matando todos. Vocês então vão de volta até a torre. O que vão fazer?")
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
    
    if ((cidade and continua_explorando_cidade and descansar and desviar and lutar_armadura) or (torre and lutar_grupo_inimigos_A and continuar_torre and lutar_armadura)) and fugir and avancar:
        clear()
        print("Vocês chegam em um lugar com duas portas. Uma de gelo e outra de lava. Infelizmente você não tem como abrir nenhuma delas só que nenhum de vocês sabem disso já que não são magos. Encostando nas portas pra tentar entender como abrir vocês dois morrem, parabéns.")
        input("\nPressione Enter para continuar...")
        return

    if ((cidade and continua_explorando_cidade and descansar and desviar and lutar_armadura) or (torre and lutar_grupo_inimigos_A and continuar_torre and lutar_armadura)) and fugir and explorar:
        while True:
            clear()
            print("Você encontra uma chave preta e nada mais que seja útil. Subindo na torre vocês encontram duas portas. Uma de lava e outra de gelo")
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
    
    if ((cidade and continua_explorando_cidade and descansar and desviar and lutar_armadura) or (torre and lutar_grupo_inimigos_A and continuar_torre and lutar_armadura)) and fugir and explorar and lava:
        clear()
        print("Você usa a chave pra abrir a porta de lava. A chave some e você consegue entrar num lugar com o dragão o soldado fala que vai trazer ajuda. Você fica responsável por enfrentar o dragão enquanto a cavalaria não chega, mas você provavelmente já sabe como isso acaba. Final mortis.")
        input("\nPressione Enter para continuar...")
        return
    
    if ((cidade and continua_explorando_cidade and descansar and desviar and lutar_armadura) or (torre and lutar_grupo_inimigos_A and continuar_torre and lutar_armadura)) and fugir and explorar and gelo:
        clear()
        print("Você usa a chave pra abrir a porta de gelo. A chave some e você consegue entrar numa enorme biblioteca cheia de itens mágicos das maiores variedades. Você encontra um cajado de gelo que provavelmente pode ser usado para abrir a porta de lava, uma pena que a maldição desse lugar desceu sobre você, afinal você não é um paladino, você mata o soldado que lhe acompanhou até agora. Parabéns você virou um escravo do rei demônio e ira defender essa torre. Final moderatus")
        input("\nPressione Enter para continuar...")
        return
    
    if ((cidade and continua_explorando_cidade and descansar and desviar and lutar_armadura) or (torre and lutar_grupo_inimigos_A and continuar_torre and lutar_armadura)) and fugir and explorar and outra:
        clear()
        print("Você usa a chave preta na parede abrindo pra um lugar completamente negro. Vocês entram, mas não tem nada lá. Você fica preso pelo resto da eternidade sozinho nessa escuridão. Final obscuris.")
        input("\nPressione Enter para continuar...")
        return