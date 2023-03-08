# Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.
price = float(input("Preço do produto: "))
discount = float(input("Desconto: "))
price_off = price*(discount/100)
to_pay = price-price_off
print("com o desconto de {} reais, o preço a se pagar é de {} reais.".format(price_off, to_pay))
