# Proyecto I: Multiplicador_Combinacional

![image](https://user-images.githubusercontent.com/111375712/195476581-b4a65f14-fa37-4b95-a1a7-ba00fbd7c58a.png)

### Instituto Tecnológico de Costa Rica
### EL 3307: Diseño Lógico
### Grupo 20
### Profesor: Ing. Kaleb Alfaro Badilla

### Integrantes
1. Azofeifa Jiménez Alonso
2. Luna Herrera José David
3. Vargas Arce Andrés
4. Víquez Sánchez Manfred

### I Semestre 2023


## Descripción general
En primer lugar es importante mencionar que los circuitos de lógica aritmética que los operadores que permiten realizar la operación de la multiplicación y lógicas básicas mediante circuitos combinacionales, como la suma, la resta y la multiplicación de números binarios, sin la necesidad de que exista la realimentación o el almacenamiento temporal de la información, estos los combierte en que sean fundamentales para el procesamiento de datos. En el caso del método de multiplicación binaria es un proceso de operación por sumas y desplazamientos, la multiplicación de los números binarios se realiza multiplicando el multiplicando con el multiplicador, en la cualexisten dos opciones en donde, la multiplicación por cero hace que todos los bits sean cero y la multiplicación por 1 hace que todo el valor del multiplicando no cambie, este proceso se tiene que continuar hasta que se haga todo el multiplicador, y finalmente, se hace la operación de suma, la cual tiene una implementación combinacional prácticamente directa realizando el mismo procedimiento algorítmico que la multiplicación en decimal.

![image](https://user-images.githubusercontent.com/111375712/226212475-083ccd67-8f55-4391-8ccd-a957bed57154.png)

Este proyecto consiste en el desarrollo de un circuito de multiplicación convinacional mediante la capacidad de implementarlos utilizando un lenguaje de programación por medio de Python, consta con la implementación de un módulo main de lectura del dato, un subsistema de transformación de base, además de un subsistema de multiplicación de dos números binarios, así como un subsistema con el objetivo de generar el PDF final en formato LaTeX con la respuesta de salida de la multiplicación binaria.


## Objetivo General del Proyecto
Introducir al estudiante en el tema de implementación de algoritmos que emulen sistemas digitales.

##  Objetivos Específicos del Proyecto
1. Estudiar la complejidad computacional del algoritmo que permite la multiplicación binaria.
2. Desarrollar una implementación de un multiplicador combinacional.
3. Coordinación de trabajo en equipo mediante el uso de herramientas de control de versiones.
4. Practicar planificación de tareas para trabajo de grupo.


## Descripción de cada subsistema
### Subsistema de implementación del módulo main
En este subsistema en primer lugar se verifica que los números ingresados a multiplicar sean binarios, además es el encargado de llamar a los demás módulos en caso de ser necesaria la transformación de la base para realizar la multiplicación.


### Subsistema de implementación del módulo transformación de base.
En este segundo subsistema se realiza la conversión de cualquier tipo de número que entre en hexadecimal o decimal a binario.

#### Imagen correspondiente a conversión binaria, decimal y hexadecimal:

![image](https://user-images.githubusercontent.com/111375712/226212630-6d80f40b-fe50-4083-84a3-27ddc4ee15d5.png)


### Subsistema de implementación del módulo Multiplicación Binaria.
En este tercer subsistema se realiza la multiplicación de dos números binarios con el fin de generar la salida de un solo número binario.

#### Imagen correspondiente a ejemplo de la multiplicación de los números binarios:

![image](https://user-images.githubusercontent.com/111375712/226212997-5fb46a29-348f-40d6-8916-df95b8c331eb.png)


### Subsistema de generación del PDF en formato LaTeX
En este cuarto subsistema se toman los datos del algoritmo de multiplicación en binario y se genera un archivo en estilo Beamer por medio de LaTeX, en donde se muestran 3 diapositivas, la primera diapositiva indica los valores que se leyeron en la entrada de usuario (operandos, cantidad de bits, nombre del archivo de configuración), las siguientes diapositivas demuestran el desarrollo completo de la multiplicación binaria y el resultado final y la última diapositiva la información de la institución, integrantes, curso, año y semestre.

## Diagramas de bloques de cada subsistema
A continuación se muestra un diagrama de bloques sobre el funcionamiento general del circuito multiplicador combinacional, así como un diagrama de bloques para cada subsistemas, con su funcionalidad descrita y su esquema de interconexión, además con el registro de entradas y salidas, sus diagramas de estado y las señales de control de cada bloque en la ruta de datos.

#### Funcionamiento general

![Image](https://user-images.githubusercontent.com/111375712/224883886-803199b0-54e4-436c-9e0a-a8afbbfcb0c8.png)

### Subsistema main.

![image](https://user-images.githubusercontent.com/111375712/227062212-3239d34b-e726-4925-9ac8-94e219ec6abb.png)


### Subsistema de implementación del módulo transformación de base.

![image](https://user-images.githubusercontent.com/111375712/226993424-433d17c1-0cb0-4a48-8727-85ceb56393e2.png)


#### Subsistema de implementación del módulo Multiplicación Binaria.

![image](https://user-images.githubusercontent.com/111375712/226993462-c8227218-78ff-42f7-9221-9168efd1acdf.png)




## Imágenes de la gereración del PDF final en formato LaTeX con la solución algoritmo de multiplicación binaria.

#### Diapositiva indica los valores que se leyeron en la entrada de usuario (operandos, cantidad de bits, nombre del archivo de configuración)

![image](https://user-images.githubusercontent.com/111375712/226993708-c6fa6828-d935-4097-9ddc-3636809c1946.png)


#### Diapositiva del desarrollo completo de la multiplicación binaria y el resultado final 

![image](https://user-images.githubusercontent.com/111375712/226993845-2ba1c402-90ee-42bf-9b29-3850335a70bf.png)


#### Diapositiva con la información general

![image](https://user-images.githubusercontent.com/111375712/226993998-3164cdee-7e59-4958-973c-35c2b8e7e6c8.png)


