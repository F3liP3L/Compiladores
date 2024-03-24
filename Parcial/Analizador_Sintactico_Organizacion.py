import sys
import re

nombre_archivo = input("Ingrese el path del archivo a probar :D : ")
currentTokenPosition = 0
currentToken = ""

def match(token):
    global currentTokenPosition
    global currentToken
    global vecTokenTypes
    global vecLexems
    currentToken = vecTokenTypes[currentTokenPosition]
    print(vecLexems[currentTokenPosition])
    if currentToken == token:
        currentTokenPosition = currentTokenPosition + 1
        print(f"Token {token} consumido.\n")
    elif currentToken == "UNKNOWN":
        raise Exception("Error sintáctico, la cadena ingresada es desconocida.")
    else:
        raise Exception("Error sintáctico, la cadena ingresada no corresponde al carácter esperado ó se esperaban datos adicionales.\n")

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
    f = open(nombre_archivo, "r")
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
    vecLexems = []
    dic_directTokens = {'str': 'str',
                        '(': '(',
                        'WG': 'WG',
                        ')': ')',
                        'number': 'number',
                        'email': 'email',
                        ';': ';',
                        'UKNOWN':'UNKNOWN'}
    for c in inputstr:
        r = dic_directTokens.get(c)
        if r:
            vecTokenTypes.append(r)
            vecLexems.append(r)
        elif re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", c):
            vecTokenTypes.append('email')
            vecLexems.append(c)
        elif re.match(r'^\".*\"$', c):
            vecTokenTypes.append('str')
            vecLexems.append(c)
        elif re.match(r"^\d+$", c):
            vecTokenTypes.append('number')
            vecLexems.append(c)
        else:
            vecTokenTypes.append('UNKNOWN')
            vecLexems.append(c)

    print("\n\tTokentypes result:\n")
    print(vecTokenTypes)
    print("\n\tLexems result:\n")
    print(vecLexems)

    # The syntax analize begin
    print("\nThe syntax analize\n")
    org()
    print("La cadena ingresada es valida sintácticamente.")
    f.close()

except Exception as exception:
    print(exception)