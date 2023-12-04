while (1):
    # Recebe as diviões da palavra e o índice de cada divisão
    num1 = input("Digite o primeiro termo: ")  # u
    ind1 = input("Digite o índice do primeiro termo: ")
    num2 = input("Digite o segundo termo: ")  # v
    ind2 = input("Digite o índice do segundo termo: ")
    num3 = input("Digite o terceiro termo: ")  # z
    ind3 = input("Digite o índice do terceiro termo: ")
    p = input("Digite o valor de P: ")
    var1 = 0
    var2 = -1
    var3 = 0
    var4 = -1
    var5 = 0
    var6 = -1
    aux = 0
    aux1 = 0
    aux2 = 0
    aux3 = 0
    wordx = 0
    wordy = 0
    wordz = 0

    # Verifica se os índices são números negativos
    if ind1[0] == '-' or ind2[0] == '-' or ind3[0] == '-':
        print("Entrada inválida!")
        continue
    # Verifica se os símbolos que não pertence a linguagem foi inserido
    for caractere in num1:
        if caractere != 'a' and caractere != 'b':
            print("Entrada de x inválida!")
            aux = -1
            break
    for caractere in num2:
        if caractere != 'a' and caractere != 'b':
            print("Entrada de y inválida!")
            aux = -1
            break
    for caractere in num3:
        if caractere != 'a' and caractere != 'b':
            print("Entrada de z inválida!")
            aux = -1
            break
    if aux == -1:
        continue

    # Obtem o valor de x para índices p - x
    if ind1 == '0' and ind2 == '0' and ind3 == '0':
        print("A palavra vazia é aceita na linguagem.")
        break

    if len(ind1) >= 3:
        if ind1[0] == 'p':
            var1 = ind1[0]
            aux1 = ind1[1]
            var2 = ind1[2:]
            var4 = ind2
            wordx = int(p) - int(var2)
            wordy = int(var4)
        else:
            var2 = ind2
            wordx = int(var2)

    if len(ind2) >= 3:
        if ind2[0] == 'p':
            var3 = ind2[0]
            aux2 = ind2[1]
            var4 = ind2[2:]
            var2 = ind1
            wordy = int(p) - int(var4)
            wordx = int(var2)
        else:
            var4 = ind2
            wordy = int(var4)

    if len(ind3) >= 3:
        if ind3[0] == 'p':
            var5 = ind3[0]
            aux3 = ind3[1]
            var6 = ind3[2:]
            if aux3 == '-':
                wordz = int(p) - int(var6)
            else:
                wordz = int(p) + int(var6)
        else:
            var5 = ind3
            wordz = int(var5)
    else:
        if ind3 == 'p':
            wordz = int(p)
        else:
            wordz = int(ind3)

    # Verifica se uma das entradas foi p + x
    if aux == '+':
        print("Entrada parou no critério 1, digite outra entrada.")
        continue

    # Verifica se y == 'ab'
    for caractere in num2:
        if caractere == 'a':
            aux1 = 1
        else:
            aux2 = 2
    if aux1 == 1 and aux2 == 2:
        print("Entrada parou no critério 1, digite outra entrada.")
        continue

    # Verifica se uv = p
    if num2 == 'a':
        if len(ind1) < 3 and len(ind2) < 3:
            if ind2[0] == 'p':
                print("Entrada parou no critério 1, digite outra entrada.")
                continue
            var2 = ind1
            var4 = ind2
            wordx = int(var4)
            wordy = int(var2)
        if var4 == -1 and var2 == -1:
            print("Entrada parou no critério 1, digite outra entrada.")
            continue
        if var4 == -1 and var2 != -1:
            if int(var2) - int(var4) < 0:
                print("Entrada parou no critério 1, digite outra entrada.")
                continue
        if var4 != -1 and var2 == -1:
            if int(var4) - int(var2) < 0:
                print("Entrada parou no critério 1, digite outra entrada.")
                continue
        if var4 != -1 and var2 != -1:
            if var1 == 'p':
                if int(var2) - int(var4) < 0:
                    print("Entrada parou no critério 1, digite outra entrada.")
                    continue
            else:
                if int(var4) - int(var2) < 0:
                    print("Entrada parou no critério 1, digite outra entrada.")
                    continue
    else:
        if len(ind1) < 3:
            var1 = ind1[0]
            aux1 = ind1[1]
            var2 = ind1[2:]
            if var1 == 'p':
                var2 = ind1
                wordx = p
            else:
                var2 = ind1
                wordx = int(var2)
        if len(ind1) >= 3:
            var1 = ind1[0]
            if var1 == 'p' and aux1 == '+':
                print("Entrada parou no critério 1, digite outra entrada.")
                continue
        if var2 == 'p':
            var4 = ind2
            wordy = p
        else:
            var4 = ind2
            wordy = int(var2)
        if len(ind2) >= 3:
            if var3 == 'p' and aux2 == '+':
                print("Entrada parou no critério 1, digite outra entrada.")
                continue
    # Verifica se v > 0
    if ind2 == '0':
        print("Entrada parou no critério 2, digite outra entrada.")
        continue

    # Verifica se após retiramos v a palavra pertence a linguagem
    if ind1 != ind3 or ind1 == ind3:
        print(num1 * wordx + num2 * wordy + num3 * wordz)
        print("A Linguagem pode ser regular")
        break
    else:
        print("A Linguagem não é regular")
        break