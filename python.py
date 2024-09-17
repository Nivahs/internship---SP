#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#• SP – R$67.836,43
#• RJ – R$36.678,66
#• MG – R$29.229,88
#• ES – R$27.165,48
#• Outros – R$19.849,53
#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  


dic_estados = { 'SP': 67836.43,
'RJ': 36678.66,
'MG': 29229.88,
'ES': 27165.48,
}
other = 19849.53
value_total = 0
per_estados = {}


for estado, valor in dic_estados.items():
    value_total += valor

for estado, valor in dic_estados.items():
    per_estado = (valor / value_total) * 100
    per_estados[estado] = per_estado
    print(f"Estado: {estado}\nValor: {valor}\nPorcentagem: {per_estado:.2f}%")
    print()

print(f"R${value_total:.2f}")