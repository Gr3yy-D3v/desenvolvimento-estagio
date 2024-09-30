'''
Questão número 1

INDICE = 13
SOMA = 0
K = 0
while K < INDICE:
    K = K + 1
    SOMA = SOMA + K
print(SOMA)
'''
# Função para verificar se um número pertence à sequência de Fibonacci
def is_fibonacci(num):
    if num < 0:
        return False
    
    # Inicia a sequência com os primeiros dois valores
    fib1, fib2 = 0, 1
    
    # Verifica se o número é igual a um dos dois primeiros valores
    if num == fib1 or num == fib2:
        return True
    
    # Gera a sequência até que fib2 seja maior ou igual ao número informado
    while fib2 <= num:
        fib1, fib2 = fib2, fib1 + fib2
    
    # Verifica se o número informado pertence à sequência
    return fib2 == num

# Solicita ao usuário que informe um número
try:
    numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    
    if is_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, insira um número inteiro válido.")

