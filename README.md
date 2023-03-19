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

En el mundo de la electrónica digital, los circuitos de lógica aritmética son fundamentales para el procesamiento
de datos. Estos circuitos son capaces de realizar operaciones aritméticas y lógicas básicas, tales como
la suma, la resta y la multiplicación de números binarios. En particular, los multiplicadores combinacionales
son circuitos que realizan la multiplicación de dos números de entrada sin la necesidad de almacenamiento
temporal.
Este proyecto tiene como objetivo brindar a los estudiantes una comprensión profunda de los circuitos
digitales combinacionales y la capacidad de implementarlos utilizando un lenguaje de programación. Además,
con este proyecto se pretende dar un acercamiento al uso de sistemas de control de versiones.
Este proyecto consiste en el desarrollo de un circuito decodificador de Gray mediante utilización de Verilog y el suit de herramintas de Vivado, así como la implementación de diseño digital en una FPGA en este caso una NEXYS 4 ddr para demostrar su funcionamiento, este proyecto consta de un subsistema de lectura y decodificación de código Gray además de un subsistema de despliegue de código ingresado traducido a formato binario en luces LED y así como un subsistema de despliegue de código ingresado y decodificado en display de 7 segmentos.

## Descripción de cada subsistema
### Subsistema de lectura y decodificación de código Gray
En este primer subsistema el programa traduce la entrada de cuatro conmutadores en código gray a formato del código binario. La entrada del código es capturada y sincronizada con el sistema principal, para que posterior se realice un muestreo de estos con una duración de al menos cada 500 ms. Como se muestra en la imagen a continuación sobre la implementación y la correcta trasformación del Código Binario de 4 bits a partir de un Código de Gray necesario al llevar a cabo este circuito para mostrar un numero final decimal.

#### Imagen correspondiente al Código Gray de 4 bits

