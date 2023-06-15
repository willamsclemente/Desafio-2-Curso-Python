def saque (saldo, valor, extrato, limite, numero_saques, limite_saque):
        
    if valor > saldo:
        print("Operação falhou: Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou: O valor do saque excedeu o limite.")
    elif numero_saques >= limite_saque:
        print("Operação falhou: Número de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou: Valor informado é inválido.")

    return (saldo, extrato)

def deposito(valor, saldo, extrato):
    if valor > 0:
        saldo+= valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou:o valor informado é inválido.")

    return (saldo, extrato)

def exibir_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========\n")
    print("\nNão foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("\n=============================")

def criar_usuario(usuarios):
    cpf = int(input("Digite o CPF do novo usuário (Somente números): "))

    for usuario in usuarios:
        if cpf ==  (usuario["cpf"]):
            print("Usuário já cadastrado")
            return (usuarios)

    novo_usuario = {"nome":"", "data_de_nascimento": "", "endereço" : "", "cpf": cpf}
    nome = (input("Digite o nome do usuario: "))
    novo_usuario["nome"] = nome
    dtNasc = (input("Digite a data de nascimento do usuário (No formato DD-MM-YYYY): "))
    novo_usuario["data_de_nascimento"] = dtNasc
    endereco = (input("Digite o endereço do usuário (logradouro, bairro - cidade/sigla  estado): "))
    usuarios.append(novo_usuario)
    print(usuarios)
    print ("Usuário cadastrado!!")
    return (usuarios)

def criar_conta(usuarios, contas, agencia, numero_contas):
    cpf = int(input("Digite o CPF do usuário (Somente números): "))
    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            print("Conta cadastrada!!")
            nova_conta = {"numero":numero_contas, "agencia": agencia, "usuario": usuario}
            numero_contas += 1
            contas.append(nova_conta)
            return (contas, numero_contas)
           
    print("Usuário ainda não está cadastrado!!")
    return (contas, numero_contas)

def listar_contas(contas):
    print ("============== Contas ===============\n")
    for conta in contas:
        numero = conta["numero"]
        agencia = conta["agencia"]
        usuario = conta["usuario"]["nome"]
        print (f"Usuário: {usuario} Conta: {numero} Agencia: {agencia}")
    



def main():
    menu = """

    =========== MENU =============

    [d] \tDepositar
    [s] \tSacar
    [e] \tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q] \tSair

    => """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    numero_contas = 1

    while True:

        opcao = input(menu)

        if opcao == 'd':
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = deposito (valor, saldo, extrato)


        elif opcao == 's':
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = saque (
                saldo = saldo,
                valor = valor, 
                extrato = extrato, 
                limite = limite,
                numero_saques = numero_saques,
                limite_saque = LIMITE_SAQUE
            )
        
        
        elif opcao == 'e':
            exibir_extrato(saldo, extrato)

        elif opcao == 'nu':
            usuarios = criar_usuario(usuarios)

        elif opcao == 'nc':
            contas, numero_contas = criar_conta(usuarios, contas, AGENCIA, numero_contas)

        elif opcao == 'lc':
            listar_contas(contas)
        
        elif opcao == 'q':
            break

        else:
            print("Operação inválida: Por favor selecione novamente a operação desejada.")

main()
