import time

def eldecorador(lafuncion):
    def wrapper():
        print(f"Ejecutando {lafuncion.__name__}")
        lafuncion()
        print("Terminado")
        time.sleep(2.5)
    return wrapper

@eldecorador
def hace1():
    print("Hacer funcion 1")
    
@eldecorador
def hace2():
    print("Hacer funcion 2")
    
hace2()
hace1()