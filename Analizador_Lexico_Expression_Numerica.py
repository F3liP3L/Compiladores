codigoFuente = input()
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print("Longitud: ", len(numeros))
signos = ['+', '-']
tiposToken=[]
lexemas = []
for c in codigoFuente:
    print('Checking ', c)
    if c in numeros:
        tiposToken.append('NUM')
        lexemas.append(c)
    else:
        if c in signos:
            tiposToken.append('SIGN')
            lexemas.append(c)
        else:
            tiposToken.append("UNKNOWN")
            lexemas.append(c)


print("tiposToken: ", tiposToken)
print("lexemas: ", lexemas)


#Fase de analisis sintactico
#Diccionario tipo de token por codigo token
tiposTokenXcodigoToken = {'NUM':0,'SIGN':1,'UNKNOWN':2}
estadoActual = 0;
matrizDeEstados = [
    [2, 1, 6],
    [1, 1, 1],
    [5, 3, 6],
    [2, 4, 6],
    [4, 4, 4],
    [5, 5, 5],
    [6, 6, 6]
    ]
matrizEstadosAceptacion = [0, 2]
matrizEstadosRechazo = [1, 3, 4, 5, 6]
DiccionarioCodigosError = {1:"No se puede empezar por signo", 3:"Se esperaba un numero", 4:"Se esta repitiendo signo", 5:"Se esta repitiendo numero", 6:"Se encontro caracter invalido"}
cursorToken = 0
caracterError = ""
posicionError = 0
for c in codigoFuente:
    codigoToken = tiposTokenXcodigoToken[tiposToken[cursorToken]]
    estadoActual=matrizDeEstados[estadoActual][codigoToken]
    print("Nuevo estado: ", estadoActual)
    if estadoActual == 6:
        posicionError = cursorToken
        caracterError = c
        print('Error por el elemento ', c)
        break
    cursorToken = cursorToken+1

if estadoActual in matrizEstadosAceptacion:
    print("El codigo es valido en lo sintactico")
else:
    if estadoActual in matrizEstadosRechazo: # Mostrar estado donde se toteo, donde se mostro el primer error.
        print("Error sintactico en el caracter ", caracterError , " encontrado en la posicion ", posicionError)
        print(DiccionarioCodigosError[estadoActual])