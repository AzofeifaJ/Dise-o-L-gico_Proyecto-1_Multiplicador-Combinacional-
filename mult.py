from T_Binario import T_Binario
from multiplicacionBinaria import multiplicacionBinaria
from generadorPDF import generadorPDF
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
