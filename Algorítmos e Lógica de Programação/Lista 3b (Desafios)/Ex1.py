"""
Dizemos que um número natural é triangularse ele é produto de três números naturais consecutivos. 
Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se né triangular.
"""
num = int(input("Digite um inteiro positivo: "))
if num < 0:
    print("O numero precisa ser positivo.")
else:
    f_cube = int(num**(1/3))
    p_num = f_cube*(f_cube+1)*(f_cube+2)
    if p_num == num:
        print(f"{num} é um numero triangular")
    else:
        print(f"{num} não é um numero triangular")
