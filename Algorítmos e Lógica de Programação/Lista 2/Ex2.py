# Determine se um ano é bissexto.Verifiqueno Google como fazer isso...
ano = int(input("Digite um ano: "))
if ano % 400 == 0:
    print("Este ano é bissexto")
elif ano % 100 == 0:
    print("Este ano não é bissexto")
elif ano % 4 == 0:
    print("Este ano é bissexto")
else:
    print("Este ano não é bissexto")
    