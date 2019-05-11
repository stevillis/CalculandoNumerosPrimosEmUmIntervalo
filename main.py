__author__ = 'Stévillis Sousa'

def calculaPrimo(numero):    
    divisores = 0
    if numero > 0:
        for divisor in range(1, numero):
            if numero % divisor == 0:
                divisores += 1
                if divisores > 1:            
                    break

        if divisores > 1 : # Número não é primo
            return False
        else: # Número é primo
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


if __name__ == '__main__':
    print('-'*60)
    print('Este programa mostra a quantidade de números primos \nentre os intervalos dados a e b\n', '-'*60, '\n', sep='')

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
                    print(f'\nExistem {len(lista_primos)} números primos entre {a} e {b}. \nEsses números são: ', end='')
                    for cont, primo in enumerate(lista_primos):
                        if cont == len(lista_primos) - 1:
                            print('e', primo, end=' ')
                        else:
                            print(primo, end=' ')
            
            sair = int(input('\n\nDeseja definir outros intervalos? (-1 para sair): '))    
    except ValueError:
        print('Apenas números são aceitos!')
        
    


