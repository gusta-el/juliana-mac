
total_alunos = int(input("Digite o número de alunos da turma: "))
reprovados = 0
aprovados = 0
situacao = ""
separador = "**************************************************"
print(separador)

for x in range(total_alunos):
    
    print("ALUNO ", x+1)
    frequencia = int(input("Digite a frequencia: "))
    nota_p1 = int(input("Digite a nota de prova 1: "))
    nota_p2 = int(input("Digite a nota de prova 2: "))
    nota_p3 = int(input("Digite a nota de prova-sub: "))
    nota_ep1 = int(input("Digite a nota de EP 1: "))
    nota_ep2 = int(input("Digite a nota de EP 2: "))
    nota_ep3 = int(input("Digite a nota de EP 3: "))

    if nota_p1 == -1 and nota_p2 == -1 and nota_p3 == -1:
        nota_p1 = 0
        nota_p2 = 0
    elif nota_p1 == -1 and nota_p3 == -1:
        nota_p1 = 0
    elif nota_p2 == -1 and nota_p3 == -1:
        nota_p2 = 0
    elif nota_p1 == -1:
        nota_p1 = nota_p3
    elif nota_p2 == -1:
        nota_p2 = nota_p3
    else:
        nota_p3 = -1

    media_provas = (nota_p1 + (2 *nota_p2) )/3
    media_eps = ((4 * nota_ep1) + (5 * nota_ep2) + (11 * nota_ep3)) / 20

    if media_provas >=50 and media_eps>=50:
        media_final = ((3*media_provas) + media_eps)/4
    else:
        if media_provas >= media_eps:
            media_final = media_eps
        else:
            media_final = media_provas

    print("\nMedia das provas: ", media_provas)
    print("Media dos EPs: ", media_eps)
    print("Media final: ", media_final)
    
    if 30 <= media_final and media_final < 50:
        nota_recuperacao = int(input("Digite a nota da prova de recuperaçao: "))
        media_final = (media_final + nota_recuperacao)/2
        print("Media final apos recuperaçao: ", media_final)

    if media_final < 30 and frequencia < 70:
        situacao = "Reprovado por nota e por falta."
        reprovados = reprovados + 1
    elif frequencia < 70:
        situacao = "Reprovado por falta."
        reprovados = reprovados + 1
    elif media_final < 30:
        situacao = "Reprovado por nota."
        reprovados = reprovados + 1
    else:
        situacao = "Aprovado."
        aprovados = aprovados + 1
    
    print(situacao)
    print(separador, "\n")

print("Total de alunos aprovados: ", aprovados)
print("Total de alunos reprovados:: ", reprovados)



    


        
