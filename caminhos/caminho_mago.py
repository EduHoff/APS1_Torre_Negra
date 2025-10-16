from auxiliar.clear import clear

def caminho_mago() -> None:

    #variáveis booleanas para evitar muitos alinhamentos de if dentro de outros if o que deixaria muito dificil a construção da história
    destrutiva:bool=False
    construtiva:bool=False

    carroca:bool=False
    caminhada:bool=False

    torre:bool=False
    arredores:bool=False

    questionar:bool=False
    atacar:bool=False

    matar_homem:bool=False
    nao_matar_homem:bool=False

    esperar:bool=False

    explorar:bool=False
    avancar:bool=False

    lava:bool=False
    gelo:bool=False

    ir_embora:bool=False

    matar_dragao:bool=False

    investigar:bool=False
    seguir_caminho:bool=False

    seguir_ursa:bool=False

    cidade:bool=False

    ajudar_dragaon:bool=False
    nao_ajudar_dragaon:bool=False

    #todas as ramificações começam logo abaixo. os nomes das váriaveis usados nas estruturas IF indica quais ações foram tomadas para alcançar esse ponto da história, por tanto não há necessiadade de comentar cada um deles
    while True:
        clear()
        print("Por favor, escolha seu foco de magia:")
        escolha: str = input("1 | destrutiva \n2 | construtiva \n\n|| ")

        match escolha:
            case '1':
                destrutiva=True
                break
            case '2':
                construtiva=True
                break
            case _:
                print("Opção inválida! Tente novamente.")
                input("\nPressione Enter para continuar...")
    
    if destrutiva:
        while True:
            clear()
            print("Existem boatos de um dragão em um reino próximo que está causando muitos problemas. Equipado com seu cajado de fogo, você está indo em direção ao dito reino, seja em busca de magias mais poderosas ou talvez liberar o reino desse mal. Escolha a sua forma de transporte:")
            escolha: str = input("1 | carroça \n2 | caminhada \n\n|| ")

            match escolha:
                case '1':
                    carroca=True
                    break
                case '2':
                    caminhada=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if destrutiva and caminhada:
        clear()
        print("Você por algum motivo decidiu ir caminhando até a torre. Você não foi feito pra isso. Durante sua caminhada suas provisões acabam e você é atacado por ursos. Você morre de forma cruel e dolorosa pois essa é a natureza. Eu diria parabéns mas eu sinto mais é pena de você.")
        input("\nPressione Enter para continuar...")
        return
    
    if destrutiva and carroca:
        while True:
            clear()
            print("Você acha um homem disposto a te levar até o reino. Durante a viagem você presta atenção no homem que é meio suspeito. Depois de algum tempo vocês chegam ao destino, uma enorme torre negra estava no centro do reino. Você sai da carroça. O que fará agora?")
            escolha: str = input("1 | seguir até a torre \n2 | investigar os arredores \n\n|| ")

            match escolha:
                case '1':
                    torre=True
                    break
                case '2':
                    arredores=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if destrutiva and carroca and torre:
        clear()
        print("Você leva uma facada pelas costas do homem suspeito. Por que você ignorou isso? Tu é burro?")
        input("\nPressione Enter para continuar...")
        return

    if destrutiva and carroca and arredores:
        while True:
            clear()
            print("Você olha os seus arredores, prestando bastante atenção, você percebe um movimento suspeito do homem. O que fara agora?")
            escolha: str = input("1 | questionar \n2 | atacar \n\n|| ")

            match escolha:
                case '1':
                    questionar=True
                    break
                case '2':
                    atacar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if destrutiva and carroca and arredores and atacar:
        while True:
            clear()
            print("Você ataca o homem suspeito, matando ele antes que ele possa te matar. Você agora está livre:")
            escolha: str = input("1 | seguir até a torre \n2 | esperar \n\n|| ")

            match escolha:
                case '1':
                    torre=True
                    break
                case '2':
                    esperar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")

    if destrutiva and carroca and arredores and atacar and torre:
        clear()
        print("Você vai até a torre quando você chega nela as suas vítimas aparecem na sua frente para se vingar. Você usa toda sua magia, mas não basta. Agora você está preso entre vida e a morte sendo um escravo para o rei demônio. Parabéns pelo pior final.")
        input("\nPressione Enter para continuar...")
        return
    
    if destrutiva and carroca and arredores and questionar:
        while True:
            clear()
            print("Você pergunta a ele o que ele pensa que está fazendo. Em um susto ele cai para trás e deixa a faca cair. Ele se ajoelha e começa a implorar por piedade:")
            escolha: str = input("1 | matar \n2 | não matar \n\n|| ")

            match escolha:
                case '1':
                    matar_homem=True
                    break
                case '2':
                    nao_matar_homem=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if destrutiva and carroca and arredores and questionar and matar_homem:
        clear()
        print("Você deixa o corpo dele em chamas e ele morre lentamente queimado. O problema é que isso chama atenção de um grupo de goblins. Você tenta usar suas magias para matar eles, mas têm muitos goblins. Parabéns, você morreu por ser muito cruel.")
        input("\nPressione Enter para continuar...")
        return
    
    if destrutiva and carroca and arredores and questionar and nao_matar_homem:
        while True:
            clear()
            print("Você decide não matar ele e o mandar embora. O homem vai indo correndo. Agora você ta livre pra continuar até a torre:")
            escolha: str = input("1 | seguir até a torre \n2 | esperar \n\n|| ")

            match escolha:
                case '1':
                    torre=True
                    break
                case '2':
                    esperar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if destrutiva and carroca and arredores and ((questionar and nao_matar_homem) or atacar) and esperar:
        clear()
        print("Por algum motivo que só Deus sabe, você decide esperar, afinal não faz mal dar uma pequena pausa depois de uma viagem, até que você é cercado por um grupo de goblins. Você tenta usar suas magias pra matar eles, mas têm muitos goblins. Parabéns, você morreu por preguiça.")
        input("\nPressione Enter para continuar...")
        return

    if destrutiva and carroca and arredores and questionar and nao_matar_homem and torre:
        while True:
            clear()
            print("Você segue até a torre, quando chega a porta não ta trancada. Você adentra e vê uma cena estranha, uma carnificina enorme havia acontecido, vários monstros estando mortos pelo chão. O que você fara agora?")
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
    
    if destrutiva and carroca and arredores and questionar and nao_matar_homem and torre and explorar:
        while True:
            clear()
            print("Não tem nada muito interessante de se encontrar nesse lugar além do sangue e corpos de monstros, mas você acha um cajado de gelo que é melhor que o seu atual. Agora você pode avançar. Você chega em duas portas. Uma delas é feita de lava enquanto a outra é feita de gelo:")
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
    
    if destrutiva and carroca and arredores and questionar and nao_matar_homem and torre and avancar:
        while True:
            clear()
            print("Sem querer perder tempo, você chega em duas portas. Uma delas é feita de lava enquanto a outra é feita de gelo:")
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
    
    if destrutiva and carroca and arredores and questionar and nao_matar_homem and torre and avancar and lava:
        clear()
        print("Você morre queimado tentando abrir uma porta sem o cajado certo. Parabéns, você morreu por ser muito fraco.")
        input("\nPressione Enter para continuar...")
        return
    
    if destrutiva and carroca and arredores and questionar and nao_matar_homem and torre and explorar and lava:
        clear()
        print("Você chega numa sala cheia de sangue e vários corpos de humanos e monstros, em cima deles dorme um dragão bem machucado, você percebe muito tarde que entrar numa sala com uma porta de fogo não seja uma boa ideia sem as magias corretas, no seu primeiro passo você cai no chão desmaiado e morre queimado, parabéns você morreu.")
        input("\nPressione Enter para continuar...")
        return

    if destrutiva and carroca and arredores and questionar and nao_matar_homem and torre and (explorar or avancar) and gelo:
        while True:
            clear()
            print("Você chega numa enorme biblioteca, parece que encontrou o que veio fazer aqui. Você encontra inúmeros tipos de magias interessantes. Você agora pode ir embora com todo esse conhecimento, ou ir ver o que tem na outra porta:")
            escolha: str = input("1 | ir embora \n2 | porta de lava \n\n|| ")

            match escolha:
                case '1':
                    ir_embora=True
                    break
                case '2':
                    lava=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if destrutiva and carroca and arredores and questionar and nao_matar_homem and torre and (explorar or avancar) and gelo and ir_embora:
        while True:
            clear()
            print("Depois de adquirir toda a coleção de itens mágicos e livros, você volta pra sua cidade e cria uma guilda de magia extremamente bem sucedida. Final feliz.")
            input("\nPressione Enter para continuar...")
            return
    
    if destrutiva and carroca and arredores and questionar and nao_matar_homem and torre and avancar and gelo and lava:
        while True:
            clear()
            print("Você tenta abrir a porta com tudo que você tem. Infelizmente você gasta toda sua energia tentando abrir a porta, e acaba desmaiando. Quando finalmente consegue, você acorda soterrado por escombros da torre, morrendo sangrando lentamente. Parabéns, você morreu.")
            input("\nPressione Enter para continuar...")
            return
    
    if destrutiva and carroca and arredores and questionar and nao_matar_homem and torre and explorar and gelo and lava:
        while True:
            clear()
            print("Você chega numa sala cheia de sangue e vários corpos de humanos e monstros. Em cima deles dorme um dragão bem machucado. Você pode acabar com ele ou só ir embora:")
            escolha: str = input("1 | matar o dragão \n2 | ir embora \n\n|| ")

            match escolha:
                case '1':
                    matar_dragao=True
                    break
                case '2':
                    ir_embora=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if destrutiva and carroca and arredores and questionar and nao_matar_homem and torre and explorar and gelo and lava and matar_dragao:
        clear()
        print("Parabéns, com todo os itens mágicos e novas magias que roubou do dragão você é capaz de matar ele sem nenhum problema nem ser pego por qualquer tipo de armadilha besta. Quando volta ao reino é tido como herói e vive até o fim de sua vida como nobre. Final feliz… para você.")
        input("\nPressione Enter para continuar...")
        return
    
    if destrutiva and carroca and arredores and questionar and nao_matar_homem and torre and explorar and gelo and lava and ir_embora:
        clear()
        print("Você vai embora, mas antes que  consiga sair da torre ela inteira treme e desaba, não é uma ideia muito boa destrancar um dragão sem matar ele. Agora você está morto preso pelos escombros com todo o conhecimento que você queria. Parabéns, final ruim… para você.")
        input("\nPressione Enter para continuar...")
        return
    
    if construtiva:
        while True:
            clear()
            print("Existem boatos de um dragão em um reino próximo que está causando muitos problemas. Você está indo em direção ao dito reino para ajudar os outros e talvez conseguir convencer o dragão a ir embora. Escolha sua forma de transporte:")
            escolha: str = input("1 | carroça \n2 | caminhada \n\n|| ")

            match escolha:
                case '1':
                    carroca=True
                    break
                case '2':
                    caminhada=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if construtiva and carroca:
        clear()
        print("Você acha um homem disposto a te levar até o reino. Durante a viagem você acaba dormindo e é esfaqueado enquanto dorme. Parabéns, você morreu e todos os seus pertences foram roubados. Não é uma boa ideia confiar cegamente num estranho quando você é tão indefeso.")
        input("\nPressione Enter para continuar...")
        return
    
    if construtiva and caminhada:
        while True:
            clear()
            print("Você decide ir caminhando, é um caminho mais longo porém pode ser melhor para você. Os animais são mais honestos e legais que as pessoas de qualquer forma. Durante sua caminhada você ouve algo.O que fará?")
            escolha: str = input("1 | investigar \n2 | seguir seu caminho \n\n|| ")

            match escolha:
                case '1':
                    investigar=True
                    break
                case '2':
                    seguir_caminho=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if construtiva and caminhada and seguir_caminho:
        clear()
        print("Você continua indo no seu caminho ignorando o barulho. Você chega na cidade. Infelizmente os goblins ali perto não são tão amigáveis a ponto de você conseguir conversar com eles e sem auxilio você é uma presa fácil, então não preciso nem dizer o que aconteceu com você. Parabéns, você morreu.")
        input("\nPressione Enter para continuar...")
        return
    
    if construtiva and caminhada and investigar:
        while True:
            clear()
            print("Indo até a origem do barulho você acha um filhote de urso com a pata presa, como você não é um monstro você ajuda ele e também cura o pobre filhote, porém a mãe logo chega. Você explica toda a situação e a mãe urso parece bem compreensiva. Ela te convida pra seguir ela:")
            escolha: str = input("1 | seguir a ursa \n2 | seguir seu caminho \n\n|| ")

            match escolha:
                case '1':
                    seguir_ursa=True
                    break
                case '2':
                    seguir_caminho=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if construtiva and caminhada and investigar and seguir_caminho:
        clear()
        print("Você continua seu caminho após se despedir da mãe urso e chega à cidade. Infelizmente os goblins ali perto não são tão amigáveis a ponto de você conseguir conversar com eles, e sem auxilio você é uma presa fácil, então não preciso nem dizer o que acontece com você. Parabéns, você morreu.")
        input("\nPressione Enter para continuar...")
        return
    
    if construtiva and caminhada and investigar and seguir_ursa:
        while True:
            clear()
            print("Ela te leva para a toca dela e te oferece algo pra comer. Você agradece, mas prefere não aceitar. Após ela falar com seu parceiro a ursa se junta a você para continuar sua aventura como um agradecimento por salvar seu filho. Vocês seguem até a torre juntos, vocês chegam na cidade, alguns goblins se afastam quando veêm você e a ursa ali e agora vocês podem escolher fazer algo:")
            escolha: str = input("1 | explorar a cidade \n2 | entrar na torre \n\n|| ")

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
    
    if construtiva and caminhada and investigar and seguir_ursa and cidade:
        clear()
        print("Você olha ao redor da cidade procurando por algo que possa ser útil na aventura dentro da torre. Pelos escombros da cidade você encontra algo brilhante, uma lança que perfurou seu olho e te mata antes que você possa reagir. A ursa te vinga mas nada pode ser feito sobre seu corpo. Parabéns, você morreu por não ter reação.")
        input("\nPressione Enter para continuar...")
        return
    
    if construtiva and caminhada and investigar and seguir_ursa and torre:
        while True:
            clear()
            print("Vocês entram dentro da torre, dentro dela existem vários monstros mortos, prece que alguém passou por aqui antes de vocês. O que fará?")
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
    
    if construtiva and caminhada and investigar and seguir_ursa and torre and avancar:
        clear()
        print("Você chega em um lugar com duas portas uma feita de lava e outra de gelo. Você não tem como abrir nenhuma delas pois não tem as magias necessárias nem mesmo a ursa consegue te ajudar nisso. Vocês então são obrigados a irem embora, pelo menos você salvou um filhote de urso. Final mediano.")
        input("\nPressione Enter para continuar...")
        return
    
    if construtiva and caminhada and investigar and seguir_ursa and torre and explorar:
        while True:
            clear()
            print("Você encontra um monstro ainda vivo usando um cajado de gelo. A ursa com sua ajuda consegue matar ele, e você pega o cajado para você. Não é o tipo de cajado que você usa mas pode servir pra outra pessoa, você segue na torre até que chega em duas portas uma de lava e outra de gelo. O que você faz?")
            escolha: str = input("1 | porta de gelo \n2 | porta de lava \n\n|| ")

            match escolha:
                case '1':
                    gelo=True
                    break
                case '2':
                    lava=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if construtiva and caminhada and investigar and seguir_ursa and torre and explorar and gelo:
        clear()
        print("Você encosta na porta de gelo e é congelado até a morte. Pelo menos você salvou um filhote de urso. Final mediano?")
        input("\nPressione Enter para continuar...")
        return
    
    if construtiva and caminhada and investigar and seguir_ursa and torre and explorar and lava:
        while True:
            clear()
            print("Você usa o cajado de gelo para abrir a porta, entrando você vê o dragão sobre uma montanha de corpos. Você vai até ele e conversam. Você acaba descobrindo que ele tinha sido preso ali pelo rei demônio, o real vilão dessa historia toda, e agora que ele está livre, o dragão está pronto para juntar a seus irmãos e ir contra o rei demônio. Você pode ajudar ele ou não:")
            escolha: str = input("1 | ajudar ele \n2 | não ajudar ele \n\n|| ")

            match escolha:
                case '1':
                    ajudar_dragaon=True
                    break
                case '2':
                    nao_ajudar_dragaon=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if construtiva and caminhada and investigar and seguir_ursa and torre and explorar and lava and ajudar_dragaon:
        clear()
        print("A ursa e você embarcam na jornada de ajudar o dragão. Final… não é um final. Continue na historia do dragão (digite “auxilio” ao entrar na historia do dragão)")
        input("\nPressione Enter para continuar...")
        return
    
    if construtiva and caminhada and investigar and seguir_ursa and torre and explorar and lava and nao_ajudar_dragaon:
        clear()
        print("O dragão te leva de volta pra sua cidade e vai indo até o castelo do rei demônio. Final apenas.")
        input("\nPressione Enter para continuar...")
        return