'''🔹 Desafio 1: Gerenciador de Contatos (Básico)
📌 Habilidades: Manipulação de listas e dicionários, entrada e saída de dados.

Crie um programa que permita ao usuário:

Adicionar um contato com nome, telefone e e-mail.
Listar todos os contatos cadastrados.
Buscar um contato pelo nome.
Remover um contato.'''

#Códigos ANSI
Preto= "\033[30m"
Vermelho= "\033[31m"
Verde="\033[32m"
Amarelo="\033[33m"
Azul="\033[34m"
Roxo="\033[35m"
Ciano="\033[36m"
Branco="\033[37m"
Negrito="\033[1m"
Reset="\033[0m"

contatos= []


def cabecalho(texto=None):
    if texto is None or texto.strip(): #Validação da função
        print(Negrito+Vermelho+" !ERROR! Você Esqueceu de Passar Argumento!"+ Reset)
    else:
        print(Negrito+"-"*35) #Código cabeçalho 
        print(Ciano + texto.center(35) + Reset)
        print(Negrito+"-"*35 + Reset)
    
def adicionar(Nome="Não Informado",Telefone="Não Informado",Email="Não Informado"):
    contato= list()
    pessoa= dict()

    contato.append(Nome)
    contato.append(Telefone)
    contato.append(Email)
    
    pessoa[f'Pessoa {len(contatos)+1}']=contato

    contatos.append(pessoa)

def listar():
    for i in contatos:
        print(f"Nome: {i}")

adicionar("Murilo","79991463940","MURIBECO@HOTMAIL.COM")
adicionar("Maria","79999816647","maria@gmail.com")

listar()
print(contatos)

#Problemas em Tirar saída, Tava com a ideia de Fazer somente um Dicionário e pegar do dicionário, sem precisar fazer essa lista contatos