from random import randint

def ProcuraPrimeiroNumero(RETANG, PADRAO, i, j):
    while i < 8:
        while j < 9:
            if RETANG[i][j] == PADRAO[0]:
                COORDENADA = [i,j]
                return COORDENADA
            j = j + 1
        i = i + 1
        j = 0
    return -1

def VerificaSeCabe(RETANG, t, direcao, i, j):
    result = 0
    if direcao == 11:
        if (i + 1 - t)  >= 0:
            result = 1
    if direcao == 33:
        if (i + t)  <= 8:
            result = 1
    if direcao == 22:
        if (j + t)  <= 9:
            result = 1
    if direcao == 44:
        if (j + 1 - t)  >= 0:
            result = 1
    if direcao == 12:
        if (i + 1 - t)  >= 0 and (j + t)  <= 9:
            result = 1
    if direcao == 14:
        if (i + 1 - t)  >= 0 and (j + 1 - t)  >= 0:
            result = 1
    if direcao == 32:
        if (i + t)  <= 8 and (j + t)  <= 9:
            result = 1
    if direcao == 34:
        if (i + t)  <= 8 and (j + 1 - t)  >= 0:
            result = 1
    return result

def AchaPadrao(RETANG, PADRAO, direcao, i, j):
    result = False
    if direcao == 11:
        for aux in range(len(PADRAO)):
            if RETANG[i][j] == PADRAO[aux]:
                result = True
            else:
                return False
            i -= 1
    if direcao == 33:
        for aux in range(len(PADRAO)):
            if RETANG[i][j] == PADRAO[aux]:
                result = True
            else:
                return False
            i += 1
    if direcao == 22:
        for aux in range(len(PADRAO)):
            if RETANG[i][j] == PADRAO[aux]:
                result = True
            else:
                return False
            j += 1
    if direcao == 44:
        for aux in range(len(PADRAO)):
            if RETANG[i][j] == PADRAO[aux]:
                result = True
            else:
                return False
            j -= 1
    if direcao == 12:
        for aux in range(len(PADRAO)):
            if RETANG[i][j] == PADRAO[aux]:
                result = True
            else:
                return False                
            i -= 1
            j += 1
    if direcao == 14:
        for aux in range(len(PADRAO)):
            if RETANG[i][j] == PADRAO[aux]:
                result = True
            else:
                return False
            i -= 1
            j -= 1
    if direcao == 32:
        for aux in range(len(PADRAO)):
            if RETANG[i][j] == PADRAO[aux]:
                result = True
            else:
                return False
            i += 1
            j += 1
    if direcao == 34:
        for aux in range(len(PADRAO)):
            if RETANG[i][j] == PADRAO[aux]:
                result = True
            else:
                return False
            i += 1
            j -= 1
    return result  

def EncontraPadrao(COORDENADA, RETANG, PADRAO, direcao, direcao_texto):
    if VerificaSeCabe(RETANG, len(PADRAO), direcao, COORDENADA[0], COORDENADA[1]) == 1:
        if AchaPadrao(RETANG, PADRAO, direcao, COORDENADA[0], COORDENADA[1]):
            print("padrão ", PADRAO, " começa em ", COORDENADA, " com direção", direcao_texto)
            return True
    return False

def CacaPadrao(RETANG, PADRAO, DIRECOES):
    aux = 0
    COORDENADA = ProcuraPrimeiroNumero(RETANG, PADRAO, 0, 0)
    if COORDENADA != -1:
        while COORDENADA != -1 and aux != len(DIRECOES) + 1:
            aux = 0
            while aux < len(DIRECOES):
                if EncontraPadrao(COORDENADA, RETANG, PADRAO, DIRECOES[aux][1], DIRECOES[aux][0]):
                    aux = len(DIRECOES)
                aux += 1
            COORDENADA = ProcuraPrimeiroNumero(RETANG, PADRAO, COORDENADA[0], COORDENADA[1]+1)
    if aux != len(DIRECOES) + 1:
        print("padrão ", PADRAO, " não ocorre.")

DIRECOES = [["norte", 11],["nordeste", 12],["leste", 22],["sudeste", 32],
            ["sul", 33],["sudoeste", 34],["oeste", 44],["noroeste", 14]]

RETANG = [[]]
i = 0
j = 0

#construir matriz
for i in range(8):
    line = []
    for j in range(9):
        line.insert(j, randint(1,9))
    RETANG.insert(i, line)

#imprimindo matriz
for i in range(8):
    text_line = ""
    for j in range(9):
        text_line = text_line +  "  " + (str)(RETANG[i][j])
    print(text_line)

print(len(RETANG[0]))
print(len(RETANG))

PADRAO = []
p = int(input("Digite a quantidade de padrões (p): "))

while p < 5:
    print("O número mínimo de padrões é 5!!")
    p = int(input("Digite a quantidade de padrões (p): "))

for i in range (p):
    #construir padrao
    print("Digite o ", i + 1, "º padrão númerico")
    PADRAO_STR = input("")
    t = len(PADRAO_STR)
    for i in range(t):
        PADRAO.insert(i, int(PADRAO_STR[i]))
    CacaPadrao(RETANG, PADRAO, DIRECOES)
    PADRAO = []



