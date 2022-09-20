idade = int(input("digite sua idade:"))

if idade < 16 :
    print("não eleitor")
elif idade >= 18 and idade <= 65:
    print("eleitor obrigatório")
else :
    idade >= 16 and idade <= 18 or idade > 65 
    print("eleitor facultativo")