#Crie um algoritmo que solicite ao usuário o seu turno de trabalho e a quantidade
#de horas trabalhadas, calcule e mostre o valor do salário. Considere os valores de
#horas a seguir, de acordo com o turno de trabalho. Caso o turno seja igual a ‘N’
#(utilize um caractere para representar) o valor da hora trabalhada é R$ 45,00, caso
#contrário é R$ 37,50


turno = input("Digite aqui o seu Turno de Trabalho (D)=DIURNO e (N)=NOTURNO:")
horas = int(input("Digite aqui o tanto de horas trabalhadas:"))

if turno=="d" or "D":
    print ("o valor do seu salario é" ,(37.50*horas))
elif turno=="n" or "N":
    print ("o valor do seu salario é" ,(45.00*horas))
else :
    print ("informações invalidas")