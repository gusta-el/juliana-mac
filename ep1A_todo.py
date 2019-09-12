salario=float(input("Digite seu salário: R$ "))
econ=float(input("Digite o quanto você vai economizar por mês: "))
custo_total=float(input("Digite o custo da casa: R$ "))
b=econ/100
y=salario*b
juros=1.0004
guarda=0
cont=0
while(guarda<=custo_total):
        guarda=guarda+y
        guarda=guarda*juros
        cont=cont+1
print(cont)





