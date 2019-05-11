__author__ = 'Stévillis Sousa'
__copyright__ = "Copyright 2019, Calculando Números Primos em um Intervalo"
__credits__ = ["Stévillis Sousa"]
__license__ = "MIT"
__version__ = "1.0.2"
__maintainer__ = "Stévillis Sousa"
__email__ = "stevillis@hotmail.com"
__status__ = "Production"


def calculaPrimo(numero):
    divisores = 0
    if numero > 0:
        for divisor in range(1, numero):
            if numero % divisor == 0:
                divisores += 1
                if divisores > 1:
                    break

        if divisores > 1:  # Número não é primo
            return False
        else:  # Número é primo
            return numero
    else:
        print('Número preciso ser maior que zero!')


def rangePrimos(numero_inicial, numero_final):
    lista_primos = []
    for numero in range(numero_inicial, numero_final):
        primo = calculaPrimo(numero)
        if primo:
            lista_primos.append(numero)

    return lista_primos


def diferencaPrimos(lista_primos):
    print('\n\nDiferença entre os números primos encontrados:\n[', end=' ')
    for cont, primo in enumerate(lista_primos):
        if cont > 0:
            print(primo - lista_primos[cont - 1], end=' ')
    print(']')


if __name__ == '__main__':
    dashes = '-'*60
    print(dashes)
    print('Este programa mostra a quantidade de números primos \nentre os intervalos dados a e b\n', dashes, '\n', sep='')

    try:
        sair = 0
        while sair != -1:

            a = int(input('Informe o intervalo inicial (a): '))
            b = int(input('Informe o intervalo inicial (b): '))

            if a >= b:
                print('Valor de a precisa ser menor que valor de b')
            else:
                lista_primos = rangePrimos(a, b)
                if len(lista_primos) > 0:
                    print(
                        f'\nExistem {len(lista_primos)} números primos entre {a} e {b}. \nEsses números são: ', end='')
                    for cont, primo in enumerate(lista_primos):
                        if cont == len(lista_primos) - 1:
                            print('e', primo, end=' ')
                        else:
                            print(primo, end=' ')

                    diferencaPrimos(lista_primos)

            sair = int(
                input('\n\nDeseja definir outros intervalos? (-1 para sair): '))
    except ValueError:
        raise ValueError('Apenas números são aceitos!')
