"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
"""
while True:
    username = input("Nome de usuário: ")
    password = input("Senha: ")
    if username == password:
        print("Nome de usuário e Senha não podem ser iguais")
    else:
      break
