def multiplicar(num1, num2):
     resultado=0
     x=0
     sum=[]
     acumulador=0
     #si el valor del primer binario y el valor del segundo binario
     #no son cero, procede a obtener el resultado de multiplicación entre ambos
     while num1!=0 or num2!=0:
         sum.insert(x,(((num1 % 10)+(num2%10)+acumulador)%2))
         acumulador=int(((num1 % 10)+(num2%10)+acumulador)/2)
         num1=int(num1/10)
         num2=int(num2/10)
         x=x+1
     #siempre que el acumulador no sea igual
     #a cero lo almacena en una matriz para su posterior suma
     if acumulador!=0:
         sum.insert(x,acumulador)
         x=x+1
     x=x-1
     while x>=0:
         resultado=(resultado*10)+sum[x]
         x=x-1
     return resultado
def binarios(b1,b2):
     multiplicador=0
     factor=1
#Ahora se procede a hacer lectura del segundo num.binario
#para saber si posee un digito o si termina y así seguir multiplicando
#los digitos que encuentre con el primer binario hasta que recorra por
#completo ambos números
     while b2 != 0:
         digit=b2%10
         if digit==1:
             b1=b1*factor
             multiplicador=multiplicar(b1,multiplicador)
         else:
             b1=b1*factor
         b2=int(b2/10)
         factor=10
     print("\nEl resultado de la multiplicación es= " + str(multiplicador))
