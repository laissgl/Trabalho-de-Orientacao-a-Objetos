from cliente import Cliente
from funcionario import Funcionario
from restaurante import Restaurante
from produto import Produto
from pagamento import Pagamento
from pedido import Pedido
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_restaurantes_padrao():
    r1 = Restaurante("Pizzaria", "Fratello Uno")
    r1.adicionar_item(Produto("Pizza Margherita", 75.00))
    r1.adicionar_item(Produto("Pizza Calabresa", 80.00))
    r1.adicionar_item(Produto("Refrigerante", 6.00))

    r2 = Restaurante("Cafeteria", "Studio Grão")
    r2.adicionar_item(Produto("Toast Presunto de Parma", 32.00))
    r2.adicionar_item(Produto("Brownie", 24.00))
    r2.adicionar_item(Produto("Café Gelado", 17.00))

    r3 = Restaurante("Japonesa", "Gurume")
    r3.adicionar_item(Produto("Combo Sushi 20 peças", 90.00))
    r3.adicionar_item(Produto("Temaki Salmão", 30.00))
    r3.adicionar_item(Produto("Água com gás", 5.00))

    r4 = Restaurante("Italiana", "Babbo")
    r4.adicionar_item(Produto("Gnocchi de Abóbora", 75.00))
    r4.adicionar_item(Produto("Lasanha de Filé", 70.00))
    r4.adicionar_item(Produto("Suco Natural", 9.00))

    return [r1, r2, r3, r4]


