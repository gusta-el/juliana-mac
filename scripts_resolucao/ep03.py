#===================USP - MAC0110   Introdução à Computação===================
#===================Exercício-Programa 1 (EP1)===================
#===================Entregar até 18 de outubro de 2020===================
#Escreva um programa, na linguagem Python 3.x, que leia um número inteiro
#positivo n, e verifica se n é ou não a soma de três números primos consecutivos.
#No caso de n ser tal soma, o seu programa deve imprimir também os números
#primos correspondentes.

def verifica_primo(p):
	if p<=1 or (p != 2 and p % 2 == 0):
		return False
	elif p ==2:
		return True
	else:
		d = 3
		while ( d <= p//2):
			if(p% d == 0):
				return False
			d = d + 2
		return True
        
def verifica_valor_total(p, ponto_medio, ponto_medio_ant, ponto_medio_suc):
    valor_total = ponto_medio + ponto_medio_ant + ponto_medio_suc
    if valor_total==p:
        print(p, "é soma de três números primos consecutivos:")
        print(p, "=", ponto_medio_ant, "+", ponto_medio, "+",ponto_medio_suc)
        return True
    else:
        return False

def calcula_primos_consecutivos(n):
    ponto_medio = n // 3
    ponto_medio_ant = ponto_medio - 1
    ponto_medio_suc = ponto_medio + 1

    while(not verifica_primo(ponto_medio)):
        ponto_medio = ponto_medio - 1
        ponto_medio_suc = ponto_medio + 1
        ponto_medio_ant = ponto_medio - 1

    while(not verifica_primo(ponto_medio_ant)):
        ponto_medio_ant = ponto_medio_ant - 1
        
    while(not verifica_primo(ponto_medio_suc)):
        ponto_medio_suc = ponto_medio_suc + 1

    if(not verifica_valor_total(n, ponto_medio, ponto_medio_ant, ponto_medio_suc)):
        ponto_medio = n // 3
            
        while(not verifica_primo(ponto_medio)):
            ponto_medio = ponto_medio + 1
            ponto_medio_suc = ponto_medio + 1
            ponto_medio_ant = ponto_medio - 1

        while(not verifica_primo(ponto_medio_ant)):
            ponto_medio_ant = ponto_medio_ant - 1
            
        while(not verifica_primo(ponto_medio_suc)):
            ponto_medio_suc = ponto_medio_suc + 1
            
        if(not verifica_valor_total(n, ponto_medio, ponto_medio_ant, ponto_medio_suc)):
            print(n, "não é soma de três números primos consecutivos.")

def main():
    print("Este programa verifica se n é soma de três números primos consecutivos.")

    n = 0
    menor_soma_possivel = 10
    
    while(n <= 0):
        n = int(input("Digite um inteiro positivo para n: "))

    if n < menor_soma_possivel:
        print(n, "não é soma de três números primos consecutivos.")
    else:
        calcula_primos_consecutivos(n)


if __name__ == '__main__':
    main()    
    
