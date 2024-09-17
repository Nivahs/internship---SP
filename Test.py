
print('='*90)
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K
    
print(SOMA)


#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o 
#próximo valor sempre será a soma dos 2 valores anteriores 
#(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa 
#na linguagem que desejar onde, informado um número, ele calcule a 
#sequência de Fibonacci e retorne uma mensagem avisando se o número 
#informado pertence ou não a sequência.
print('='*90)

a = 0
b = 1
list_fibo = []

maxi = int(input("Informe o número de termos que deseja na sequência de Fibonacci: "))

while a <= maxi:
    list_fibo.append(a)
    temp = a + b
    a = b
    b = temp

if maxi in list_fibo:
    print(f"O valor {maxi} está presente na Lista de Fibonacci")
else:
    print(f"O valor {maxi} não está presente na Lista de Fibonacci")

for i in list_fibo:
    print(f"{i}", end=" ")
#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
print()
print('='*90)

import json

# Carregar os dados 
with open('faturamento.json', 'r') as file:
    data = json.load(file)

faturamento_diario = data['faturamento_diario']

#  variáveis
menor_faturamento = float('inf')  
maior_faturamento = float('-inf') 
total_faturamento = 0
dias_com_faturamento = 0

# cada entrada de faturamento
for entrada in faturamento_diario:
    valor = entrada['valor']
    if valor > 0:
        #  menor e maior valor de faturamento
        if valor < menor_faturamento:
            menor_faturamento = valor
        if valor > maior_faturamento:
            maior_faturamento = valor
        
        # Somar o faturamento e contar os dias 
        total_faturamento += valor
        dias_com_faturamento += 1

# média de faturamento
if dias_com_faturamento > 0:
    media_faturamento = total_faturamento / dias_com_faturamento
else:
    media_faturamento = 0

#  dias com faturamento superior à média
dias_acima_da_media = 0
for entrada in faturamento_diario:
    valor = entrada['valor']
    if valor > media_faturamento:
        dias_acima_da_media += 1

# Resultados
print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento superior à média: {dias_acima_da_media}")
print('='*90)
print()
#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#• SP – R$67.836,43
#• RJ – R$36.678,66
#• MG – R$29.229,88
#• ES – R$27.165,48
#• Outros – R$19.849,53
#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  
fat_SP = 67836.43
fat_RJ = 36678.66
fat_MG = 29229.88
fat_ES = 27165.48
fat_Outros = 19849.53

fat_total = fat_SP + fat_RJ + fat_MG + fat_ES + fat_Outros

per_SP = (fat_SP / fat_total) * 100
per_RJ = (fat_RJ / fat_total) * 100
per_MG = (fat_MG / fat_total) * 100
per_ES = (fat_ES / fat_total) * 100

print("O percentual de cada Estado dentro do total mensal. ")
print()
print(f"São Paulo: {per_SP:.2f}% \nRio de Janeiro: {per_RJ:.2f}% \nMinas Gerais: {per_MG:.2f}% \nEspirito Santo: {per_ES:.2f}% \n")

#5) Escreva um programa que inverta os caracteres de um string.

user_string = str(input("Digite uma palavra para inverter: "))
invert_string = user_string[::-1]
print(invert_string)
