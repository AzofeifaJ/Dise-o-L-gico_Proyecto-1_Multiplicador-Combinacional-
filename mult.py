from T_Binario import T_Binario
from multiplicacionBinaria import multiplicacionBinaria
from generadorPDF import generadorPDF
import sys

def mult(a,b):
  aB=T_Binario(a);
  bB=T_Binario(b);
  #Si los numeros a multiplicar cumplen con la 
  #cantidad de bits, se realiza la multiplicacion binaria
  if verificar_Bits(aB,bB)==True:
    pasos=multiplicacionBinaria(aB,bB)
    return generadorPDF(a,b,pasos)
  else:
    return verificar_Bits(aB,bB)  
#Verifica que los numeros a multiplicar sean igual 
#o menos a 8 bits
def verificar_Bits(aB,bB):
  if len(aB)>8:
    return "El valor <a> excede los 8 bits"
  elif len(bB)>8:
    return "El valor <b> excede los 8 bits"
  else:
    return True
#Se lee entrada al sistema
args = sys.argv[1:]
if args[0] == "--bits":
    mult(args[3],args[5])
elif args[0] == "-f":
    file = open(args[1])
    linea = list(file.read())
    #Separamos el texto que entra en una lista para extraer los números a multiplicar
    listaAux = []
    stringAux = ""
    for i in linea:
      if i == " ":
        listaAux.append(stringAux)
        stringAux= ""
      else:
        stringAux = stringAux + i
    listaAux.append(stringAux)
    mult(listaAux[3],listaAux[5])
    file.close()

else:
  print("Comando no correcto")
