## Paso 1: crear el cartòn
## Paso 2: obtener un nùmero del bolillero
## Paso 3: chequear si el sorteo està en el cartòn. 
    # 3.1: Restar el nùmero sorteado al bolillero
    # 3.2: Si nùmero sorteado = nùmero cartòn, restar un nùmero a los 15 del cartòn
## Paso 4: Repetir paso 2 hasta completar cartòn, con el ùltimo nùmero BINGO
## Paso 5: Estadìsticas: con cuàntos sorteos complete el cartòn

import random
random.sample

carton = random.sample(range(1, 91), 15)

