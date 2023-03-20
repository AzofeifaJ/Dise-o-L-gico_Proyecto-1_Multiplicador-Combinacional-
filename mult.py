def mult(a,b):
  a=T_Binario(a);
  b=T_Binario(b);
  
  if verificar_Bits(a,b)==True:
    return multiplicacionBinaria(a,b) ###

  else:
    return verificar_Bits(a,b)  

def verificar_Bits(a,b):
  if len(a)>8:
    return "El valor <a> excede los 8 bits"
  elif len(b)>8:
    return "El valor <b> excede los 8 bits"
  else:
    return True
