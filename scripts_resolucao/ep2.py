#Função para calcular pi através da série de pi:
def AproxSerie(k):
#iniciando valor de pi como 0    
    pi = 0
#para cada número de termos da série, executar os comandos abaixo:
    for n in range(k):
        #serie atual representa a f(x) = 2x +1 onde x é o termo atual
        serie_atual = 2*n + 1
    #se serie for 1 quer dizer que n é o primeiro termo. Devemos adicionar um ao pi para iniciar o cálculo
        if serie_atual == 1:
            pi = 1
    #os proximos termos terão operacoes de soma e subtração intercalados
        #caso o resto do termo atual seja divísivel por 2, iremos somar uma parte da serie atual
        elif n % 2 == 0:
            pi = pi +  (1 / serie_atual)
        #senão iremos subtrair uma parte da serie atual
        else:
            pi = pi -  (1 / serie_atual)
    #a serie de pi calculo 1/4 de pi. O retorno da função multiplica o resultado da serie por 4.
    return pi*4


#Função para calcular pi através da área de um quarto de círculo
def AproxRetang(n, r):
#iniciando valor de um quarto da area como 0
    A = 0
#definindo constante da largura do retangulo dividindo o raio pelo número de retangulos desejados
    w = r / n
#primeiro ponto médio (x) será dado pela metade da largura do primeiro retangulo 
    x = w / 2
#Para cada retangulo executar os comandos abaixos
    for i in range(n):
        #Calcula a altura do retangulo pela formula: h=(r^2-x^2)^(1/2)        
        h = ((r**2) - (x**2))**(1/2)
        #Calculando área do retangulo atual e somando a área total correspondente a 1/4 do círculo
        A = A + (w * h)
        #Alterando o ponto médio do retangulo para o próximo retangulo 
        x = x + w
#retorna a soma das areas dos retangulos
    return A


#Comandos para realizar os dados obrigatórios para teste:
k = 10
n = 10
r = 2
print("Cálculo da área de um quarto de um círculo:",k,"termos para a série e raio =",r,"cm e",n,"retângulos.")
print("Pi através da série de pi", AproxSerie(k))
print("Pi através de um quarto da área do círculo: ",AproxRetang(n, r))
print("================================================================================================\n")

k = n = 100
print("Cálculo da área de um quarto de um círculo:",k,"termos para a série e raio =",r,"cm e",n,"retângulos.")
print("Pi através da série de pi", AproxSerie(k))
print("Pi através de um quarto da área do círculo: ",AproxRetang(n, r))
print("================================================================================================\n")

k = n = 500
print("Cálculo da área de um quarto de um círculo:",k,"termos para a série e raio =",r,"cm e",n,"retângulos.")
print("Pi através da série de pi", AproxSerie(k))
print("Pi através de um quarto da área do círculo: ",AproxRetang(n, r))
print("================================================================================================\n")

k = 1000
n = 500
print("Cálculo da área de um quarto de um círculo:",k,"termos para a série e raio =",r,"cm e",n,"retângulos.")
print("Pi através da série de pi", AproxSerie(k))
print("Pi através de um quarto da área do círculo: ",AproxRetang(n, r))
print("================================================================================================\n")

k = 500
n = 1000
print("Cálculo da área de um quarto de um círculo:",k,"termos para a série e raio =",r,"cm e",n,"retângulos.")
print("Pi através da série de pi", AproxSerie(k))
print("Pi através de um quarto da área do círculo: ",AproxRetang(n, r))
print("================================================================================================\n")
