"""
Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu algoritmo deve ler o valor 
da conta a ser paga e o valor do pagamento efetuado desprezando os centavos.Suponha que as notas para troco 
sejam as de 50, 20, 10, 5, 2 e 1 reais, e que nenhuma delas esteja em falta no caixa.
"""
price = int(input("Preço da conta: "))
paid = int(input("Valor do pagamento: "))
troco = paid-price
fifty = troco//50
twenty = troco%50//20
ten = troco%50%20//10
five = troco%50%20%10//5
two = troco%50%20%10%5//2
one = troco%50%20%10%5%2//1
print(f"{fifty} notas de R$50.00\n{twenty} notas de R$20.00\n{ten} notas de R$10.00\n{five} notas de R$5.00\n{two} notas de R$2.00\n{one} notas de R$1.00")
