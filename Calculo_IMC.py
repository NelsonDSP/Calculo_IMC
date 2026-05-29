#A fórmula do IMC é: IMC = peso / (altura_em_metros * altura_em_metros)

peso = float(input("Introduza o seu peso (kg): "))
altura = float(input("Introduza a sua altura (cm): "))
 
altura_metros = altura / 100
imc = peso / (altura_metros * altura_metros)
