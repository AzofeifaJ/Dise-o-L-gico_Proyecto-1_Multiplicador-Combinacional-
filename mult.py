from T_Binario import T_Binario
from multiplicacionBinaria import multiplicacionBinaria
####from LaTex import Latex
def mult(a,b):
  a=T_Binario(a);
  b=T_Binario(b);
  #Si los numeros a multiplicar cumplen con la 
  #cantidad de bits, se realiza la multiplicacion binaria
  if verificar_Bits(a,b)==True:
    return multiplicacionBinaria(a,b)
  else:
    return verificar_Bits(a,b)  
#Verifica que los numeros a multiplicar sean igual 
#o menos a 8 bits
def verificar_Bits(a,b):
  if len(a)>8:
    return "El valor <a> excede los 8 bits"
  elif len(b)>8:
    return "El valor <b> excede los 8 bits"
  else:
    return True
