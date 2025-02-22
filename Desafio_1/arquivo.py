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