     #Exercicio1

soma = 0
contador = 0

print("Informe os números:")


while True:
    numero = int(input("> "))
    
    if numero == 0:
        break  
    
    soma += numero  
    contador += 1 

if contador > 0:
    media = soma / contador
    print(f"Soma: {soma}")
    print(f"Média: {media:.2f}")
else:
    print("Nenhum número foi informado.")

     #Exercicio2

maior = None
menor = None

print("Informe os números:")


while True:
    numero = int(input("> "))
    
    if numero == 0:
        break  
    
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero

if maior is not None and menor is not None:
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")
else:
    print("Nenhum número foi informado.")

     #Exercicio3

def fibonacci(n):
    
    a, b = 1, 1
    
    for _ in range(3, n + 1):
        a, b = b, a + b  
    
    return b

n = int(input("Digite o valor de n (n ≥ 3): "))

if n >= 3:
    resultado = fibonacci(n)
    print(f"O {n}-ésimo termo da sequência de Fibonacci é: {resultado}")
else:
    print("O valor de n deve ser maior ou igual a 3.")

     #Exercicio4

     def verificar_primo(numero):
    
    if numero <= 1:
        return False
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Informe o número: "))

if verificar_primo(numero):
    print("Resposta: primo")
else:
    print("Resposta: não primo")
