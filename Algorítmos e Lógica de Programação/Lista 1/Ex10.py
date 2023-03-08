"""
Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros 
fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, 
calcule quantos dias de vida um fumante perderá. Exiba o total de dias.
"""
diaria_cigarro = int(input("Quantos cigarros foram fumados por dia? "))
periodo_cigarro = int(input("Durante quantos anos fumou? "))
total_cigarro = diaria_cigarro*(periodo_cigarro * 365)
lifespan_reduction = (total_cigarro*10)/1440
print("Foram perdidos um total de {} dias de vida".format(int(lifespan_reduction)))
