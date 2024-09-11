# Crie um programa que receba a nota de um aluno e informe se ele foi aprovado ou reprovado. Considere que a média para aprovação é 7.


nota = float(input("Digite sua nota "))

if nota <=6:
    print("Você está reprovado!")
else:
    print("Você está aprovado")