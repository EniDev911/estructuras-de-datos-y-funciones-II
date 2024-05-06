def factorial(numero):
    if numero <= 1:
        return 1
    return numero * factorial(numero - 1)
    
    
def productoria(numeros=[]):
    resultado = 1
    for num in numeros:
        resultado = resultado * num
    return resultado

def calcular(**kargs):

    for k, v in kargs.items():
        if k.startswith("fact"):
            print(f"El factorial de {v} es {factorial(v)}")
        elif 'prod_' in k:
            print(f"La productoria de {v} es {productoria(v)}")
        else:
            print("Acción no disponible")
            
if __name__ == "__main__":
    calcular(fact_1 = 5, prod_1 = [4, 6, 7, 4, 3], fact_2 = 6)