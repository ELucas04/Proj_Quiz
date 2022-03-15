from time import sleep

acertos = 0
tentativas = 10
delay = 0.7

# (Fácil)
altF1 = '1) O jogador considerado o melhor de todos os tempos é: \na) Diego Maradona \nb) Lionel Messi \nc) Cristiano Ronaldo \nd) Pelé'
altF2 = '2) Qual é a seleção mais antiga? \na) Inglesa \nb) Holandesa \nc) Brasileira \nd) Belga'
altF3 = '3) O time com mais títulos da Copa Libertadores é: \na) Independiente \nb) Boca Juniors \nc) Flamengo \nd) Peñarol'
altF4 = '4) Seleção campeã da copa de 2014: \na) Holanda \nb) Brasil \nc) Alemanha \nd) Argentina'
altF5 = '5) O prêmio Puskás de 2021 foi para: \na) Igor Gomes (São Paulo)\nb) Patrick Shick (Bayer Leverkusen)\nc) Erik Lamela (Tottenham)\nd) Mehdi Taremi (Porto)'
altF6 = '6) Qual é o atual técnico do Liverpool: \na) Hans Dieter Flick\nb) Jurgen Klopp\nc) Steven Gerrard\nd) Julian Nagelsmann'
altF7 = '7) Time com mais campeonatos brasileiros na era dos pontos corridos: \na) Corinthians\nb) Cruzeiro\nc) Flamengo\nd) São Paulo'
altF8 = '8) Qual o time com mais vice-campeonatos da Copa do Brasil?\na) Flamengo\nb) Atlético Mineiro\nc) São Paulo\nd) Grêmio'

# (Médio)
altM_F1 = '1) Em 1981, consagrava-se campeão da Copa Intercontinental: \na) Liverpool (ING)\nb) Santos (BR)\nc) Peñarol (URU)\nd) Flamengo (BR)'
altM_F2 = '2) Qual o artilheiro da Neo Química Arena (Arena Corinthians)?\na) Paolo Guerrero\nb) Ángel Romero\nc) Jadson\nd) Jô'
altM_F3 = '3) Qual a maior goleada de 2020?\na) Bayern München vs Barcelona\nb) Ajax vs VVV-Venlo\nc) Manchester United vs Southampton\nd) Liverpool vs Aston Villa'
altM_F4 = '4) Campeão da Liga dos Campeões 2004:\na) Porto\nb) Milan\nc) Mônaco\nd) Barcelona'
altM_F5 = '5) Primeiro campeão brasileiro (1971): \na) Atlético Mineiro\nb) São Paulo\nc) Palmeiras\nd) Fluminense'
altM_F6 = '6) Qual dos times brasileiros, nunca perdeu para o Real Madrid: \na)São Paulo \nb) Vasco\nc) Botafogo\nd) Santos'
altM_F7 = '7) Por qual desses times o jogador Diego Souza não jogou: \na) Metalist\nb) Fluminense\nc) Corinthians\nd) Benfica'
altM_F8 = '8) Time com mais vice-campeonatos da Liga dos Campeões: \na) Milan (ITA)\nb) Benfica (POR)\nc) Bayern München (GER)\n d)Juventus (ITA)'

# (Difícil)
altD_F1 = '1) Qual jogador nunca punido com um cartão amarelo?\na) Andrés Iniesta\nb) Philipp Lahm\nc) Michel Platini\nd) Gary Lineker'
altD_F2 = '2) Campeão mundial de 1993 e 1994, respectivamente:\na) Milan e São Paulo\nb) Barcelona e Olympique de Marseille\nc) São Paulo e Vélez Sarsfield\nd) Vélez Sarsfield e Ajax'
altD_F3 = '3) Local onde ocorreu a final da Copa do mundo de 1970:\na) Cidade do México, México\nb) Munique, Alemanha\nc) Ñuñoa, Chile\nd) Wembley, Inglaterra'
altD_F4 = '4) Jogador premiado com a bola de ouro em 1996:\na) Zinédine Zidane\nb) Romário\nc) Matthias Sammer\nd) Marco van Basten'
altD_F5 = "5) Qual o maior público em um jogo da Copa Libertadores: \na) Cruz Azul x River Plate\nb) America-MEX x Boca Juniors\nc) São Paulo x Newell's Old Boys\nd) Cruz Azul x Rosário Central"
altD_F6 = '6) Há 21 anos(2001), (...) ganhava seu primeiro campeonato brasileiro: \na) Criciúma\n b) Botafogo\n c)Athletico Paranaense\n d) Juventude'
altD_F7 = '7) Primeiro campeão brasileiro de forma invicta: \na) Palmeiras\nb) Santos\nc) Fluminense\n d) Cruzeiro'
altD_F8 = '8) Estádio onde foi sediado a final da Copa dos Campeões 2000: \na) Mineirão \nb) Rei Pelé\nc) Pacaembu\nd) Nilton Santos'

