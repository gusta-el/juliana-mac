salario=float(input("Digite seu salário: R$ "))
econ=float(input("Digite o quanto você vai economizar por mês: "))
aumento=float(input("Digite o aumento semestral do salário a partir do 6º mês: "))
custo_total=float(input("Digite o custo da casa: R$ "))
b=econ/100
a=aumento/100
y=salario*b
juros=1.0004
guarda=0
cont=0
while(guarda<=custo_total):
        y=salario*b
        guarda=guarda+y
        guarda=guarda*juros
        cont=cont+1
        if(cont%6==0):
                salario=salario*(1+a)
print(cont)
