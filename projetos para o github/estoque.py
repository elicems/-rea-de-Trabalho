import função
opc = 0
função.carregar_estoque() 

while True:
    print('--- Menu ---')
    print('1 - Adicionar item')
    print('2 - Remover item')
    print('3 - Ver estoque')
    print('4 - Sair')
    print('------------')

    opc = int(input('Escolha uma opção: '))

    if opc == 1:
        while True:
            item = str(input('Digite o nome do item que deseja adicionar: ')).strip().lower()
            try:
                qtd = int(input('Digite a quantidade a ser adicionada: '))
                if qtd > 0:
                    função.add_item(item,qtd)
                else: 
                    print('Quantidade inválida')
            except ValueError:
                print('Valor inválido. Digite um número inteiro.')
            cont = str(input('Deseja adicionar mais itens? (s/n): ')).strip().lower()
            if cont == 'n':
                break
            elif cont != 's':
                print('Opção inválida.')
                break

    elif opc == 2:
        item = str(input('Digite o item a ser removido do estoque: ')).strip().lower()
        if função.item_existe(item):
            try:
                qtd = int(input('Digite a quantidade a ser removida: '))
                if qtd > 0:
                    função.remove_item(item,qtd)
                else: 
                    print('Quantidade inválida')
            except ValueError:
                print('Valor inválido. Por favor digite um número inteiro.')
        else: 
            print(f'{item} não encontrado no estoque')
    
    elif opc == 3:
        função.visualizar_estoque()

    elif opc == 4:
        print('Encerrando programa...')
        função.salvar_estoque()
        break
    else:
        print('Opção inválida. Tente novamente.')
    print()
        



        