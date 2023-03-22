def T_Binario(a):
    if a[0] == "b": #Es notación binario?
        return a[1:]

    elif a[0] == "d": #Es notación decimal?
        
        numero_decimal=int(a[1:]) #Extraemos el número de la cadena
        binario = ""
    
        while numero_decimal != 0: # mientras el número de entrada sea diferente de cero
            modulo = numero_decimal % 2 
            cociente = numero_decimal // 2 
            modulostr = str(modulo) #transformamos el entero en string para poder contatenarlo
            binario = binario + modulostr #agregamos el bit a la cadena

            #modulos.append(str(modulostr)) # guardamos el módulo calculado
            numero_decimal = cociente # el cociente pasa a ser el número de entrada
        
        return binario[::-1]

    
    elif a[0] == "h": #Es notación hexadecimal?
        n = int(a[1:], 16) #Por medio de la biblioteca math transformamos el hexadecimal a decial
        return T_Binario("d"+str(n)) #Mandamos el número transformado a decial a ser convertido a binario a esta misma función

    else:       #Como no hay un identificador, asumimos como número decimal 
        return T_Binario("d"+a) #Mandamos el número transformado a decial a ser convertido a binario a esta misma función

