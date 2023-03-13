def menuMultiplicador(a,b):
  a=T_Binario(a);
  b=T_Binario(b);
  
  if verificar_Bits(a,b)==True:
    return multi_Binaria(a,b)

  else:
    return verificar_Bits(a,b)

def verificar_Bits(a,b):
  if len(a)>8:
    return "El valor <a> excede los 8 bits"
  elif len(b)>8:
    return "El valor <b> excede los 8 bits"
  else:
    return True 

def T_Binaria(a):
  if a[0]=="d" or a[0]=="":
     return decimal_binario(a)
  elif a[0]=="h":
    return hexadecimal_binario(a)
  elif a[0]=="b":
    a=a[1:];
    return a
  else:
    return "Base incorrecta"

def decimal_binario(a):
  a=int(a[1:]);
  modulo=[];
  binario="";
  while a!=0:
    modulo.insert(0,a%2)
    a//=2;  
  for i in modulo:
    binario+=str(i);  
  return binario
