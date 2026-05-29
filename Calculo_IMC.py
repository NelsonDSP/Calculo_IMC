# Sprint 3 - Histórico do IMC

def calcular_imc(peso, altura):
    altura_metros = altura / 100
    imc = peso / (altura_metros * altura_metros)
    return round(imc, 2)
 
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Excesso de peso"
    else:
        return "Obesidade"
    
peso = float(input("Introduza o seu peso (kg): "))
altura = float(input("Introduza a sua altura (cm): "))

imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)
 
print(f"IMC: {imc}")
print(classificacao)

