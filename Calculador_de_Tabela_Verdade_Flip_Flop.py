# Este programa demonstra a tabela verdade de um flip flop, este pode ser do tipo RS, D, JK e T.
# Declaração das variáveis: flfp (flip flop);
while True:
    print('''\n[Cálculo da tabela verdade]
    Primeiro selecione um tipo de flip-flop:
    [1] Reset & Set (RS)
    [2] Tipo D
    [3] Jack Kilby (JK)
    [4] Tipo Toggle
    [5] Sair\n''')
    flfp = int(input("Digite uma das opções: "))

    if flfp == 5:
        break

    # Verificação do input.
    while True:
        if flfp > 5 or flfp < 1:
            print("\nEscolha inválida, tente novamente.")
            flfp = int(input("Digite uma das opções: "))
        else:
            break

    # Cálculo da tabela verdade do flip flop RS. 
    if flfp == 1:
        # Declaração das variáveis Reset e Set.
        s = int(input("Defina o Set (0 ou 1): "))
        r = int(input("Defina o Reset (0 ou 1): "))

        # Invalidações. 
        while True:
            if s == 1 and r == 1:
                print("\nFlip Flop inválido, Set e Reset não podem ser ativados ao mesmo tempo.")
                s = int(input("Defina o Set (0 ou 1): "))
                r = int(input("Defina o Reset (0 ou 1): "))
            elif (s > 1 or s < 0) or (r > 1 or r < 0):
                print("\nNúmeros digitados inválidos.")
                s = int(input("Defina o Set (0 ou 1): "))
                r = int(input("Defina o Reset (0 ou 1): "))
            else:
                break
        
        # Cálculo da tabela verdade. 
        if s == 1 and r == 0:
            print('''\nTabela Verdade:
            [S] = 1
            [R] = 0
            [Q] = 1
            [ÑQ] = 0''')
        elif s == 0 and r == 1:
            print('''\nTabela Verdade:
            [S] = 0
            [R] = 1
            [Q] = 0
            [ÑQ] = 1''')
        else:
            print('''Tabela Verdade:
            [S] = 0
            [R] = 0
            [Q] = Mantém o último valor
            [ÑQ] = ÑQ''')

    # Flip Flop D
    if flfp == 2:
        # Declaração das variáveis Reset e Set.
        s = int(input("Defina o Set (0 ou 1): "))

        # Invalidações. 
        while True:
            if (s > 1 or s < 0):
                print("\nNúmero digitado inválido.")
                s = int(input("Defina o Set (0 ou 1): "))
            else:
                break

        if s == 1:
            print('''Tabela Verdade
            [S] = 1
            [R] = 0
            [Q] = 1
            [ÑQ] = 0''')
        else:
            print('''Tabela Verdade
            [S] = 0
            [R] = 1
            [Q] = 0
            [ÑQ] = 1''')

    # Flip Flop JK
    if flfp == 3:
        j = int(input("Defina o J (0 ou 1): "))
        k = int(input("Defina o K (0 ou 1): "))

        # Invalidações
        while True:
            if (j > 1 or j < 0) or (k > 1 or k < 0):
                print("\nNúmero digitado inválido.")
                j = int(input("Defina o J (0 ou 1): "))
                k = int(input("Defina o K (0 ou 1): "))
            else:
                break
        
        # Tabela Verdade
        if j == 0 and k == 0:
            print('''Tabela Verdade
            [J] = 0
            [K] = 0
            [Q] = Q(t)
            [ÑQ] = ÑQ(t)
            
            Armazena o valor anterior.''')
        elif j == 1 and k == 0:
            print('''Tabela Verdade
            [J] = 1
            [K] = 0
            [Q] = 1
            [ÑQ] = 0''')
        elif j == 0 and k == 1:
            print('''Tabela Verdade
            [J] = 0
            [K] = 1
            [Q] = 0
            [ÑQ] = 1''')
        else:
            print('''Tabela Verdade
            [J] = 0
            [K] = 0
            [Q] = Q(t + 1)
            [ÑQ] = ÑQ(t + 1)
            
            Efeito de alternância. O próximo valor de Q será diferente do anterior no posterior ciclo (t)''')
        
    # Flip Flop Toggle (t)
    if flfp == 4:
        T = int(input("Defina o T (0 ou 1): "))

        # Invalidações
        while True:
            if (T > 1 or T < 0):
                print("\nNúmero digitado inválido.")
                j = int(input("Defina o T (0 ou 1): "))
            else:
                break
        
        # Tabela Verdade
        if T == 0:
            print('''Tabela Verdade
            [T] = 0
            [J] = 0
            [K] = 0
            [Q] = Q(t)
            [ÑQ] = ÑQ(t)
            
            Efeito de armazenamento.''')
        else:
            print('''Tabela Verdade
            [T] = 1
            [J] = 1
            [K] = 1
            [Q] = Q(t + 1)
            [ÑQ] = ÑQ(t + 1)
            
            Efeito de alternância. O sistema permanecerá nesse estado até que T volte a ser 0.''')
