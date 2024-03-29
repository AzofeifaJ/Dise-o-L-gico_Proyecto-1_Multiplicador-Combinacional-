import os

def generadorPDF(num1,num2,procedimiento):
    file = open("main.tex", "w")
    file.write(r"\documentclass[numbering=fraction]{beamer}")
    file.write("\n")
    file.write(r"\usepackage[utf8]{inputenc}")
    file.write("\n")
    file.write(r"\usepackage{blindtext}")
    file.write("\n")
    file.write(r"\usetheme[progressbar=frametitle]{metropolis}")
    file.write("\n")
    file.write(r"%Define colors")
    file.write("\n")
    file.write(r"\definecolor{wuppergreen}{RGB}{0, 43, 128}")
    file.write("\n")
    file.write(r"\definecolor{background}{RGB}{0,0,0}")
    file.write("\n")
    file.write(r"%Adjust color theme")
    file.write("\n")
    file.write(r"\setbeamercolor{frametitle}{bg=wuppergreen}")
    file.write("\n")
    file.write(r"\setbeamercolor{title separator}{fg=wuppergreen}")
    file.write("\n")
    file.write(r"\setbeamercolor{footline}{fg=gray}")
    file.write("\n")
    file.write(r"\setbeamercolor{progress bar}{fg=black}")
    file.write("\n")
    file.write(r"%Adding footer")
    file.write("\n")
    file.write(r"\setbeamertemplate{frame footer}{\insertshortauthor~(\insertshortinstitute)}")
    file.write("\n")
    file.write(r"\begin{document}")
    file.write("\n")
    file.write(r"%Primera diapositiva indica los valores que se leyeron en la entrada de usuario (operandos, cantidad de bits, nombre del archivo de configuración")
    file.write("\n")
    file.write(r"\begin{frame}{Implementacion con Multiplicador combinacional}")
    file.write("\n")                   
    file.write(r"   \begin{block}{Los valores de entrada que ingreso el usuario son :}")
    file.write("\n")
    file.write(num1+r"\\"+num2)
    file.write("\n")
    file.write(r"    \end{block}")
    file.write("\n")
    file.write(r"    \begin{block}{La cantidad de bits de los factores a multiplicar corresponde a :}")
    file.write("\n")                        
    file.write(r"        {Factor 1 : }"+str(len(procedimiento[0])))
    file.write("\n")
    file.write(r"        \\{Factor 2 : }"+str(len(procedimiento[1])))
    file.write("\n")
    file.write(r"    \end{block}")
    file.write("\n")
    file.write("\end{frame}")
    file.write("\n")                                                                                
    file.write(r"%Diapositivas del desarrollo completo de la multiplicación binaria y el resultado final.")
    file.write("\n")
    file.write(r"\begin{frame}{Desarrollo de la multiplicacion binaria}")
    file.write("\n")
    file.write(r"    \begin{block}{Proceso de la multiplicacion binaria}")
    file.write("\n")
    file.write(r"    \begin{center}"+procedimiento[0])
    file.write("\n")
    file.write(r"   \\x"+procedimiento[1])
    file.write("\n")
    file.write(r"   \\{---------------------------------------}\\")
    file.write("\n")
    fParciales=[]
    #Se separa los factores parciales y se reacomodan.
    for i in range(2,len(procedimiento)-1):
        fParciales.append(procedimiento[i])
        
    for j in range(len(fParciales)):
        if j==len(fParciales)-1:
            file.write(r"   +"+fParciales[j])
        else:
            for k in range(j,len(fParciales)+3):
                fParciales[j]="-"+fParciales[j]
            file.write(fParciales[j]+"\\\\")
    file.write("\n")
    file.write(r"\\{---------------------------------------}\\=  "+procedimiento[len(procedimiento)-1])
    file.write("\n")
    file.write(r"    \end{center}")
    file.write("\n")
    file.write(r"    \end{block}")
    file.write("\n")
    file.write(r"\end{frame}")
    file.write("\n")
    file.write(r"%Portada.")
    file.write("\n")
    file.write(r"\begin{frame}{Informacion}")
    file.write("\n")
    file.write(r"    \begin{block}{Instituto Tecnologico de Costa Rica}")
    file.write("\n")
    file.write(r"    \end{block}")
    file.write("\n")
    file.write(r"    \begin{block}{Estudiantes:\\}")
    file.write("\n")
    file.write(r"       Andres Vargas Arce\\Alonso Azofeifa Jimenez\\Jose David Luna Herrera\\Manfred Viquez Sanchez")
    file.write("\n")
    file.write(r"    \end{block}")
    file.write("\n")
    file.write(r"    \begin{block}{I Semestre}")
    file.write("\n")
    file.write(r"    \end{block}")
    file.write("\n")
    file.write(r"    \begin{block}{2023}")
    file.write("\n")
    file.write(r"    \end{block}")
    file.write("\n")
    file.write(r"\end{frame}")
    file.write("\n")

    file.write(r"\end{document}")

    file.close()

    os.system("pdfLaTex main.tex")

    return "multiplicacion Realizada"

