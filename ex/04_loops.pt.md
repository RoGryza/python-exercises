# Laços de Repetição

1. 

    1. Escreva um programa que peça um número `n` e mostre a soma de todos os números de 1 até `n`.

    2. Modifique o programa anterior para que apenas múltiplos de 3 ou 5 sejam considerados para a
       soma.

1. Escreva um programa que calcula o fatorial de um número.

1. 

    1. Escreva um programa que, dado um número `n`, imprima o seguinte padrão:
            
            Tamanho: 4
            1
            22
            333
            4444
    
        !!! note "Nota"
            O operador `*` entre strings e números replica a string várias vezes. Não utilizá-lo para
            este exercício.

    2. Modifique o programa anterior para incrementar os números na mesma linha:
  
            Tamanho: 10
            1
            2 3
            4 5 6
            7 8 9 10

1. 

    1. Escreva um programa que peça um número e imprima a tabuada dele de 1 a 10.

    2. Modifique o programa anterior para executar novamente até que o usuário entre com 0.

            Número: 1
            1 * 1 = 1
            1 * 2 = 2
            ...
     
            Número: 5
            5 * 1 = 5 
            5 * 2 = 10
            ...

            Número: 0

1. Escreva um programa em que o usuário tem que adivinhar um número entre 1 e 10 em 3 tentativas. A
   cada tentativa errada, imprima se ela foi maior ou menor do que o número.
   
    !!! tip "Dica"
        Para gerar números aleatórios é necessário utilizar a função `randint` da biblioteca padrão:

            :::python
            from random import randint # Faz com que a função randint esteja disponível
            x = randint(1, 10) # x recebe um número aleatório tal que 1 <= x <= 10

1. Escreva um programa que imprima todos os números primos de 1 a 100.
