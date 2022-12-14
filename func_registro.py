import datetime

def mostrarAnimal(animal):
    return ( "Nome: "+animal['nome']+" | Idade: "+str(animal['idade'])+
             " | Porte: "+animal['porte']+" | Raça: "+animal['raca']+" | Lar Temporário: "+animal['lar'] )
#---------------------------------------------------------------------


def ordernarIdade(lista): # inserir lista de dicionários, não lista de strings
    return sorted(lista, key=lambda a: a['idade'], reverse=True)
#---------------------------------------------------------------------

def lerNaoAdotados():
    try: 
        arq = open("registro_naoadotados.txt", "r") # modo leitura
        velhalista_registro = arq.readlines()
    except: return [] # caso o arquivo não exista
    
    # converter strings pra dicts
    novalista_registro = []
    for linha in velhalista_registro:
        dic = eval(linha.removesuffix("\n")) # transformar string em dicionário
        novalista_registro.append(dic)
    arq.close()
    return novalista_registro
#---------------------------------------------------------------------

def lerAdotados(): 
    try:
        arq = open("registro_adotados.txt", "r") # modo leitura
        velhalista_registro = arq.readlines()
    except: return [] # caso arquivo não exista

    # converter strings pra dicts
    novalista_registro = []
    for linha in velhalista_registro:
        dic = eval(linha.removesuffix("\n")) # transformar string em dicionário
        novalista_registro.append(dic)
    arq.close()
    return novalista_registro
#---------------------------------------------------------------------

def salvarNaoAdotados(lista):
    arq = open("registro_naoadotados.txt", "w")
    for dic in lista:
        arq.write(str(dic)+"\n")
    arq.close()
#---------------------------------------------------------------------

def regMoverAnimalAdotado(animal, dono, data):
    # animal é o dicionario, dono é string, data é datatime
    lista_naoadotados = lerNaoAdotados()
    lista_naoadotados.remove(animal)
    salvarNaoAdotados(lista_naoadotados)

    animal['dono'] = dono
    animal['data'] = data

    arq = open("registro_adotados.txt", "a")
    arq.write(str(animal)+"\n")
    arq.close()

#---------------------------------------------------------------------

def regAdicionar(): # adiciona um novo animal à lista dos não adotados
    print("--Novo Animal--")
    
    nome = input("Digite o nome do animal: ")
    
    while True:
        try: 
            idade = int(input("Digite a idade do animal (número inteiro): ").strip())
            break
        except: print("digite um número inteiro")
    
    while True:
        porte = input("Digite o porte do animal (pequeno, medio, grande): ").lower().strip()
        if ( porte == "pequeno" or porte == "medio" or porte == "grande"):
            break
        else: print("digite um porte válido")

    raca = input("Digite a raça do animal: ")
    lar = input("Digite o lar temporário do animal: ")
    entrada = {"nome": nome, "idade": idade, "porte": porte, "raca": raca, "lar": lar}

    arq = open("registro_naoadotados.txt", "a") # modo adicionar linha
    arq.write(str(entrada)+"\n")

    arq.close()
    print("Animal adicionado ao registro!")
#---------------------------------------------------------------------

def regModificar():
    novalista_registro = lerNaoAdotados()
    #print(novalista_registro) # debug

    # mostrar a lista de animais
    print("--Registro--")
    for i in range(len(novalista_registro)):
        # i + 1 para fazer os índices começando em 0 parecerem começar com 1
        print(str(i+1) + ' - ' + mostrarAnimal(novalista_registro[i]))
        print("-------")
    
    if len(novalista_registro) == 0:
        print("O registro está vazio.")
    else:
        # escolher o animal
        id = 0
        while True:
            id = -1
            try: 
                id = int(input("Digite o ID do animal para modificar: ")) - 1 # pra usar index 0 denovo
            except: id = -1
            
            # o usuário só pode escolher números entre 0 e tamanho-1
            if id not in range(len(novalista_registro)):
                print("id inválido, tente novamente")
            else:
                break # sair se o ID existe na lista

        # escolher a operação
        while True:
            mostrarAnimal(novalista_registro[id])
            print("O que deseja modificar?")
            operacao = input("(nome, idade, porte, raca, lar, remover, salvar): ").lower().strip()
            
            if operacao == "nome":
                nome = input("Digite o novo nome: ")
                novalista_registro[id]['nome'] = nome
                print("Operação realizada com sucesso!")
            
            elif operacao == "idade":
                while True:
                    try: 
                        idade = int(input("Digite a nova idade (número inteiro): ").strip())
                        break
                    except: print("digite um número inteiro")
                novalista_registro[id]['idade'] = idade
                print("Operação realizada com sucesso!")
            
            elif operacao == "porte":
                while True:
                    porte = input("Digite o novo porte (pequeno, medio, grande): ").lower().strip()
                    if ( porte == "pequeno" or porte == "medio" or porte == "grande"):
                        break
                    else: print("digite um porte válido")
                novalista_registro[id]['porte'] = porte
                print("Operação realizada com sucesso!")
            
            elif operacao == "raca":
                raca = input("Digite a nova raça: ")
                novalista_registro[id]['raca'] = raca
                print("Operação realizada com sucesso!")
            
            elif operacao == "lar":
                lar = input("Digite o novo lar: ")
                novalista_registro[id]['lar'] = lar
                print("Operação realizada com sucesso!")
            
            elif operacao == "remover":
                print("Tem certeza que deseja remover esse animal do registro?")
                inp = ""
                while True:
                    inp = input("(sim/nao): ").lower()
                    if inp == "nao": break
                    elif inp == "sim":
                        novalista_registro.pop(id)
                        salvarNaoAdotados(novalista_registro)
                        print("Animal removido com sucesso!\nRegistro Salvo com sucesso!")
                        break
                if inp == "sim": break # sair das operações
            
            elif operacao == "salvar":
                salvarNaoAdotados(novalista_registro)
                print("Registro Salvo com sucesso!")
                break
        
    # fim
#---------------------------------------------------------------------

