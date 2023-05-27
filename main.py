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
                nota = input("Digite sua nota para Entrevista (entre 1 e 10): ")
            elif i == 1:
                nota = input("Digite sua nota para Teste Teórico (entre 1 e 10): ")
            elif i == 2:
                nota = input("Digite sua nota para Teste Prático (entre 1 e 10): ")
            else:
                nota = input("Digite sua nota para Soft Skills (entre 1 e 10): ")

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
    {"nome": "João", "notas": [7, 8, 9, 6]},
    {"nome": "Maria", "notas": [6, 7, 8, 9]},
    {"nome": "Pedro", "notas": [8, 7, 6, 9]},
    {"nome": "Ana", "notas": [7, 6, 8, 9]}
]

continuar = True
while continuar:
    notas_busca = []
    for i in range(4):
        nota_valida = False
        while not nota_valida:
            if i == 0:
                nota = input("Digite sua nota para Entrevista (entre 1 e 10): ")
            elif i == 1:
                nota = input("Digite sua nota para Teste Teórico (entre 1 e 10): ")
            elif i == 2:
                nota = input("Digite sua nota para Teste Prático (entre 1 e 10): ")
            else:
                nota = input("Digite sua nota para Soft Skills (entre 1 e 10): ")

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
            notas_formatadas = " ".join(f"{letra}_{nota}" for letra, nota in zip(['e', 't', 'p', 's'], notas_candidato))
            print(f"{nome} {notas_formatadas}")
    else:
        print("Nenhum candidato encontrado com as notas especificadas.")

    opcao = input("Deseja pesquisar novamente? (S/N): ")
    if opcao.upper() != 'S':
        continuar = False
        continue  # Pular para a próxima iteração do loop

    opcao_adicionar = input("Deseja adicionar um novo candidato? (S/N): ")
    if opcao_adicionar.upper() == 'S':
        adicionar_candidato(lista_candidatos)
