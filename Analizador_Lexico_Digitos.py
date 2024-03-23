codigoFuente = input()
digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operatorBin  = ['+','-', '*','/']
operatorUni = ['L', 'E']

tiposToken = []
lexemas = []
for c in codigoFuente:
    if c in digitos:
        tiposToken.append('DIGITO')
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

print("tiposToken: ", tiposToken)
print("lexemas: ", lexemas)

tiposTokenXcodigoToken = {'DIGITO':0,'OPUNI':1,'OPBIN':2, 'UNKNOWN':3}

estadoActual = 0
matrizDeEstados = [
    [1, 2, 8, 3], # q0
    [6, 9, 4, 3], # q1
    [1, 7, 10, 3], # q2
    [3, 3, 3, 3], # q3
    [1, 2, 5, 3], # q4
    [5, 5, 5, 5], # q5
    [6, 6, 6, 6], # q6
    [7, 7, 7, 7], # q7
    [8, 8, 8, 8], # q8
    [9, 9, 9, 9],  # q9
    [10, 10, 10, 10]  # q11
    ]
estadosDeAceptacion = [1] # q1
estadosDeRechazo = [2, 4]
estadosErrorCritico = [3,5,6,7,8,9,10]

diccionarioCodigoError = {2:"Se esperaba una digito despues del operador unitario.",
                          3:"El caracter ingresado no pertenece a la expresión.", 5:"No se puede tener dos operadores binarios seguidos.",
                          4:"Se espera un digito o un operador unitario despues del operador binario.",
                          6:"No se puede tener dos digitos seguidos.", 7: "No se puede tener dos operadores unitarios seguidos.",
                          8:"No se puede empezar por un operador binario.", 9: "No se puede tener un operador unitario despues de un digito.",
                          10:"No se puede tener un operador binario despues de un operador unitario."}

cursorToken = 0
posicionError = 0 # Se cuenta desde la posicion 0
caracterError = ''
for c in codigoFuente:
    codigoToken = tiposTokenXcodigoToken[tiposToken[cursorToken]]
    estadoActual=matrizDeEstados[estadoActual][codigoToken]

    if estadoActual in estadosErrorCritico:
        caracterError = c
        posicionError = cursorToken
        break
    cursorToken = cursorToken+1

if estadoActual in estadosDeAceptacion:
    print("El codigo es válido en lo sintáctico.")
else:
    mensajeError = "Ha ocurrido un error sintáctico por el caracter {} en la posición {}"
    mensajeCodigoError = diccionarioCodigoError[estadoActual]
    if estadoActual in estadosErrorCritico:
        print("\t\n ERROR CRITICO! ")
        print(mensajeError.format(caracterError, posicionError))
        print(mensajeCodigoError)
    elif estadoActual in estadosDeRechazo:
        print("\t\n ERROR DE RECHAZO! ")
        posicionError = cursorToken - 1
        print(mensajeError.format(codigoFuente[posicionError], posicionError))
        print(mensajeCodigoError)