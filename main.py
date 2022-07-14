import os
import validar_CPF
import apartamentos
#str_cpf = str(input("CPF: "))
#print(validar_CPF.Validar(str_cpf))
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
    os.system('clear')
    print("\nRESERVAR QUARTO\n")

def Consultar_Reserva():
    pass

def Registrar_Entrada():
    pass

def Registrar_Saida():
    pass

def Cadastrar_Hospede():
    # Dados(Nome, CPF, Categoria(Simples. Duplo, Casal, Luxo), opeck-in, opeck-out)
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