def funcao_principal():
    from time import sleep
    import Regras
    import Perguntas
    delay = Perguntas.delay
    Regras.funcao()
    sleep(delay)
    print("Olá usuário(a). Bem vindo(a) ao QUIZ.")
    Regras.funcao()
    continuar = input("Deseja continuar? [S/N] ").strip().upper()[0]
    sleep(delay)
    Regras.continuacao(continuar)
    Regras.funcao()
    reg = (input("Digite '0' para ver as regras: ")).strip()
    Regras.rules(reg)
    Regras.funcao()
    print(f'\n\033[1;94m{"NÍVEL 1!":^30}\033[1;97m')
    Perguntas.perguntas_fut1(Perguntas.altF1)
    Perguntas.perguntas_fut2(Perguntas.altF2)
    Perguntas.perguntas_fut3(Perguntas.altF3)
    Perguntas.perguntas_fut4(Perguntas.altF4)
    Perguntas.perguntas_fut5(Perguntas.altF5)
    Perguntas.perguntas_fut6(Perguntas.altF6)
    Perguntas.perguntas_fut7(Perguntas.altF7)
    Perguntas.perguntas_fut8(Perguntas.altF8)
    print(f'\nTotal de acertos: {Perguntas.acertos}\n')
    sleep(delay)
    if Perguntas.acertos >= 5:
        print(f'\n\033[1;94m{"NÍVEL 2!":^30}\033[1;97m')
        Perguntas.perguntasM_Fut1(Perguntas.altM_F1)
        Perguntas.perguntasM_Fut2(Perguntas.altM_F2)
        Perguntas.perguntasM_Fut3(Perguntas.altM_F3)
        Perguntas.perguntasM_Fut4(Perguntas.altM_F4)
        Perguntas.perguntasM_Fut5(Perguntas.altM_F5)
        Perguntas.perguntasM_Fut6(Perguntas.altM_F6)
        Perguntas.perguntasM_Fut7(Perguntas.altM_F7)
        Perguntas.perguntasM_Fut8(Perguntas.altM_F8)
        print(f'\nTotal de acertos: {Perguntas.acertos}\n')
        sleep(delay)
    else:
         print("Que pena... parece que você não acertou o número MÍNIMO de questões para passar de nível.")
    if Perguntas.acertos >= 11:
        print(f'\n\033[1;94m{"NÍVEL 3!":^30}\033[1;97m')
        Perguntas.perguntasD_Fut1(Perguntas.altD_F1)
        Perguntas.perguntasD_Fut2(Perguntas.altD_F2)
        Perguntas.perguntasD_Fut3(Perguntas.altD_F3)
        Perguntas.perguntasD_Fut4(Perguntas.altD_F4)
        Perguntas.perguntasD_Fut5(Perguntas.altD_F5)
        Perguntas.perguntasD_Fut6(Perguntas.altD_F6)
        Perguntas.perguntasD_Fut7(Perguntas.altD_F7)
        Perguntas.perguntasD_Fut8(Perguntas.altD_F8)
        print(f'\nTotal de acertos: {Perguntas.acertos}\n')
        sleep(delay)
    if Perguntas.acertos == 24:
        print(f"\nPARABÉNS usuário, você acertou {Perguntas.acertos} de 24 questões e leva \033[1;33mOURO\033[1;97m")
    elif Perguntas.acertos >= 20:
        print(f"\nPARABÉNS usuário, você acertou {Perguntas.acertos} de 24 questões e leva \033[1;37mPRATA\033[1;97m")
    elif Perguntas.acertos >= 16:
        print(f"\nPARABÉNS usuário, você acertou {Perguntas.acertos} de 24 questões e leva \033[1;91mBRONZE\033[1;97m")
    else:
        print(f"\nVocê acertou {Perguntas.acertos} de 24.")
funcao_principal()