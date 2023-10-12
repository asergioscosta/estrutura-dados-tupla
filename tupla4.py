num1 = int(input("Digite o 1 número: "))
num2 = int(input("Digite o 2 número: "))
def opera(tupla):
    operacao = tupla[0]
    num1 = tupla[1]
    num2 = tupla[2]

    if operacao == 'SOMA':
        return num1 + num2
    if operacao == 'MULT':
        return num1 * num2
    if operacao == 'DIV':
        return num1 / num2
    if operacao == 'SUB':
        return num1 - num2
    else:
        return None

resultado_soma = opera(('SOMA', num1, num2))
print("O resultado da soma será: ", resultado_soma)

resultado_mult = opera(('MULT', num1, num2))
print("O resultado da multiplicação será: ", resultado_mult)

resultado_div = opera(('DIV', num1, num2))
print("O resultado da divisão será: ", resultado_div)

resultado_sub = opera(('SUB', num1, num2))
print("O resultado da subtração será: ", resultado_sub)

resultado_pot = opera(('POT', num1, num2))
print("O resultado da potenciação será: ", resultado_pot)