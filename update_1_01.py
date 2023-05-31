def buscar_candidatos(notas_busca, lista_candidatos):#funcao buscar candidatos 
    candidatos_encontrados = []
    for candidato in lista_candidatos:
        notas_candidato = candidato['notas']
        if all(nota_candidato >= nota_busca for nota_candidato, nota_busca in zip(notas_candidato, notas_busca)):
            candidatos_encontrados.append(candidato)# na linha acima defini que : somente se todas notas atenderem aos criterios de busca deve retornar candidatos encontrados
    return candidatos_encontrados

def adicionar_candidato(lista_candidatos):# esta e a funcao que adiciona candidatos 
    nome = input("Digite o nome do candidato: ")
    notas = []
    for i in range(4):
        nota_valida = False
        while not nota_valida:
            if i == 0:
                nota = input("Digite sua nota para Entrevista (Somente números inteiros entre 1 e 100): ")
            elif i == 1:
                nota = input("Digite sua nota para Teste Teórico (Somente números inteiros entre 1 e 100): ")
            elif i == 2:
                nota = input("Digite sua nota para Teste Prático (Somente números inteiros entre 1 e 100): ")
            else:
                nota = input("Digite sua nota para Soft Skills (Somente números inteiros entre 1 e 100): ")

            if nota.isdigit() and 1 <= int(nota) <= 100: # Aqui neste local defini que a nota seria valor entre 1 e 100
                notas.append(int(nota)) #defini tambem acima que o valor inputado pelo usuario deve ser digito
                nota_valida = True
            else:
                print("Valor inválido. Digite um número entre 1 e 10.")

    candidato = {"nome": nome, "notas": notas}#defini aqui a variavel candidato que recebe o nome e as notas como parametros caracteristicas
    lista_candidatos.append(candidato)#comando que adiciona candidato no dicionario lista candidatos
    print("Candidato adicionado com sucesso!")

# Exemplo de uso
lista_candidatos = [
    {"nome": "RPhael", "notas": [9, 9, 9, 9]},
    {"nome": "William", "notas": [9, 9, 9, 9]},
    {"nome": "Jseph", "notas": [8, 8, 9, 6]},
    {"nome": "Vicka", "notas": [9, 6, 9, 6]},
    {"nome": "ThC", "notas": [5, 5, 5, 0]},
    {"nome": "Luck", "notas": [7, 8, 9, 9]},
    {"nome": "Feibs", "notas": [7, 8, 9, 6]},
    {"nome": "Jacq", "notas": [7, 6, 5, 5]},
    {"nome": "Edineutron", "notas": [3, 4, 5, 3]},
    {"nome": "Maria", "notas": [6, 7, 8, 9]},
    {"nome": "Cristh", "notas": [10, 10, 10, 10]},
    {"nome": "YHVH", "notas": [100, 100, 100, 100]}#candidato teste
]

opcao = "0"# menu principal loop principal diferente de tres continua executando
while opcao != "3":
    print(" \n Opções:")# com o barra n pulo uma linha pra ficar legal a apresentacao no terminal
    print("1 - Realizar uma pesquisa")
    print("2 - Inserir um candidato")
    print("3 - Sair do programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":#opcao 1 do menu principal
        notas_busca = []
        for i in range(4):
            nota_valida = False
            while not nota_valida:
                if i == 0:
                    nota = input("Digite sua nota para Entrevista (Somente números inteiros entre 1 e 100): ")
                elif i == 1:
                    nota = input("Digite sua nota para Teste Teórico (Somente números inteiros entre 1 e 100): ")
                elif i == 2:
                    nota = input("Digite sua nota para Teste Prático (Somente números inteiros entre 1 e 100): ")
                else:
                    nota = input("Digite sua nota para Soft Skills (Somente números inteiros entre 1 e 100): ")

                if nota.isdigit() and 1 <= int(nota) <= 100:# esse comando vrf se a nota digitada foi digito de um a 100
                    notas_busca.append(int(nota))
                    nota_valida = True
                else:
                    print("Valor inválido. Digite um número entre 1 e 10.")

        candidatos_encontrados = buscar_candidatos(notas_busca, lista_candidatos)

        if len(candidatos_encontrados) > 0:
            print("Candidatos encontrados:")
            for candidato in candidatos_encontrados:
                nome = candidato['nome']
                notas_candidato = candidato['notas']
                notas_formatadas = "_".join(f"{letra}{nota}" for letra, nota in zip(['e', 't', 'p', 's'], notas_candidato))
                print(f"{nome} {notas_formatadas}")
        else:
            print("Nenhum candidato encontrado com as notas especificadas.")

    elif opcao == "2":
        adicionar_candidato(lista_candidatos)

    elif opcao == "3":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Digite novamente.")
