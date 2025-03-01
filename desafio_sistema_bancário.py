menu = '''
    Bem-vindo ao Banco do Desenvolvedor!
    Escolha uma das opções abaixo:

    1 - Depositar Valor
    2 - Sacar Valor
    3 - Consultar Extrato
    4 - Encerrar Operação
'''

# Variáveis globais do sistema bancário
saldo = 7000  # Armazena o saldo da conta
extrato = []  # Lista para registrar as operações (depósitos e saques)
numero_de_saques = 0  # Contador de saques realizados no dia
LIMITE_DE_SAQUES = 3  # Limite máximo de saques diários
LIMITE_POR_SAQUE = 500  # Limite máximo por saque

# Laço de repetição principal para exibir o menu e processar as opções
while True:  # Loop infinito até o usuário escolher a opção de encerrar
    opcao = input(menu)  # Exibe o menu e captura a escolha do usuário

    if opcao == "1":  # Opção para depósito
        valor = int(input("Informe o valor de depósito:\n"))  # Solicita o valor do depósito

        # Verifica se o valor é positivo usando expressão ternária para mensagem
        print("Depósito realizado com sucesso!" if valor > 0 else "Operação falhou! Valor inválido.")
        
        if valor > 0:  # Se o valor for válido, atualiza o saldo e registra no extrato
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")  # Adiciona o depósito ao extrato

    elif opcao == "2":  # Opção para saque
        valor = int(input("Informe o valor do saque: "))  # Solicita o valor do saque

        # Condições locais para validação do saque
        excedeu_saldo = valor > saldo  # Verifica se o valor excede o saldo disponível
        excedeu_limite = valor > LIMITE_POR_SAQUE  # Verifica se o valor excede o limite por saque
        excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES  # Verifica se o limite de saques foi atingido

        # Mensagens de erro para cada condição usando expressões ternárias
        print("Falha na operação! Você não tem saldo suficiente.\n" if excedeu_saldo else "")
        print("Falha na operação! O valor do saque excede o limite de saque único.\n" if excedeu_limite else "")
        print("Falha na operação! Número máximo de saque diário excedido.\n" if excedeu_saques else "")

        if not (excedeu_saldo or excedeu_limite or excedeu_saques):  # Se todas as condições forem satisfeitas
            if valor > 0:  # Verifica se o valor é positivo
                saldo -= valor  # Deduz o valor do saldo
                extrato.append(f"Saque: R$ {valor:.2f}")  # Registra o saque no extrato
                numero_de_saques += 1  # Incrementa o contador de saques
                print("\nSaque realizado! Recolha seu dinheiro.\n")
            else:
                print("Falha na operação! O valor informado é inválido.\n")

    elif opcao == "3":  # Opção para consultar o extrato
        print("\n=============== EXTRATO ===============\n")
        # Usa expressão ternária para verificar se há movimentações no extrato
        print("Não foram realizadas movimentações.\n" if not extrato else "\n".join(extrato))
        print(f"\nSaldo: R$ {saldo:.2f}")  # Exibe o saldo formatado
        print("\n=======================================\n")

    elif opcao == "4":  # Opção para encerrar o programa
        print("Encerrando operação. Obrigado por usar o Banco do Desenvolvedor!")
        break  # Sai do loop e encerra o programa

    else:  # Caso o usuário insira uma opção inválida
        print("Opção inválida! Tente novamente.")  # Exibe mensagem de erro