def submenu_restaurantes(restaurantes):
    while True:
        print("\n----- RESTAURANTES E CARDÁPIOS -----")
        print("[1] Ver os restaurantes e seus cardápios")
        print("[0] Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        clear()

        if opcao == "1":
            print("\n----- LISTA COMPLETA DE RESTAURANTES E CARDÁPIOS -----")
            for r in restaurantes:
                print(f"\n🍽️  {r.nome} ({r.categoria})")
                print("-" * (len(r.nome) + len(r.categoria) + 6))
                for item in r.cardapio:
                    print(f"• {item.nome} - R${item.preco:.2f}")
            print("\n-------------------------------------------")

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def perguntar_clube():
    while True:
        resposta = input("É membro do clube? (Sim/Não): ").strip().lower()
        if resposta in ["sim", "s", "SIM", "Sim"]:
            return True
        elif resposta in ["não", "nao", "n", "NÃO", "Não", "Nao"]:
            return False
        else:
            print("Resposta inválida! Digite 'Sim' ou 'Não'.")


def submenu_clientes(clientes):
    while True:
        print("\n----- CADASTRO DE CLIENTES -----")
        print("[1] Cadastrar novo cliente")
        print("[2] Listar clientes cadastrados")
        print("[0] Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        clear()

        if opcao == "1":
            while True:
                nome = input("Digite o nome do cliente: ")
                if any(char.isdigit() for char in nome):
                    print("Nome inválido! Não pode conter números. Tente novamente.")
                elif nome.strip() == "":
                    print("Nome não pode ser vazio. Tente novamente.")
                else:
                    break

            while True:
                cpf = input("Digite o CPF: ")
                cpf_limpo = cpf.replace(".", "").replace("-", "").replace(" ", "")
                
                if not cpf_limpo.isdigit():
                    print("CPF inválido! Não pode conter letras. Tente novamente.")
                elif len(cpf_limpo) < 11 or len(cpf_limpo) > 14:
                    print("CPF inválido! Deve conter entre 11 e 14 dígitos. Tente novamente.")
                else:
                    break

            while True:
                numero = input("Digite o número de telefone: ")
                numero_limpo = numero.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
                
                if not numero_limpo.isdigit():
                    print("Número inválido! Não pode conter letras ou caracteres especiais. Tente novamente.")
                elif len(numero_limpo) < 9 or len(numero_limpo) > 15:
                    print("Número inválido! Deve conter entre 9 e 15 dígitos. Tente novamente.")
                else:
                    break

            clube = perguntar_clube()
            cliente = Cliente(nome, cpf, numero, clube)
            clientes.append(cliente)
            print(f"\nCliente {nome} cadastrado com sucesso!")

        elif opcao == "2":
            if not clientes:
                print("\nNenhum cliente cadastrado ainda.")
            else:
                print("\n--- CLIENTES ---")
                for c in clientes:
                    print(f"- {c}")

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")


def submenu_funcionarios(funcionarios):
    while True:
        print("\n----- CADASTRO DE FUNCIONÁRIOS -----")
        print("[1] Cadastrar novo funcionário")
        print("[2] Listar funcionários cadastrados")
        print("[0] Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        clear()

        if opcao == "1":
            while True:
                nome = input("Digite o nome: ")
                if any(char.isdigit() for char in nome):
                    print("Nome inválido! Não pode conter números. Tente novamente.")
                elif nome.strip() == "":
                    print("Nome não pode ser vazio. Tente novamente.")
                else:
                    break

            while True:
                cpf = input("Digite o CPF: ")
                cpf_limpo = cpf.replace(".", "").replace("-", "").replace(" ", "")
                
                if not cpf_limpo.isdigit():
                    print("CPF inválido! Não pode conter letras. Tente novamente.")
                elif len(cpf_limpo) < 11 or len(cpf_limpo) > 14:
                    print("CPF inválido! Deve conter entre 11 e 14 dígitos. Tente novamente.")
                else:
                    break

            while True:
                numero = input("Digite o número de telefone: ")
                numero_limpo = numero.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
                
                if not numero_limpo.isdigit():
                    print("Número inválido! Não pode conter letras ou caracteres especiais. Tente novamente.")
                elif len(numero_limpo) < 9 or len(numero_limpo) > 15:
                    print("Número inválido! Deve conter entre 9 e 15 dígitos. Tente novamente.")
                else:
                    break

            while True:
                cargo = input("Digite o cargo: ").strip()
                if cargo == "":
                    print("Cargo não pode ser vazio. Tente novamente.")
                elif any(char.isdigit() for char in cargo):
                    print("Cargo inválido! Não pode conter números. Tente novamente.")
                else:
                    break

            while True:
                salario_str = input("Digite o salário: R$")
                try:
                    salario = float(salario_str.replace(",", "."))
                    if salario < 0:
                        print("Salário não pode ser negativo. Tente novamente.")
                        continue
                    break
                except ValueError:
                    print("Valor inválido para salário. Tente novamente.")

            funcionario = Funcionario(nome, cpf, numero, cargo, salario)
            funcionarios.append(funcionario)
            print(f"\nFuncionário {nome} cadastrado com sucesso!")

        elif opcao == "2":
            if not funcionarios:
                print("Nenhum funcionário cadastrado ainda.")
            else:
                print("\n----- FUNCIONÁRIOS -----")
                for f in funcionarios:
                    print(f"- {f}")

        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def submenu_pedidos(clientes, restaurantes):
    clear()
    if not clientes:
        print("\nNenhum cliente cadastrado! Cadastre-se antes de fazer um pedido.")
        return


    print("\n----- CLIENTES CADASTRADOS -----")
    for i, c in enumerate(clientes, 1):
        print(f"{i}. {c}")

    try:
        indice_cliente = int(input("Escolha o cliente: ")) - 1
        cliente_escolhido = clientes[indice_cliente]
    except (ValueError, IndexError):
        print("Escolha inválida.")
        return
    

    print("\n----- RESTAURANTES DISPONÍVEIS -----")
    for i, r in enumerate(restaurantes, 1):
        print(f"{i}. {r}")

    try:
        indice_restaurante = int(input("Escolha o restaurante: ")) - 1
        restaurante_escolhido = restaurantes[indice_restaurante]
    except (ValueError, IndexError):
        print("Escolha inválida.")
        return

    pedido = Pedido(cliente_escolhido, restaurante_escolhido)

    clear()

    while True:
        restaurante_escolhido.mostrar_cardapio()
        try:
            escolha = int(input("Escolha o número do produto (0 para finalizar): "))
        except ValueError:
            print("Entrada inválida! Digite um número.")
            continue

        if escolha == 0:
            break

        item = restaurante_escolhido.escolher_item_por_numero(escolha)
        if item:
            pedido.adicionar_item(item)
            print(f"Item '{item.nome}' adicionado ao pedido.")
        else:
            print("Número inválido.")

    if not pedido.itens:
        print("Pedido vazio! Nenhum item selecionado.")
        return

    clear()


    if cliente_escolhido.clube:
        for item in pedido.itens:
            item.preco *= 0.9
        print("\nDesconto de 10% aplicado para cliente do clube!")
    
    
    while True:
        tipo_pagamento = input("\nForma de pagamento (Pix ou Cartão): ").strip().lower()
        if tipo_pagamento in ["pix", "cartao", "cartão"]:
            break
        print("\nPagamento inválido! Digite 'Pix' ou 'Cartão'.")
            
    pagamento = Pagamento(pedido.itens, tipo_pagamento)
    pedido.pagamento = pagamento
    
    clear()

    print("\n----- RESUMO DO PEDIDO -----")
    print(f"Cliente: {cliente_escolhido.nome}\n")

    print(f"🍽️  Restaurante: {restaurante_escolhido.nome}")
    print("Itens do pedido:")

    for item in pedido.itens:
        print(f"• {item.nome} - R${item.preco:.2f}")

    print("\n💳 Detalhes do pagamento:")
    print(pagamento)
    print("\nObrigado por escolher nosso sistema de restaurante! Volte sempre!")


    input("\nPressione Enter para voltar ao menu principal")



def main():
    restaurantes = criar_restaurantes_padrao()
    clientes = []
    funcionarios = []

    while True:
        print("\n----- SISTEMA DE RESTAURANTE -----")
        print("[1] Restaurantes e Cardápios")
        print("[2] Cadastro de Clientes")
        print("[3] Cadastro de Funcionários")
        print("[4] Fazer Pedido")
        print("[0] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            submenu_restaurantes(restaurantes)
        elif opcao == "2":
            submenu_clientes(clientes)
        elif opcao == "3":
            submenu_funcionarios(funcionarios)
        elif opcao == "4":
            submenu_pedidos(clientes, restaurantes)
        elif opcao == "0":
            print("Encerrando o sistema. Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()