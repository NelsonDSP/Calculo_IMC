# Sprint 2 - Classificação do IMC

def calcular_imc(peso, altura):
    altura_metros = altura / 100
    imc = peso / (altura_metros * altura_metros)
    return round(imc, 2)
 
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
    
