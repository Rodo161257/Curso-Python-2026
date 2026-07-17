from random import sample

def generar_carton():
        return set(sample(range(1, 91), 15))

def estado_del_carton(carton, salientes):
        marcados = carton & salientes
        pendientes = carton - salientes
        
        print("_"*58)
        for n in carton:
            if n in salientes:
                print(n,"✓",sep="", end = " ")
            else:
                print(n, end = "  ")

        print()
        print("_"*58)
        print(f"Marcados: {len(marcados)}/15    |    Faltan: {len(pendientes)}")