# L = {a^nb^n / n >= 0}
def bombeamento(p, k, j):
    # Monta a palavra de acordo com o comprimento passado
    palavra = "a"*p+"b"*p

    # Pega o começo da palavra
    u = palavra[0:p-j]
    print("u:", u)

    # Pega j letras que serão bombeadas
    v = palavra[p - j:p]
    print("v:", v)

    # Pega o resto da palavra
    z = palavra[p:]
    print("z:", z)

    aux = 0
    # Aplica o bombeamento repetindo v
    for i in range(k+1):
        nova_palavra = u + v*i + z
        print("\n",nova_palavra)
        if nova_palavra == palavra:
            aux += 1

    # Verifica se a nova palavra ainda pertence à linguagem
    if aux == k+1 and k != 0 or aux > k:
        return "\nA linguagem pode ser regular."
    else:
        return "\nA linguagem não é regular."

# Obtém o comprimento da palavra
# Condições: p >= 0
while(1):
    p = int(input("Digite o valor do comprimento do bombeamento: "))
    if p < 0:
        continue
    else:
        break

# Condições: |uv| <= p - o comprimento da parte que pode ser "bombeada" é limitado pelo comprimento de bombeamento.
# Condições: |v| > 0 - a parte v não pode ser vazia.
# Tamanho de v não pode ser maior que p (comprimento do bombeamento)
while(1):
    # Tratamento para palavra vazia
    if p == 0:
        j = int(input("Digite o tamanho da divisão de v: "))
        break

    j = int(input("Digite o tamanho da divisão de v: ")) # Esse valor significa a quantidade de elementos de 'v' que serão submetidos ao bombeamento
    if j > p or j <= 0:
        continue
    else:
        break

k = int(input("Digite a quantidade de bombeamento k: "))

teste = bombeamento(p, k, j)
print(teste)

# Casos de teste
"""
Caso 1:
    p = 0
    j = qualquer
    k = qualquer
    resultado = palavra vazia é reconhecida pela linguagem
    
Caso 2:
    p > 0
    1 <= j <= p
    k = 1
    resultado = linguagem não é regular
    
Caso 3:
    p > 0
    1 <= j <= p
    k > 1
    resultado = linguagem não é regular
"""


