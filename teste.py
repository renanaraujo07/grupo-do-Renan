import time

# Isso serve para mostrar olá mundo

"""
Este é um comentário
não sei o que colocar
kkk
"""

tempo = 2
print("Seja bem-vindo")
nome = input("Digite seu nome: ")

print("Bem-vindo,", nome + "!")

time.sleep(tempo)

print("Em que posso te ajudar?")

def menu():
    # Correção de indentação aqui
    print("1- Consultar mensalidade")
    print("2- Consultar diária")
    print("3- Consultar promoções")
    print("4- Cancelar vínculo")

    opcao = int(input("Digite o número da opção desejada: "))

    time.sleep(tempo)

    # Esta é uma parte importante do código
    """ Como ele faz parte do menu, tem que seguir a indentação """

    if opcao == 1:
        print("R$ 200,00")
    elif opcao == 2:
        print("R$ 30,00")
    elif opcao == 3:
        print("Promo de inauguração, 10 meses por R$ 1000,00")
    elif opcao == 4:
        print("Vínculo cancelado, sob multa de R$ 50,00")
        
        #sempre tentar ser detalhista para que o usuário entenda qual o erro
    else:
        print("Erro: opção inválida")

menu()
