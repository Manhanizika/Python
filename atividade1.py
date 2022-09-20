#Uma empresa está selecionando entre seus estagiários os que irão fazer um
#treinamento especial. O selecionado deve satisfazer ao mesmo tempo a dois critérios.

#O primeiro critério é que ele deve ter uma bolsa maior ou igual a R$ 750,00 e
#menor ou igual a R$ 950,00.

#O segundo critério leva em conta o tempo de estágio, este deve ser maior ou
#igual a 2 anos.

#Escreva um algoritmo que solicite ao usuário o valor da bolsa e o tempo de estágio, e
#caso os critérios acima sejam satisfeitos, mostre a mensagem “Participará do
#treinamento”, caso contrário mostre “Não participará”

bolsa = float(input("Qual o valor da Bolsa:"))
tempo = int(input("Quanto tempo do estágio:"))

if (tempo >= 2) and (bolsa >= 750 and bolsa <= 950):
    print("Participará do Treinamento")
else :
    print("Não Participará")