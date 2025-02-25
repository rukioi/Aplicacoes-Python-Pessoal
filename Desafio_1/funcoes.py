'''🔹 Desafio 1: Gerenciador de Contatos (Básico)
📌 Habilidades: Manipulação de listas e dicionários, entrada e saída de dados.

Crie um programa que permita ao usuário:

Adicionar um contato com nome, telefone e e-mail.
Listar todos os contatos cadastrados.
Buscar um contato pelo nome.
Remover um contato.'''
import arquivo

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

def cabecalho(arg):
    print(Negrito+"-"*len(arg))
    print(Ciano+arg.center(len(arg))+Reset)
    print(Negrito+"-"*len(arg)+Reset)


def adicionar(Nome="Não Informado",Telefone="Não Informado",Email="Não Informado"):
    contato= [Nome,Telefone,Email]
    
    pessoas[f'Pessoa {len(pessoas)+1}']=contato

    try:
        with open("GERENCIADOR_DE_CONTATOS.TXT", "a") as arquivo_contatos:
            arquivo_contatos.write(f"{Nome};{Telefone};{Email}\n")
        print(f"\033[32mContato '{Nome}' adicionado com sucesso!\033[0m") 
    except Exception as erro:
        print(f"\033[31mErro ao salvar o contato: {erro}\033[0m")
    
def listar():
    print(Negrito+"-"*70+Reset)
    print(Negrito+Ciano+"Lista de Contatos".center(70)+Reset)
    print(Negrito+"-"*70+Reset)

    try:
        with open("GERENCIADOR_DE_CONTATOS.TXT", "r") as arquivo_contatos:
            linhas = arquivo_contatos.readlines()

        if not linhas:  
            print(Negrito+Verde+"NENHUM CONTATO ADICIONADO!"+Reset)
        else:
            for linha in linhas:
                dados = linha.strip().split(";") 
                print(f"{dados[0].ljust(30)} {dados[1].ljust(18)} {dados[2].ljust(15)}")

    except FileNotFoundError:
        print(Negrito+Vermelho+"ERRO: O arquivo de contatos não foi encontrado."+Reset)
    except Exception as erro:
        print(Negrito+Vermelho+f"ERRO AO LER O ARQUIVO: {erro}"+Reset)

    print(Negrito+"-"*70+Reset)

def buscar(Nome):
    """
    Digite o nome da pessoa que você deseja buscar para receber todos os dados dela.
    """
    encontrado = False
    try:
        with open("GERENCIADOR_DE_CONTATOS.TXT", "r") as arquivo_contatos:
            linhas = arquivo_contatos.readlines()

        for linha in linhas:
            dados = linha.strip().split(";")
            if Nome.lower() in dados[0].lower(): 
                encontrado = True
                cabecalho("CONTATO ENCONTRADO!")
                print(f"{Negrito}{Amarelo}Nome: {dados[0]}")
                print(f"Telefone: {dados[1]}")
                print(f"E-mail: {dados[2]}{Reset}")
                print(Negrito+"-"*40+Reset)

        if not encontrado:
            print(f"\033[31mContato '{Nome}' não encontrado no sistema.\033[0m") 

    except FileNotFoundError:
        print("\033[31mERRO: O arquivo de contatos não foi encontrado.\033[0m")
    except Exception as erro:
        print(f"\033[31mERRO AO LER O ARQUIVO: {erro}\033[0m")

def remover(nome_da_pessoa):
    encontrado = False
    nova_lista = []
    try:
        with open("GERENCIADOR_DE_CONTATOS.TXT", "r") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            dados = linha.strip().split(";")
            if nome_da_pessoa.lower() == dados[0].lower():  
                encontrado = True
                continue  
            nova_lista.append(linha) 

        if encontrado:
            with open("GERENCIADOR_DE_CONTATOS.TXT", "w") as arquivo:
                arquivo.writelines(nova_lista)  
            print(f"\033[32mContato '{nome_da_pessoa}' removido com sucesso!\033[0m")
        else:
            print(f"\033[31mContato '{nome_da_pessoa}' não encontrado no sistema.\033[0m")

    except FileNotFoundError:
        print("\033[31mERRO: O arquivo de contatos não foi encontrado.\033[0m")
    except Exception as erro:
        print(f"\033[31mERRO AO REMOVER CONTATO: {erro}\033[0m")




#adicionar("Murilo Souza de Barros","79991463940","muribeco@hotmail.com")
#adicionar("Maria Bragantina Silva","79999816647","mariabraga@gmail.com")
#adicionar("José de Augusto Carvalho","79325916647","josecarv@gmail.com")



#listar()
#remover("Murilo Souza de Barros")
#validar_nomes#()
#listar()

#Estava dando erro pois fiz o código para funcionar sem "banco de dados" agora está funcionando com o "banco de dados" txt