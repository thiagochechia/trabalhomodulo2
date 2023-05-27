def obter_nota_valida(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Por favor, digite um número entre 0 e 10.")
        except ValueError:
            print("Por favor, digite um número válido.")

def pesquisar_notas_por_criterio(string, criterios):
    valores = string.split(',')
    notas = valores[1].split('_')

    for nota in notas:
        prefixo, valor = nota.split('x')
        if prefixo in criterios and float(valor) <= criterios[prefixo]:
            return False
    
    return True

# Exemplo de uso
string_notas = [
    "João,ex9.5_tx8.7_px7.2_sx9.0",
    "Maria,ex8.0_tx7.5_px6.8_sx7.2",
    "Pedro,ex7.2_tx6.5_px8.0_sx9.5",
    "Lucas,ex6.8_tx7.0_px8.5_sx7.7",
    "Ivo,ex6.8_tx7.0_px8.5_sx7.7",
    "Livia,ex6.8_tx7.0_px8.5_sx7.7",
    "Naldo,ex6.8_tx7.0_px8.5_sx7.7"
]

criterios = {
    'ex': 0,
    'tx': 0,
    'px': 0,
    'sx': 0
}

usuarios_selecionados = []

for nota_pesquisada in criterios:
    nota_digitada = obter_nota_valida(f"Digite a nota pesquisada para {nota_pesquisada}: ")
    criterios[nota_pesquisada] = nota_digitada

for string in string_notas:
    if pesquisar_notas_por_criterio(string, criterios):
        usuarios_selecionados.append(string.split(',')[0])

if usuarios_selecionados:
    print("Lista de usuários que atendem a todos os critérios pesquisados:")
    for usuario in usuarios_selecionados:
        print(usuario)
else:
    print("Nenhum usuário encontrado que atenda a todos os critérios pesquisados.")
def obter_nota_valida(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Por favor, digite um número entre 0 e 10.")
        except ValueError:
            print("Por favor, digite um número válido.")

def pesquisar_notas_por_criterio(string, criterios):
    valores = string.split(',')
    notas = valores[1].split('_')

    for nota in notas:
        prefixo, valor = nota.split('x')
        if prefixo in criterios and float(valor) <= criterios[prefixo]:
            return False
    
    return True


