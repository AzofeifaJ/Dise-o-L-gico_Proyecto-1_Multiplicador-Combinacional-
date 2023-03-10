# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 15:21:19 2023

@author: José David
"""


#Biblioteca
import copy
from pylatex import Document, LongTable, Section, Command, NewPage
from pylatex.utils import bold, NoEscape





geometry_options = {"tmargin": "1cm", "lmargin": "1cm", "margin": "1cm"}
    doc = Document(page_numbers=True, geometry_options=geometry_options, documentclass="beamer",)




#Creación de la primera diapositiva con los valores de entrada.
def ():
    with doc.create(Section('')):
        doc.append(bold(''))
        doc.append('')
        doc.append(literal)
        doc.append('\n')
        doc.append('\n')
        for indice, min in enumerate():
            doc.append()
           
                doc.append(', ')
        doc.append('\n')
    doc.append(NewPage())

#Creación de la segunda diapositiva con el desarrollo completo de la multiplicación binaria y la solución final.
def ():
    with doc.create(Section('')):
        doc.append(bold(''))
        with doc.create(LongTable("c c")) as data_table:
            encabezado = []
            data_table.add_row()
            data_table.add_hline()
            data_table.end_table_header()

            for indice in range(len()):
                fila = []
                data_table.add_row(fila)
            data_table.add_hline()

    doc.append(NewPage())


#Crea una tabla con los minterminos agrupados según la cantidad de unos que poseen.
def ():
    with doc.create(Section('')):
        doc.append(bold(''))
        with doc.create(LongTable("c c c")) as data_table:
            encabezado = []
            data_table.add_row()
            data_table.add_hline()
            data_table.end_table_header()


    doc.append(NewPage())

#Creación de tablas
def ():
    with doc.create(Section()):
        doc.append(bold())
        with doc.create(LongTable("c c")) as data_table:
            encabezado = []
            data_table.add_row()
            data_table.add_hline()
            data_table.end_table_header()

    doc.append(NewPage())


            
            for indice, implicante in enumerate():
                    fila = []
                    data_table.add_row(fila)
            data_table.add_hline()

    doc.append(NewPage())

#Crea una diapositiva con la solucion del algoritmo.
def solucion():
    with doc.create(Section("Solución")):
         doc.append(bold("Solución\n"))
         doc.append('\nSimplificacion obtenida: ')
         doc.append('\n')
         

    doc.append(NewPage())



#Creción de la tercera diapositiva con la información general.
def portada(doc):
    with doc.create(Section('Portada')):
        doc.preamble.append(Command('titulo', 'Implementacion de un multiplicador
combinacional'))
        doc.preamble.append(Command('instituto', 'Instituto Tecnologico de Costa Rica'))
        doc.preamble.append(Command('autores', 'Alonso Azofeifa Jimenez \n Andres Vargas Arce\n Jose David Luna Herrera \n Manfred Viquez Sanchez'))
        doc.preamble.append(Command('date', NoEscape(r'\today')))
        doc.preamble.append(Command('semestre', 'I Semestre')))
        doc.append(NoEscape(r'\maketitle'))



#Creación del documento pdf resultante.
def creacion_documento(doc):
    doc.generate_pdf('', clean_tex=False, clean=True)