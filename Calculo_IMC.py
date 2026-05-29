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

historico_imcs = []
historico_classificacoes = []
 
while True:
    try:
        peso = float(input("Introduza o seu peso (kg): "))
        altura = float(input("Introduza a sua altura (cm): "))
        
        if peso <= 0 or altura <= 0:
            print("Erro: Peso e altura devem ser valores positivos!\n")
            continue
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        
        historico_imcs.append(imc)
        historico_classificacoes.append(classificacao)
        
        print(f"IMC: {imc}")
        print(classificacao)
        
        continuar = input("\nDeseja continuar? (s/n): ").lower()
        if continuar != 's':
            break
    
    except ValueError:
        print("Erro: Insira valores válidos!\n")
 
media_imc = round(sum(historico_imcs) / len(historico_imcs), 2)
classificacao_frequente = max(set(historico_classificacoes), key=historico_classificacoes.count)
 
print("\n Histórico dE IMC")
print(f"Total de consultas: {len(historico_imcs)}")
print(f"Média de IMC: {media_imc}")
print(f"Classificação mais frequente: {classificacao_frequente}")