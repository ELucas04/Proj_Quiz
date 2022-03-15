from time import sleep
delay = 0.7

def funcao():
    from time import sleep    
    l = ['-=' * 15]
    for i in l:
        print(i)
        sleep(delay)
        
def continuacao(cont):
    if cont == 'S':
        pass
    else:
        print("FIM!")
        quit()
    return cont    

def rules(r):
    erro = False
    while not erro:
        if r == '0':
            funcao()
            print("-O usuário irá escolher um tema de sua preferência, com isso, será feito algumas perguntas sobre o tema.")
            funcao()
            print("-Caso o usuário erre a resposta, terá 10 tentativas ao total.")
            funcao()
            print("-Se as tentativas se esgotarem e o usuário voltar a errar, o usuário perde.")
            funcao()
            print("Para passar de nível o usuário terá que acertar 70% das questões. Caso contrário terá de recomeçar.")
            erro = True
        else:
            sleep(delay)
            print("\033[1;31mDígito incorreto! Digite novamente.\033[0;0m")
            sleep(delay)
            regras = input("Digite '0' para ver as regras: ").strip()
            if regras == '0':
                funcao()
                print("-O usuário irá escolher um tema de sua preferência, com isso, será feito algumas perguntas sobre o tema.")
                funcao()
                print("-Caso o usuário erre a resposta, terá 10 tentativas ao total.")
                funcao()
                print("-Se as tentativas se esgotarem e o usuário voltar a errar, o usuário perde.")
                funcao()
                print("Para passar de nível o usuário terá que acertar 70% das questões. Caso contrário terá de recomeçar.")
                erro = True
