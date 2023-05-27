def buscar_candidatos(notas_busca, lista_candidatos):
    candidatos_encontrados = []
    for candidato in lista_candidatos:
        notas_candidato = candidato['notas']
        if all(nota_candidato >= nota_busca for nota_candidato, nota_busca in zip(notas_candidato, notas_busca)):
            candidatos_encontrados.append(candidato)
    return candidatos_encontrados

def adicionar_candidato(lista_candidatos):
    nome = input("Digite o nome do candidato: ")
    notas = []
    for i in range(4):
        nota_valida = False
        while not nota_valida:
            if i == 0:
                nota = input("Digite sua nota para Entrevista (Somente números inteiros entre 1 e 10): ")
            elif i == 1:
                nota = input("Digite sua nota para Teste Teórico (Somente números inteiros entre 1 e 10): ")
            elif i == 2:
                nota = input("Digite sua nota para Teste Prático (Somente números inteiros entre 1 e 10): ")
            else:
                nota = input("Digite sua nota para Soft Skills (Somente números inteiros entre 1 e 10): ")

            if nota.isdigit() and 1 <= int(nota) <= 10:
                notas.append(int(nota))
                nota_valida = True
            else:
                print("Valor inválido. Digite um número entre 1 e 10.")

    candidato = {"nome": nome, "notas": notas}
    lista_candidatos.append(candidato)
    print("Candidato adicionado com sucesso!")

# Exemplo de uso
lista_candidatos = [
    {"nome": "RPhael", "notas": [10, 10, 10, 10]},
    {"nome": "William", "notas": [10, 10, 9, 10]},
    {"nome": "Jseph", "notas": [8, 8, 9, 6]},
    {"nome": "Vic", "notas": [9, 6, 9, 6]},
    {"nome": "Thiago", "notas": [5, 5, 5, 0]},
    {"nome": "Luck", "notas": [7, 8, 9, 9]},
    {"nome": "Feibs", "notas": [7, 8, 9, 6]},
    {"nome": "Jac", "notas": [7, 6, 5, 5]},
    {"nome": "Edineutron", "notas": [3, 4, 5, 3]},
    {"nome": "Maria", "notas": [6, 7, 8, 9]},
    {"nome": "Pedro", "notas": [8, 7, 6, 9]},
    {"nome": "Ana", "notas": [7, 6, 8, 9]}
]

opcao = "0"
while opcao != "3":
    print(" \n Opções:")
    print("1 - Realizar uma pesquisa")
    print("2 - Inserir um candidato")
    print("3 - Sair do programa")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        notas_busca = []
        for i in range(4):
            nota_valida = False
            while not nota_valida:
                if i == 0:
                    nota = input("Digite sua nota para Entrevista (Somente números inteiros entre 1 e 10): ")
                elif i == 1:
                    nota = input("Digite sua nota para Teste Teórico (Somente números inteiros entre 1 e 10): ")
                elif i == 2:
                    nota = input("Digite sua nota para Teste Prático (Somente números inteiros entre 1 e 10): ")
                else:
                    nota = input("Digite sua nota para Soft Skills (Somente números inteiros entre 1 e 10): ")

                if nota.isdigit() and 1 <= int(nota) <= 10:
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
