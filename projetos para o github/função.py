estoque = {}
import json

def salvar_estoque():
    with open('estoque.json', 'w') as arquivo:
        json.dump(estoque, arquivo, indent=4)

'''
Função para salvar o estoque em um arquivo JSON.
A Função é chamada quando o programa é finalizado.
param estoque.json: arquivo onde é salvo o estoque
param w: modo de abertura do arquivo (w = write)

'''

def carregar_estoque():
    global estoque
    try:
        with open('estoque.json', 'r') as arquivo:
            estoque = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo de estoque não encontrado. Um novo arquivo será criado.')
        estoque = {}
'''
Função para carregar o estoque de um arquivo JSON.
A função é chamada quando o programa é iniciado.
param estoque.json: arquivo de onde é carregado o estoque
param r: modo de abertura do arquivo (r = read)
'''
        
def add_item(item, qtd):
    if item in estoque:
        estoque[item] += qtd
        print(f'{qtd} {item} adicionado ao estoque')    
    else:
        estoque[item] = qtd
        print(f'{item} adicionado ao estoque')
'''
Função para adicionar um item ao dicionario estoque.
A função verifica se o item já existe no estoque.
Se o item já existe, a quantidade é atualizada.
Se o item não existe, ele é adicionado ao estoque.
param item: nome do produto a ser adicionado
param qtd: quantidade do produto que vai ser adicionado
'''

def remove_item(item, qtd):
    if item in estoque:
        if qtd <= 0:
            print('Erro: A quantidade deve ser maior que zero')
        estoque[item] -= qtd
        if estoque[item] == 0:
            del estoque[item]
            print(f'{item} removido do estoque')
'''
Função para remover um item do estoque
A função verifica se o item existe no estoque
Caso exista, a quantidade é removida
Caso a quantidade chegue a zero, o item é removido do estoque
param item: nome do produto que será removido
param qtd: quantidade do produto que vai ser removido
'''


def visualizar_estoque():
    if estoque:
        print('--- Estoque Atual ---: ')
        for item,qtd in estoque.items():
            print(f' Nome: {item}  \n  qtd: {qtd}')
        print('---------------------')
    else:
        print('Estoque vazio')
'''
Função para visualizar os itens do estoque
A função verifica se o estoque está vazio
Caso não esteja vazio, imprime os itens e suas quantidades
Caso esteja vazio, imprime que o estoque está vazio
'''

    
def item_existe(item):
    return item in estoque
'''
A função verifica se o item existe no estoque
param item: nome do produto que será verificado
return: True se o item existe, False caso contrário
'''
    




