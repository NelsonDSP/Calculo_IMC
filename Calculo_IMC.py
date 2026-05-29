# Sprint 1 - Calculadora de IMC

peso = float(input("Introduza o seu peso (kg): "))
altura = float(input("Introduza a sua altura (cm): "))
 
altura_metros = altura / 100
imc = peso / (altura_metros * altura_metros)
 
imc = round(imc, 2)
 
print(f"IMC: {imc}")
 
if imc < 18.5:
    print("Fora do peso normal")
elif imc >= 18.5 and imc < 25:
    print("Peso normal")
else:
    print("Fora do peso normal")