![image](https://user-images.githubusercontent.com/111375712/194989182-d70d0202-ddf0-42c4-a5aa-75aeaf40c07f.png)


### Subsistema de despliegue de código ingresado traducido a formato binario en luces LED
En este segundo subsistema se toma los datos ya pasados a código binario y los despliega en cuatro luces LED, además en esta sección se presenta el refrescamiento de las luces al menos cada 500 ms por parte sistema, en esta sección es importante mencionar que en cuanto al funcionamiento del LED la corriente siempre fluye de ánodo a cátodo, en el cual el ánodo se conecta al voltaje positivo de la fuente y el cátodo se conecta a tierra o al voltaje negativo de la fuente, representado en la siguiente imagen.

#### Imagen correspondiente al encendido de LEDs en NEXYS 4 ddr

![image](https://user-images.githubusercontent.com/111375712/194989319-14fcad98-e482-48d3-ba70-ff9cf3102c89.png)




### Subsistema de despliegue de código decodificado en display de 7 segmentos.
En este tercer subsistema tiene la tasa de refresco para la adecuada visualización, se toma los datos en código binario anteriormente ralizado y se procede a desplegar los dispositivos 7 segmentos disponibles, para realziar esta parte es importante mencionar la conexión de los pines a la FPGA de la NEXYS4 ddr la cual es necesaria para asignar el valor al encendido de los 7 segmentos numerados de A a G según corresponda para mostrar cada determinado valor, como se muestra en la imagen a continuación: 

#### Imagen de la distribución de los componentes en la NEXYS 4 ddr
![image](https://user-images.githubusercontent.com/111375712/195011801-afe0480f-6058-425c-bd41-d2c9452f1d77.png)

#### Imagen de la distribución de pines del display de 7 segmentos
![image](https://user-images.githubusercontent.com/111375712/194989472-a5276744-b65a-47e5-b6a7-da2e06bcdfcc.png)


Es importante mencionar que a continuación se muestra la programación realizada en Verilog sobre la distribución de los  los pines display de 7 segmentos.

```SystemVerilog
 
set_property IOSTANDARD LVCMOS33 [get_ports {a_to_g[6]}]
set_property IOSTANDARD LVCMOS33 [get_ports {a_to_g[5]}]
set_property IOSTANDARD LVCMOS33 [get_ports {a_to_g[4]}]
set_property IOSTANDARD LVCMOS33 [get_ports {a_to_g[3]}]
set_property IOSTANDARD LVCMOS33 [get_ports {a_to_g[2]}]
set_property IOSTANDARD LVCMOS33 [get_ports {a_to_g[1]}]
set_property IOSTANDARD LVCMOS33 [get_ports {a_to_g[0]}]
set_property IOSTANDARD LVCMOS33 [get_ports {an[7]}]
set_property IOSTANDARD LVCMOS33 [get_ports {an[6]}]
set_property IOSTANDARD LVCMOS33 [get_ports {an[5]}]
set_property IOSTANDARD LVCMOS33 [get_ports {an[4]}]
set_property IOSTANDARD LVCMOS33 [get_ports {an[3]}]
set_property IOSTANDARD LVCMOS33 [get_ports {an[2]}]
set_property IOSTANDARD LVCMOS33 [get_ports {an[1]}]
set_property IOSTANDARD LVCMOS33 [get_ports {an[0]}]
set_property IOSTANDARD LVCMOS33 [get_ports {sw[3]}]
set_property IOSTANDARD LVCMOS33 [get_ports {sw[2]}]
set_property IOSTANDARD LVCMOS33 [get_ports {sw[1]}]
set_property IOSTANDARD LVCMOS33 [get_ports {sw[0]}]
set_property IOSTANDARD LVCMOS33 [get_ports dp]
set_property PACKAGE_PIN J15 [get_ports {sw[0]}]
set_property PACKAGE_PIN L16 [get_ports {sw[1]}]
set_property PACKAGE_PIN M13 [get_ports {sw[2]}]
set_property PACKAGE_PIN R15 [get_ports {sw[3]}]
set_property PACKAGE_PIN H15 [get_ports dp]
set_property PACKAGE_PIN T10 [get_ports {a_to_g[0]}]
set_property PACKAGE_PIN R10 [get_ports {a_to_g[1]}]
set_property PACKAGE_PIN K16 [get_ports {a_to_g[2]}]
set_property PACKAGE_PIN K13 [get_ports {a_to_g[3]}]
set_property PACKAGE_PIN P15 [get_ports {a_to_g[4]}]
set_property PACKAGE_PIN T11 [get_ports {a_to_g[5]}]
set_property PACKAGE_PIN L18 [get_ports {a_to_g[6]}]
set_property PACKAGE_PIN J17 [get_ports {an[0]}]
set_property PACKAGE_PIN J18 [get_ports {an[1]}]
set_property PACKAGE_PIN T9 [get_ports {an[2]}]
set_property PACKAGE_PIN J14 [get_ports {an[3]}]
set_property PACKAGE_PIN P14 [get_ports {an[4]}]
set_property PACKAGE_PIN T14 [get_ports {an[5]}]
set_property PACKAGE_PIN K2 [get_ports {an[6]}]
set_property PACKAGE_PIN U13 [get_ports {an[7]}]
```

## Diagramas de bloques de cada subsistema
A continuación se muestra un diagrama de bloques sobre el funcionamiento general del circuito decodificador de Gray, así como un diagrama de bloques para cada subsistema de lectura, con su funcionalidad descrita y su esquema de interconexión, además con el registro de entradas y salidas, sus diagramas de estado y las señales de control de cada bloque en la ruta de datos.

#### Funcionamiento general

![image](https://user-images.githubusercontent.com/111375712/195467262-3b9fc74c-599e-490e-a949-47ed4cb39ac9.png)


#### Subsistema de lectura y decodificación de código Gray.

![image](https://user-images.githubusercontent.com/111375712/195467288-3398b559-5165-4557-b938-326489b88016.png)


#### Subsistema de despliegue de código ingresado traducido a formato binario en luces LED.

![image](https://user-images.githubusercontent.com/111375712/195004091-9a39c866-c90d-4a22-a132-96d8fb429332.png)


#### Subsistema de despliegue de código decodificado en display de 7 segmentos.

![image](https://user-images.githubusercontent.com/111375712/195007538-0d8286cc-44f5-4b85-9f63-f9e1a2d8750e.png)


## Simulación funcional del sistema completo

Realización de las pre-síntesis, mediante la simulaciones a nivel de RTL.
En esta sección se puede detallar las comprobaciones realizadas de los sistemas sobre la NEXYS 4 ddr, las cuales se realizaron por medio de videollamadas entre los integrantes del grupo para observar y realizar el correcto funcionamiento del circuito.

#### Sesiones realizadas entre los integrantes del grupo para visualizar el procedimiento realizado en Verilog para NEXYS 4

![image](https://user-images.githubusercontent.com/111375712/194734261-98dcac3d-816e-41a6-911a-89448dc3df1c.png)


#### Utilización de Verilog para NEXYS 4

![image](https://user-images.githubusercontent.com/111375712/194734288-56ff2af4-d5b1-48fe-a763-d41032d04a6e.png)

![image](https://user-images.githubusercontent.com/111375712/194966269-b75db593-a7e6-476a-a9e0-6353bafa2141.png)




## Análisis de consumo de recursos en la FPGA (LUTs, FFs, etc.) y del consumo de potencia que reporta la herramienta Vivado.

![image](https://user-images.githubusercontent.com/111375712/195476539-44c1bf45-9369-4990-a285-8e7ea8d7cbd1.png)


## Problemas hallados durante el trabajo
Durante el presente trabajo se generaron una serie de problemas desde su inicio, los cuales se detallan a continuación: el primer inconveniente se generó al realizar la instalación del programa de Vivado ya que no se pudo utilizar el correo institucional, el problema se solucionó al utilizar el correo personal. Otro inconveniente encontrado fue aprender la correcta utilización de la aplicación Vivado, ya que se encontraban una limitación en cuanto a la cantidad de contenido. Por otro lado, un siguiente problema se produjo durante la codificación de dos subsistemas, lo cuales correspondieron al subsistema de lectura y decodificación del codigo de Gray y el refrescamiento de las luces al menos cada 500 ms dentro del despliegue de código ingresado traducido a formato binario en luces LED el inconveniente se presentó con la correcta implementación del subsistema, este requirió una mayor inversión de tiempo por parte de los estudiantes, mediante la investigación y la recolección de información para poder realizarse, además se logró solucionar con la ayuda del profesor durante la reunión realizada en la verificación del avance y el cumplimiento del plan de trabajo del proyecto.
