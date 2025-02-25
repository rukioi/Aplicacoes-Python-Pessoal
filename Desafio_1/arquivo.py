import funcoes

def ArquivoExiste(arquivo):
    try:
        a=open(arquivo,"rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def CriarArquivo(arquivo):
    try:
        a= open(arquivo,"wt+")
        a.close
    except:
        print("Erro na Criação do Arquivo!")
    else:
        print(f"Arquivo '{arquivo}' Criado Com Sucesso")

def LerArquivo(arquivo):
    try:
        a=open(arquivo,"rt")
    except:
        print("Erro ao ler o arquivo")
    else:
        funcoes.cabecalho("Pessoas Cadastradas")
        print(a.readlines())
    finally:
        a.close()

def cadastrar(arquivo,Nome="Desconhecido",Telefone="Desconhecido",Email="Desconhecido"):
    try:
        a=open(arquivo,"at")
    except:
        print("Houve um Erro ao abrir o arquivo!")
    else:
        try:
            a.write()
        except:
            print("Houve um erro na hora de escrever os dados")
        else:  
            print(f"Novo Registro de {Nome} Adicionado")
            a.close()
        

