import funcoes
import arquivo

'''Adicionar um contato com nome, telefone e e-mail.
Listar todos os contatos cadastrados.
Buscar um contato pelo nome.
Remover um contato.'''

lista_das_pessoas= "GERENCIADOR_DE_CONTATOS.TXT"

if arquivo.ArquivoExiste(lista_das_pessoas):
    print("Arquivo Encontrado")
else:
    print("Arquivo Não Encontrado!")
    arquivo.CriarArquivo(lista_das_pessoas)

while True:
    while True:
        funcoes.cabecalho("GERENCIADOR DE CONTATOS")
        print("\033[1m1 - Adicionar um contato")
        print("2 - Listar todos os contatos")
        print("3 - Buscar um contato pelo nome")
        print("4 - Remover um contato")
        print("5 - Sair\033[0m")

        escolha=(input("\033[0mEscolha: "))
        if escolha == "1":
            funcoes.cabecalho("ADICIONAR UM CONTATO")
            Nome=input("\033[0mDigite o Nome:").strip()
            Telefone=input("Digite seu Telefone:").strip()
            Email=input("Digite seu Email: ").strip()
            funcoes.adicionar(Nome,Telefone,Email)
        if escolha=="2": 
            funcoes.listar()
        if escolha=="3":
            buscar_nome=input("Digite o Nome:")
            print("")
            funcoes.buscar(buscar_nome)
            print("")
        if escolha=="4": #ERRO
            remover_nome=input("Digite o Nome para Remover: ")
            funcoes.remover(remover_nome)
        if escolha=="5":
            break
        else:
            print("\033[1m\033[31m~"*30)
            print("Escolha uma Opção Válida!")
            print("~"*30+"\033[0m")
    print("\033[1m\033[35mDeslogado do Gerenciador!\033[0m")
    break

            

#print(funcoes.pessoas.copy())
#funcoes.pessoas.pop("Murilo Souza de Barros")
#print(funcoes.pessoas)
#funcoes.adicionar
