import re

nameFile = input("Ingrese el path del archivo a probar :0 : ")
currentTokenPosition = 0
currentToken = ""

def match(token):
    global currentTokenPosition
    global currentToken
    global vecTokenTypes
    global vecLexemes
    currentToken = vecTokenTypes[currentTokenPosition]
    messageErrorGeneric = f"Error sintáctico, la cadena {vecLexemes[currentTokenPosition]} de tipo <{currentToken}>"
    if currentToken == token:
        currentTokenPosition = currentTokenPosition + 1
        print(f"Token {token} consumido.\n")
    elif currentToken == "UNKNOWN":
        raise Exception(f"{messageErrorGeneric} desconocida esperaba un <{token}>.\n")
    else:
        raise Exception(f"{messageErrorGeneric} no corresponde al esperado token esperado <{token}>\n")


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

def validatePositionError(inputOriginal):
    inputByLines = inputOriginal
    row = 1
    lexemeIndex = 0

    for line in inputByLines:
        positionLine = 0  # Posición actual en la línea
        # Continuar mientras haya lexemas por encontrar y no se haya llegado al final de la línea
        while positionLine < len(line) and lexemeIndex < len(vecLexemes):
            lexeme = vecLexemes[lexemeIndex]

            col = line.find(lexeme, positionLine) # Buscar el lexema desde la posición actual en la línea
            if col != -1:
                # Si se encuentra el lexema, guardamos su posición (fila y columna)

                if lexeme == vecLexemes[currentTokenPosition]:
                    print(f'El lexema: "{lexeme}" encontrado en la linea {row}, columna {col + 1}')
                    break
                # Mover la posición actual a la posición después del lexema encontrado
                positionLine = col + len(lexeme)
                lexemeIndex += 1
            else:
                # Si no se encuentra el lexema, se pasa a la siguiente línea
                if vecTokenTypes[currentTokenPosition] == "UNKNOWN" and positionLine > 0:
                    print(f'Error sintáctico, en la linea {row} la cadena ingresada <{vecLexemes[currentTokenPosition]}> no es válida en la posición {positionLine}.')
                if line.strip() == "":
                    print("Se alcanzo el final de linea")
                    break
                break
        row += 1



try:
    # 0. Leer el contenido del archivo de la URL proporcionada
    f = open(nameFile, "r")
    inputStr = f.read()
    inputOriginal = inputStr.splitlines()
    finalLine = len(inputOriginal)


    # 1. Ahora se borran los signos espacio, tabulador y linea nueva de la entreada
    print("1) Se eliminan las espacios, tabuladores y linea nueva, quedando asi: \n")
    inputStr = re.sub(r"[\n\t\s]*", "", inputStr)
    print(inputStr)

    # 2. Ahora se agregan nuevos espacios, pero exclusivamente a partir de los ( y )
    print("2) Ahora se agregan nuevos espacios, pero exclusivamente a partir de los (, ; y ): \n")
    inputStr = re.sub(r"\(", " ( ", inputStr)
    inputStr = re.sub(r"\)", " ) ", inputStr)
    inputStr = re.sub(r";", " ; ", inputStr)
    inputStr = re.sub(r'\s+', ' ', inputStr).strip()
    print(inputStr)

    # 3. Ahora se realiza la clasificación de lexemas
    inputStr = inputStr.split(" ")

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
    for c in inputStr:
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

except IndexError as ex:
    print(f"Error sintáctico, en la linea {finalLine} la cadena ingresada no es válida, se esperaba un token <)> al final de la cadena.")
except Exception as exception:
    validatePositionError(inputOriginal)
    print(exception)




