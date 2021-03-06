import os
import validar_CPF
import apartamentos

def Home():
    os.system('clear')
    print(f"\n {'-'*30} ")
    print(f"|{'BEM-VINDO AO HOTEL VEGAS'.center(30)}|")
    print(f" {'-'*30} \n")
    print(f"[ 1 ] - {'Reserva'.center(23)}|")
    print(f"[ 2 ] - {'Serviço de Quarto'.center(23)}|")
    print(f"[ 3 ] - {'Pagamento'.center(23)}|")
    print(f"[ 4 ] - {'Registros'.center(23)}|")
    print(f"[ 0 ] - {'Sair'.center(23)}|")
    print()
    
    op = str(input("Opção: "))

    if op == "1":
        Registrar_Reserva()
    elif op == "2":
        Servico_Quarto()
    elif op == "3":
        Pagamento()
    elif op == "4":
        Registros()
    elif op == "0":
        # Comandos para sair de um script
        exit()
    else:
        print("Opção errada!!!\nInforme a OPÇÃO correta...")
        return Home()

# 01
def Registrar_Reserva():
    # Dados(Nome, CPF, Categoria(Simples. Duplo, Casal, Luxo), opeck-in, opeck-out)
    os.system('clear')
    print("\nRESERVAR QUARTO\n")

    nome = str(input("Nome: "))
    cont = True
    while cont:
        str_cpf = str(input("CPF: "))
        validar = validar_CPF.Validar(str_cpf)
        if validar == False:
            print("CPF inválido!\n")
        else:
            cont = False
    telefone = str(input("Telefone Nº: "))
    check_in = str(input("Check-In: "))
    check_out = str(input("Check-Out: "))

def Consultar_Reserva():
    pass

def Registrar_Entrada():
    pass

def Registrar_Saida():
    pass

def Cadastrar_Hospede():
    pass

# 02
def Servico_Quarto():
    os.system('clear')
    print("-"*30)
    print("HOTEL VEGAS".center(30))
    print("-"*30)

# 03
def Pagamento():
    pass

# 04
def Registros():
    pass

Home()