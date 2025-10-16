from auxiliar.clear import clear

def caminho_dragao() -> None:

    #variáveis booleanas para evitar muitos alinhamentos de if dentro de outros if o que deixaria muito dificil a construção da história
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

    exterminar:bool=False
    continuar:bool=False

    ir_direto:bool=False
    explorar:bool=False

    enfrentar_cerberus:bool=False
    sacrificar:bool=False
    domesticar:bool=False

    enfrentar_rei_demonio:bool=False

    #todas as ramificações começam logo abaixo. os nomes das váriaveis usados nas estruturas IF indica quais ações foram tomadas para alcançar esse ponto da história, por tanto não há necessiadade de comentar cada um deles
    clear()
    nome:str=input("Escolha o seu nome: ")
    if nome.lower() == "auxilio":
        auxilio=True
    
    if not(auxilio):
        while True:
            clear()
            print("Você é um dragão qualquer. Você estava vivendo uma vida tranquila na sua caverna em sua pilha de tesouros até vê um homem chegando na entrada da caverna:")
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
            print("Você pergunta o que ele estava buscando. O homem não responde e tenta te atacar, porém ele é apenas um homem, nada que ele faz consegue te machucar. O que você faz?")
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
            print("Você pergunta denovo. Ele continua sem responder até ele se cansar de te atacar sem parar e cair no chão. Ele fala que estava em busca do seu tesouro, mas que não esperava que você fosse tão resistente. O que fara com ele?")
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
        print("Você decide matar o homem, verdadeiramente um tolo por tentar enfrentar um dragão sozinho. Você volta a dormir, porém seu sono é interrompido por um grande exército, você luta valorosamente contra eles porém eles te pegaram em um lugar onde a vantagem é deles. Parabéns, você morreu.")
        input("\nPressione Enter para continuar...")
        return
    
    if questionar_homem and questionar_homem_novamente and mandar_homem_embora:
        while True:
            clear()
            print("Você manda ele embora, não ha nescessidade de matar um ser tão fraco assim. Ele foge assim que você ordena. O que fará?")
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
        print("Você volta ao seu sono de beleza. Infelizmente durante seu sono você é atacado, não por um único homem, mas sim por um enorme exército preparado para te eliminar. Sua morte é brutal, parabéns.")
        input("\nPressione Enter para continuar...")
        return
    
    if questionar_homem and questionar_homem_novamente and mandar_homem_embora and seguir_homem:
        while True:
            clear()
            print("Você espera um pouco depois dele sair para o seguir e encontra um enorme exército do lado de fora da sua caverna com todos os tipos de armas. Eles vieram para te matar. O que fara?")
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
        print("Você não quer lidar com todo esse problema honestamente é muito cansativo então você só pega a parte da montanha com sua caverna e vai para outro lugar onde você possa viver em paz. Final vida tranquila.")
        input("\nPressione Enter para continuar...")
        return
    
    if questionar_homem and questionar_homem_novamente and mandar_homem_embora and seguir_homem and dominar:
        clear()
        print("Você decide que ira fazer eles se arrependerem disso. Você devasta o exército e logo em seguida vai até o reino de onde estes soldados haviam vindo. Você facilmente mata e se torna o novo rei instaurando uma ditadura onde todos sofrem. Final dominador.")
        input("\nPressione Enter para continuar...")
        return
    
    if questionar_homem and questionar_homem_novamente and mandar_homem_embora and seguir_homem and destruir:
        clear()
        print("Você sem piedade alguma mata todos do exército. Mesmo estando preparados eles não esperavam te enfrentar assim. Você consegue matar todos, mas somente isso não é o bastante para apaziguar sua furia. Você decide destruir o reino de onde eles haviam vindo e qualquer outro resquicio de civilização que encontra no seu caminho, você é a tormenta. Final destrutivo.")
        input("\nPressione Enter para continuar...")
        return
    
    if auxilio:
        while True:
            clear()
            print("Você é o rei dragão, o mais poderoso dentre todos os dragões. Há muito tempo atrás quando você ainda era jovem você enfrentou o rei demônio ele infelizmente venceu contra você e te aprisionou em um limbo, porém sua força cresceu demais. Ele teve que te colocar numa torre em alguma cidade aleatória, e foi aprisionado lá. Se algum mago surgisse ele poderia usar das magias guardadas para lhe matar, felizmente o mago que lhe encontrou não era um desses. Ele decidiu conversar, diferente dos outros soldados que haviam entrado anteriormente. Graças a ele você foi verdadeiramente libertado, agora mais poderoso que nunca é hora de enfrentar o rei demônio, com um auxilio, você aproveita pra entregar para o mago todo conhecimento magico que você poderia entregar a um mortal para ele poder te ajudar verdadeiramente na luta e também usou sua magia para aprimorar a ursa. Com os dois nas suas costas você voou até o castelo do rei demônio. Como entrara na torre?")
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
    
    if auxilio and parede:
        clear()
        print("Não tem motivo pra atravessar o castelo inteiro. Vocês vão direto na sala do rei demônio, infelizmente não é um confronto simples. Diversos monstros e demônios se juntam a luta incluindo um cerberus. Vocês não tem como enfrentar isso tudo. Parabéns, vocês morreram brutalmente.")
        input("\nPressione Enter para continuar...")
        return
    
    if auxilio and porta_frente:
        while True:
            clear()
            print("Você chega na frente do castelo e abre o portão da frente destruindo ele com um simples rugido. Diversos monstros e demônios tentam atacar você, mas nada que eles fazem consegue te machucar. O que fará?")
            escolha: str = input("1 | exterminar \n2 | continuar \n\n|| ")

            match escolha:
                case '1':
                    exterminar=True
                    break
                case '2':
                    continuar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if auxilio and porta_frente and continuar:
        clear()
        print("Vocês avançam ignorando todos os monstros até que chegam em um cerberus. Com todos os monstros juntos infelizmente não tem o que possa ser feito. Vocês conseguem matar todos os monstros e o cerberus, mas mesmo com toda sua força, você mal sobrevive e seus amigos morrem. Você nem tem uma chance de fugir antes do rei demônio chegar e te matar. Parabéns, você morreu.")
        input("\nPressione Enter para continuar...")
        return
    
    if auxilio and porta_frente and exterminar:
        while True:
            clear()
            print("Para defender seus colegas, você extermina os monstros ali com pouca dificuldade. Vocês podem continuar sem problemas. Qual rota irá tomar?")
            escolha: str = input("1 | ir direto \n2 | explorar \n\n|| ")

            match escolha:
                case '1':
                    ir_direto=True
                    break
                case '2':
                    explorar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if auxilio and porta_frente and exterminar and explorar:
        while True:
            clear()
            print("Vocês exploram um pouco do castelo antes de seguir e encontram uma enorme carne. Não se sabe o que podem fazer com isso, mas pode ser útil. Vocês podem logo seguir até a sala do rei demônio, porém tem um cerberus na frente. O que fará?")
            escolha: str = input("1 | enfrentar \n2 | sacrificar \n3 | domesticar \n\n|| ")

            match escolha:
                case '1':
                    enfrentar_cerberus=True
                    break
                case '2':
                    sacrificar=True
                    break
                case '3':
                    domesticar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if auxilio and porta_frente and exterminar and explorar and domesticar:
        clear()
        print("O mago dá a ideia de domesticar o cerberus, você segue com essa ideia maluca, que de algum jeito funciona. Ele se junta a vocês, graças a isso vocês podem enfrentar o rei demônio com mais um aliado. Vocês entram dentro da sala do rei demônio e enfrentam ele com muita dificuldade, porém graças ao cerberus vocês conseguem matar ele sem ninguém morrer. Melhor final, o rei demônio perdeu.")
        input("\nPressione Enter para continuar...")
        return
    
    if auxilio and porta_frente and exterminar and ir_direto:
        while True:
            clear()
            print("Você ignora qualquer outro tipo de distração que possa surgir e vai reto em direção a sala do rei demônio. No caminho você encontra um ser do seu tamanho, um enorme cerberus. Existem dois jeitos de passar:")
            escolha: str = input("1 | enfrentar \n2 | sacrificar \n\n|| ")

            match escolha:
                case '1':
                    enfrentar_cerberus=True
                    break
                case '2':
                    sacrificar=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if auxilio and porta_frente and exterminar and (ir_direto or explorar) and sacrificar:
        clear()
        print("Alguém tem que impedir o cerberus de atrapalhar a luta e apenas você tem alguma chance contra o rei demônio. Você deixa seus amigos ali e dá a volta, deixando eles para o enfrentarem e passa pela parede entrando na sala do rei demônio. Você enfrenta o rei demônio com muita dificuldade, ele ainda é mais poderoso que você e quase te mata, porém seus amigos não te abandonarão como você. O cerberus junto do mago e da ursa entram no salão e todos se juntam a luta. Com todos unidos, vocês conseguem matar o rei demônio, mas você acaba morrendo. Final feliz, o rei demônio foi morto.")
        input("\nPressione Enter para continuar...")
        return
    
    if auxilio and porta_frente and exterminar and (ir_direto or explorar) and enfrentar_cerberus:
        while True:
            clear()
            print("Alguém tem que impedir o cerberus de atrapalhar a luta e não tem como seguir sem matar ele, você fica e manda o urso e o mago para resolverem a situação do rei demônio. Você enfrenta o cerberus com dificuldade, afinal você ainda está se recuperando do seu aprisionamento. Você consegue matar o cerberus, mas está bem machucado. O que fará?")
            escolha: str = input("1 | fugir \n2 | enfrentar rei demônio \n\n|| ")

            match escolha:
                case '1':
                    fugir=True
                    break
                case '2':
                    enfrentar_rei_demonio=True
                    break
                case _:
                    print("Opção inválida! Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    if auxilio and porta_frente and exterminar and (ir_direto or explorar) and enfrentar_cerberus and enfrentar_rei_demonio:
        clear()
        print("Não é hora de deixar seus amigos pra morrer. Você entra dentro da sala no último momento possível um segundo antes do mago ser morto. Você combate o rei demônio, porém graças a seus ferimentos você não consegue mata-lo. Ele te mata, logo em seguida ele termina de matar o mago e a ursa. Final horrível, o rei demônio venceu.")
        input("\nPressione Enter para continuar...")
        return
    
    if auxilio and porta_frente and exterminar and (ir_direto or explorar) and enfrentar_cerberus and fugir:
        clear()
        print("Não faz sentido entrar em uma luta que você sabe que vai perder. Infelizmente seus amigos vão morrer. Você tenta fugir, no momento em que sai do castelo, uma maldição se ativa em você e por estar tão fraco não consegue aguentar caindo e morrendo lentamente. Pior final, o rei demônio venceu e vai usar sua carcaça como vassalo.")
        input("\nPressione Enter para continuar...")
        return