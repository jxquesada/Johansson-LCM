datos= 'b -OL \r 5.39 \r'
datos2= '-O.04'
mostrar=datos2.split()
print(mostrar)
tam=len(mostrar)
if tam == 3:
    print(mostrar[2])
else:
    print(mostrar[0])