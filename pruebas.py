
def secuencia():
    import time
    anguloObjetivo = 160
    Relacion = 70/17
    stepAngular = 0.9
    # for i in range(10):
    #     print (i)
    Start = time.time()
    End = Start
    for i in range (int(anguloObjetivo*Relacion/stepAngular+1)+20):
        if i > anguloObjetivo*Relacion/stepAngular-10:
            print (round(End-Start, 2),",",round(int(anguloObjetivo*Relacion/stepAngular-10)*stepAngular/Relacion, 2),",",anguloObjetivo)
        else: print(round(End-Start, 2),",",round(i*stepAngular/Relacion, 2),",",360)
        time.sleep(0.01)
        End = time.time()

import random

print(round(random.uniform(0.10,0.24),2))