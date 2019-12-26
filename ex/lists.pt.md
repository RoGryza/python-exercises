# Listas

1. Escreva um programa que imprima o maior elemento de uma lista de números.

2. Escreva um programa que verifique se um elemento existe numa lista.

    !!! note "Nota"
        O python tem uma forma pronta de fazer esta verificação com a operação `in`. Não utilizá-la
        para este exercício.

1. Escreva uma função que, dada uma lista, retorna outra lista apenas com os elementos em posições
   ímpares da lista original.

        :::pycon
        >>> impares([1,2,3,4,5])
        [2,4]
        >>> impares([])
        []

1. Escreva uma função que concatena duas listas.

        :::pycon
        >>> concat([1, 2], [3, 4])
        [1, 2, 3, 4]
        >>> concat([], ["a"])
        ["a"]
    
    !!! note "Nota"
        O python define `+` entre listas como concatenação. Não utilizar esta operação para este
        exercício.

1. 

    1. Escreva uma função que junte duas listas do mesmo tamanho alternando seus elementos.

            :::pycon
            >>> merge([1, 2], ["a", "b"])
            [1, "a", 2, "b"]

        !!! note "Nota"
            O python tem a função https://docs.python.org/3/library/functions.html#zip que faz esta
            operação com qualquer quantidade de listas. Não utilizá-la para este exercício.

    2. Modifique a função anterior para que ela aceite listas de tamanho diferente e preencha com
       `None` os elementos que faltam da lista menor.

            :::pycon
            >>> merge([1, 2, 3, 4], ["a", "b"])
            [1, "a", 2, "b", 3, None, 4, None]
