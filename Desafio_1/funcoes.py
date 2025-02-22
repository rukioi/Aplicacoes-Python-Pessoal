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

pessoas = dict()

def buscar(Nome):
    "Digite o nome da pessoa que você deseja buscar para receber todos os dados da pessoa!"
    validacao=0
    for i,v in pessoas.items():
        if Nome in v:
            validacao=1
            print(f"Nome: {v[0]}")
            print(f"Telefone: {v[1]}")
            print(f"E-mail: {v[2]}")
    if validacao==0:
        print(f'Não encontramos "{Nome}" no nosso Sistema!')



def adicionar(Nome="Não Informado",Telefone="Não Informado",Email="Não Informado"):
    contato= list()

    contato.append(Nome)
    contato.append(Telefone)
    contato.append(Email)
    
    pessoas[f'Pessoa {len(pessoas)+1}']=contato
    
adicionar("Murilo Souza de Barros","79991463940","muribeco@hotmail.com")
adicionar("Maria Bragantina Silva","79999816647","mariabraga@gmail.com")
adicionar("José de Augusto Carvalho","79325916647","josecarv@gmail.com")

def listar():
    print(Negrito+"-"*70+Reset)
    print(Negrito+Ciano+"Lista de Pessoas".center(70)+Reset)
    print(Negrito+"-"*70+Reset)

    for pessoa, dados in pessoas.items():
        print(f"{dados[0].ljust(30)}{dados[1].ljust(18)}{dados[2].ljust(15)}")


#listar()
buscar("Murilo Souza de Barros")
#Problemas em Tirar saída, Tava com a ideia de Fazer somente um Dicionário e pegar do dicionário, sem precisar fazer essa lista contatos
#validar_nomes#()