import re

nameFile = "test_1.txt" # input("Ingrese el path del archivo a probar :D : ")
currentTokenPosition = 0
currentToken = ""


def match(token):
    global currentTokenPosition
    global currentToken
    global vecTokenTypes
    global vecLexemes
    currentToken = vecTokenTypes[currentTokenPosition]
    if currentToken == token:
        currentTokenPosition = currentTokenPosition + 1
        print(f"Token {token} consumido.\n")
    elif currentToken == "UNKNOWN":
        raise Exception("Error sintáctico, la cadena ingresada es desconocida.")
    else:
        raise Exception(
            "Error sintáctico, la cadena ingresada no corresponde al carácter esperado ó se esperaban datos adicionales.\n")


def person():
    match("number")
    match(";")
    match("str")
    match(";")
    match("str")
    match(";")
    match("email")
    match(";")


def persons():
    global currentTokenPosition
    global currentToken
    global vecTokenTypes
    currentToken = vecTokenTypes[currentTokenPosition]
    if currentToken == "number":
        person()
        persons()


# there is no else, because con be <persons> can be epsilon

def workgroup():
    match("WG")
    match("(")
    persons()
    match(")")


def workgroups():
    global currentTokenPosition
    global currentToken
    global vecTokenTypes
    currentToken = vecTokenTypes[currentTokenPosition]
    if currentToken == "WG":
        workgroup()
        workgroups()


# there is no else, because con be <workgroups> can be epsilon

def org():
    match("str")
    match("(")
    workgroups()
    match(")")


try:
    # 0. Leer el contenido del archivo de la URL proporcionada
    f = open(nameFile, "r")
    inputstr = f.read()

    # 1. Ahora se borran los signos espacio, tabulador y linea nueva de la entreada
    print("1) Se eliminan las espacios, tabuladores y linea nueva, quedando asi: \n")
    inputstr = re.sub(r"[\n\t\s]*", "", inputstr)
    print(inputstr)

    # 2. Ahora se agregan nuevos espacios, pero exclusivamente a partir de los ( y )
    print("2) Ahora se agregan nuevos espacios, pero exclusivamente a partir de los (, ; y ): \n")
    inputstr = re.sub(r"\(", " ( ", inputstr)
    inputstr = re.sub(r"\)", " ) ", inputstr)
    inputstr = re.sub(r";", " ; ", inputstr)
    inputstr = re.sub(r'\s+', ' ', inputstr).strip()
    print(inputstr)

    # 3. Ahora se realiza la clasificación de lexemas
    inputstr = inputstr.split(" ")
    print("La lista de posibles lexemas es: \n")
    print(inputstr)

    vecTokenTypes = []
    vecLexemes = []
    dic_directTokens = {'str': 'str',
                        '(': '(',
                        'WG': 'WG',
                        ')': ')',
                        'number': 'number',
                        'email': 'email',
                        ';': ';',
                        'UKNOWN': 'UNKNOWN'}
    for c in inputstr:
        r = dic_directTokens.get(c)
        if r:
            vecTokenTypes.append(r)
            vecLexemes.append(r)
        elif re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", c):
            vecTokenTypes.append('email')
            vecLexemes.append(c)
        elif re.match(r'^\".*\"$', c):
            vecTokenTypes.append('str')
            vecLexemes.append(c)
        elif re.match(r"^\d+$", c):
            vecTokenTypes.append('number')
            vecLexemes.append(c)
        else:
            vecTokenTypes.append('UNKNOWN')
            vecLexemes.append(c)

    print("\n\tTokentypes result:\n")
    print(vecTokenTypes)
    print("\n\tLexems result:\n")
    print(vecLexemes)

    # The syntax analize begin
    print("\nThe syntax analize\n")
    org()
    print("La cadena ingresada es valida sintácticamente.")
    f.close()

except Exception as exception:
    print(exception)




'''def validatePositionError(inputOriginal, vecLexemes):
    inputByLines = inputOriginal.splitlines()  # Se obtiene el contenido del archivo por lineas
    row = 1
    numberLexeme = len(vecLexemes)
    tokenRowColumn = []
    cont = 0
    for i in inputByLines:
        rowLength = len(i)
        colOffset = 0
        r = 0
        while (r < rowLength) and (cont < numberLexeme):
            col = i.find(vecLexemes[cont], colOffset)
            if col >= 0:
                tokenRowColumn.append([row, col + 1])
                print(f'Lexema: {vecLexemes[cont]} en la fila {row} ')
                print(f'Columna: {colOffset} ')
                cont = cont + 1
            r = r + 1'''