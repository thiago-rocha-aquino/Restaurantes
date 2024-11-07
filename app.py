import os
rest = [{"nome":"Praça","categoria":"Japonesa", "ativo":False}, 
        {"nome":"Pizza Superma", "categoria":"Pizza", "ativo":True}] # restaurantes
def exibir_nome_programa(): #nome do app
   print("    🇸​​​​​🇦​​​​​🇧​​​​​🇴​​​​​🇷​​​​​ 🇪​​​​​🇽​​​​​🇵​​​​​🇷​​​​​🇪​​​​​🇸​​​​​🇸​​​​\n​")

def nome_opcoes():  #opções para o usuario escolher
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. alterar estado do restaurante restaurante")
    print("4. Sair\n")

def finalizar(): # opção 4, para finalizar
    exibir_subtitulo("finalizando app\n")
    

def opcao_inv(): # caso o usuario digite acima de 4 ou uma string
    print("opção inválida!\n")

    voltar_menu()

def exibir_subtitulo(texto): # exibe os titulos
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_rest(): # opção 1 para cadastar clientes
    exibir_subtitulo("cadastro de novos restaurantes\n")
    nome_res = input("digite o nome do restaurante que deseja cadastrar: \n ")
    categoria = input(f"digite a categoria do restaurante {nome_res}:")
    dados_res = {"nome":nome_res, "categoria":categoria, "ativo":False}
    rest.append(dados_res)
    print(f"o restaurante {nome_res} foi cadastrado!\n")

    voltar_menu()


def listar_rest(): # opção 2 para ver os restaurantes já listados no app
    exibir_subtitulo("Listando Restaurantes\n")
    print(f"{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status")
    #print(f" - {"Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | Status") erro sintaxe
    for res in rest:
       nome_res = res["nome"]
       categoria = res["categoria"]
       ativo = "ativado"if res["ativo"] else "desativado"
       print(f" - {nome_res.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    voltar_menu()   

def alterar_estado():# alterar estado do restaurante true(ativado) ou false(desativado)
    exibir_subtitulo("alterando status")
    nome_rest = input("digite o nome do restaurante que deseja alterar o estado: ")
    rest_encontrado = False
    for res in rest:
        if nome_rest == res["nome"]:
            rest_encontrado = True
            res ["ativo"] = not res ["ativo"]
            mensagem = f"O restaurante {nome_rest} foi ativado com sucesso" if res["ativo"] else f"O restaurante {nome_rest} foi desativado com sucesso"
            print(mensagem)
    if not rest_encontrado:
        print("o restaurante não foi encontrado")        

    voltar_menu()

def escolher_opcoes(): # funcionalidade das opções para o usuario escolher
    try:  
        opcao = int(input("digite uma opção: "))

        if ( opcao == 1):
            cadastrar_rest()
        elif(opcao == 2):
            listar_rest()
        elif( opcao == 3):
            alterar_estado()
        elif ( opcao == 4):
            finalizar()    
        else:
            opcao_inv()
    except: 
        opcao_inv() 

def  voltar_menu(): #funcionalidade para voltar para o menu
          input("digite uma tecla para voltar ao menu principal: ")
          main()
    
def main():
    os.system("cls")
    exibir_nome_programa()
    nome_opcoes()
    escolher_opcoes()

if __name__ == "__main__":
    main()
