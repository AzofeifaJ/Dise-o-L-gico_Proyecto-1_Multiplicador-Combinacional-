def multiplicacionBinaria(num1,num2):
  #Se obtienen los factores
  PDF=[]
  PDF.append(num1)
  PDF.append(num2) 
  #Se obtiene los productos parciales
  newNum2=num2[::-1]
  for i in range(len(num2)):
    productoParcial=""
    for j in range(len(num1)):
      multiplicacion=int(num1[j])*int(newNum2[i])      
      productoParcial=productoParcial+str(multiplicacion)
    PDF.append(productoParcial) 
  #Se obtiene el producto final 
  multiplicar=int(num1,2)*int(num2,2);
  multiBinario=bin(multiplicar)
  multiBinario=multiBinario[2:]
  PDF.append(multiBinario)
  return PDF
