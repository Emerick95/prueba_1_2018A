cadena='Programacion Avanzada'
cadena.split()

pos19=cadena[19]
pos18=cadena[18]
pos17=cadena[17]
pos16=cadena[16]
pos15=cadena[15]
pos14=cadena[14]
pos13=cadena[13]
pos12=cadena[12]
pos11=cadena[11]
pos10=cadena[10]
pos9=cadena[9]
pos8=cadena[8]
pos7=cadena[7]
pos6=cadena[6]
pos5=cadena[5]
pos4=cadena[4]
pos3=cadena[3]
pos2=cadena[2]
pos1=cadena[1]
pos0=cadena[0]

codificado=str((pos19,pos18,pos17,pos16,pos15,pos14,pos13,pos12,pos11,pos10,pos9,pos8,pos7,pos6,pos5,pos4,pos3,pos2,pos1,pos0))

def creartxt():
    file=open('2.txt','w')
    file.close()

def grabar():
    file=open('2.txt','a')
    file.write('Cadena normal: ')
    file.write(cadena)
    file.write('\nCadena invertida: ')
    file.write(codificado)
    file.close()

creartxt()
grabar()
