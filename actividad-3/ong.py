def factorial(numero):
    if numero <= 1:
        return 1
    return numero * factorial(numero - 1)
    
    
def productoria(numeros=[]):
    pass

if __name__ == "__main__":
    print(factorial(5))