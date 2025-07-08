"""
CALCULO DO PRIMEIRO DÍGITO DO CPF:
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma contagem regressiva começando de 10

Ex: 746.824.890-70 (74682489070)
    10  9   8   7   6   5   4   3   2 
*   7   4   6   8   2   4   8   9   0
    70  36  48  56  12  20  32  27  0
    
Somar todos os resultados:
70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
senão
    resultado é o próprio valor da conta
    
O primeiro dígito do CPF é 7
    
"""

cpf_do_usuario = input("Digite seu CPF (apenas números): ").strip().casefold()
comprimento_do_cpf = 11

while len(cpf_do_usuario) != comprimento_do_cpf:
    print("Tamanho inválido!")
    cpf_do_usuario = input("Digite seu CPF (apenas números): ").strip().casefold()

nove_digitos = cpf_do_usuario[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0

for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
    
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)


"""
CALCULO DO SEGUNDO DÍGITO DO CPF:
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF, MAIS O PRIMEIRO DÍGITO,
multiplicando cada um dos valores por uma contagem regressiva
começando de 11

Ex: 746.824.890-70 (74682489070)
    11  10  9   8   7   6   5   4   3  2 
*   7   4   6   8   2   4   8   9   0  7 <= PRIMEIRO DIGITO 
    77  49  54  64  14  24  40  36  0  14
    
Somar todos os resultados:
77 + 49 + 54 + 64 + 14 + 24 + 40 + 36 + 0 + 14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
senão:
    resultado é o valor da conta
     
"""

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
    
digito_2 = (resultado_digito_2) * 10 % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)

cpf_gerado = f"{cpf_do_usuario}{digito_1}{digito_2}"

if cpf_do_usuario == cpf_gerado:
    print(f"O CPF {cpf_do_usuario} é válido!")
else:
    print(f"O CPF {cpf_do_usuario} NÃO é válido!")
