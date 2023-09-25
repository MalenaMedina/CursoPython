
#List Logones
logones = ["B959263", "C569853", "T698952", "Z698563"]

#List Roles
roles = ["SUPERIOR", "ADJUNTO", "TEMPORARIO", "TERCERIZADO"]

#List Contraseñas
contraseñas = ["CHIPI1971", "EURASIA", "JAJAJANT", "ECHENME"]

#Diccionario de tipo de acto

actosDisponiblesPorRol = {"SUPERIOR" : [1,3,4],
                          "ADJUNTO" : [1],
                          "TEMPORARIO" : [3,1],
                          "TERCERIZADO" : [1,5]}


# DEF USUARIO LOGADO
intentos = 0

def usuarioLogeado ():
    logonIngresado = input (" Ingrese su Logon:  ")
    global intentos
    if logonIngresado in logones: 
        print ("Logon válido")
        intentos = 0
        ingresoDeContraseña ()
    else :
        print ("Intente nuevamente, el logon \"{}\" no es valido".format(logonIngresado))
        intentos = intentos + 1
        if intentos > 2: 
            print ("Agotó el número de intentos permitidos")
        else:
            usuarioLogeado ()

#DEF INGRESO DE CONTRASEÑA

def ingresoDeContraseña ():
    contraseñaIngresada = input ("Ingrese su contraseña:  ")
    if contraseñaIngresada in contraseñas:
        print ("Contraseña correcta")
        ingresoDeRoles ()
    else : 
        print ("Intente nuevamente")
        global intentos
        intentos = intentos + 1
        if intentos > 2: 
            print ("Agotó el número de intentos disponibles")
        else:
            ingresoDeContraseña ()

#DEF ROLES 

def ingresoDeRoles () : 
    ingreseSuRol = input ("Ingrese su rol:  ")
    if ingreseSuRol in roles:
        print ("Rol reconocido")
        print (actosDisponiblesPorRol[ingreseSuRol])
    else : 
        print ("intente nuevamente")
        ingresoDeRoles ()

usuarioLogeado ()