perguntas_dict = {altF1: 'D', altF2: 'A', altF3: 'A', altF4: 'C', altF5: 'C', altF6: 'B', altF7: 'A', altF8: 'D'}

perguntasM_dict = {altM_F1: 'B', altM_F2: 'D', altM_F3: 'B', altM_F4: 'A', altM_F5: 'A', altM_F6: 'A', altM_F7: 'C', altM_F8: 'D'}

perguntasD_dict = {altD_F1: 'D', altD_F2: 'C', altD_F3: 'A', altD_F4: 'C', altD_F5: 'A', altD_F6: 'C', altD_F7: 'A', altD_F8: 'B',}

def perguntas_fut1(F1):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(F1)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntas_dict[F1]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntas_fut2(F2):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(F2)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntas_dict[F2]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntas_fut3(F3):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(F3)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntas_dict[F3]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntas_fut4(F4):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(F4)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntas_dict[F4]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntas_fut5(F5):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(F5)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntas_dict[F5]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntas_fut6(F6):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(F6)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntas_dict[F6]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntas_fut7(F7):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(F7)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntas_dict[F7]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntas_fut8(F8):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(F8)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntas_dict[F8]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break            

def perguntasM_Fut1(M_F1):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(M_F1)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntasM_dict[M_F1]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntasM_Fut2(M_F2):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(M_F2)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntasM_dict[M_F2]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntasM_Fut3(M_F3):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(M_F3)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntasM_dict[M_F3]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntasM_Fut4(M_F4):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(M_F4)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntasM_dict[M_F4]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntasM_Fut5(M_F5):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(M_F5)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntasM_dict[M_F5]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntasM_Fut6(M_F6):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(M_F6)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntasM_dict[M_F6]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntasM_Fut7(M_F7):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(M_F7)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntasM_dict[M_F7]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntasM_Fut8(M_F8):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(M_F8)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntasM_dict[M_F8]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntasD_Fut1(D_F1):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(D_F1)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntasD_dict[D_F1]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntasD_Fut2(D_F2):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(D_F2)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntasD_dict[D_F2]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntasD_Fut3(D_F3):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(D_F3)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntasD_dict[D_F3]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntasD_Fut4(D_F4):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(D_F4)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntasD_dict[D_F4]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntasD_Fut5(D_F5):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(D_F5)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntasD_dict[D_F5]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break

def perguntasD_Fut6(D_F6):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(D_F6)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntasD_dict[D_F6]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break            

def perguntasD_Fut7(D_F7):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(D_F7)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntasD_dict[D_F7]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break  

def perguntasD_Fut8(D_F8):
    global tentativas, acertos
    if not tentativas:
        tentativas = 10
    while True:
        print(D_F8)
        sleep(delay)
        escolha = input('\nQual a alternativa correta? ').upper().strip()
        if escolha == perguntasD_dict[D_F8]:
            sleep(delay)
            print('\033[1;32mResposta correta.\033[1;97m')
            acertos += 1
            break
        else:
            sleep(delay)
            print('\033[1;31mResposta incorreta.\033[1;97m')
            while True:
                if tentativas:
                    sleep(delay)
                    dnv = input(
                        f'\nQuer tentar novamente? Isso custará uma tentativa (Suas tentativas: {tentativas}) [S/N] ').strip().upper()
                    if dnv not in 'SN':
                        sleep(delay)
                        print('\033[1;31mNão é uma opção.\033[1;97m')
                        continue
                    else:
                        break
                else:
                    sleep(delay)
                    print('\033[1;31mSuas tentativas esgotaram.\033[1;97m')
                    sleep(delay)
                    quit()
            if dnv == 'S':
                tentativas -= 1
                continue
            else:
                break                      