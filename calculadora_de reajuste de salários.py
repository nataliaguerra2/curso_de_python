salário=float(input("informe o seu salário"))
if salário < 128000:
    percentagem=0.2
    aumento=salário*percentagem
    novo_salário=salário+aumento
elif (salário>=128000 and salário<=500000):
    percentagem=0.15
    aumento=salário*percentagem
    novo_salário=salário+aumento
elif (salário>=500000 and salário<=1000000):
    percentagem=0.1
    aumento=salário*percentagem
    novo_salário=salário+aumento
else:
    percentagem=0.05
    aumento=salário*percentagem
    novo_salário=salário+aumeto
print (" salário antes do reajuste:",salário)
print ("precentagem:", percentagem)
print ("aumento a ser aplicado:",aumento)
print ("novo salário",novo_salário)
    






















    
