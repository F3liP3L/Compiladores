from pip._vendor.pygments.lexer import combined

codigoFuente = input()
prop = ['A','B','C','D','F','G']
operatorBin  = ['u','n']
operatorUni = ['~']
tiposToken = []
lexemas = []
for c in codigoFuente:
    print('Checking ', c)
    if c in prop:
        tiposToken.append('PROP')
        lexemas.append(c)
    elif c in operatorUni:
        tiposToken.append('OPUNI')
        lexemas.append(c)
    elif c in operatorBin:
        tiposToken.append("OPBIN")
        lexemas.append(c)
    else:
        tiposToken.append("UNKNOWN")
        lexemas.append(c)

print(tiposToken)
print(lexemas)

tiposTokenXcodigoToken = {'PROP':0,'OPUNI':1,'OPBIN':2, 'UNKNOWN':3}
estadoActual = 0
matrizDeEstados = [
    [3, 2, 1, 6], # q0
    [1, 1, 1, 1], # q1
    [3, 2, 2, 6], # q2
    [5, 2, 4, 6], # q3
    [3, 2, 4, 6], # q4
    [5, 5, 5, 5], # q5
    [6, 6, 6, 6]  # q6
    ]
matrizDeAceptacion = [3]
matrizDeRechazo = [0,1,2,4,5,6]
DiccionarioCodigosError = {0:"Es necesario ingresar un caracter", 1:"No se puede empezar por un operador de union o intersección", 2:"Se esperaba una proposición despues de la negación", 4:"Se esperaba una proposición despues de la unión o intersección", 5:"No se puede repetir una proposición", 6: "El caracter ingresado no pertenece a la expresión"}
cursorToken = 0
lastCharacter = ""
positionError = 0
for c in codigoFuente:
    codigoToken = tiposTokenXcodigoToken[tiposToken[cursorToken]]
    estadoActual=matrizDeEstados[estadoActual][codigoToken]
    '''print("Nuevo estado: ", estadoActual)
    print(c)
    print(codigoToken)'''
    cursorToken = cursorToken+1
    if estadoActual in matrizDeRechazo:
        lastCharacter = c
        positionError = cursorToken

if estadoActual in matrizDeAceptacion:
    print("El codigo es valido en lo sintactico")
else:
    if estadoActual in matrizDeRechazo:
        print("Error sintactico en el elemento", lastCharacter, "en la posicion ", positionError)
        print(DiccionarioCodigosError[estadoActual])