
cadena=[1,1,0,1,0,1]

x=str(cadena)

pos1=cadena[0]*pow(2,5)
pos2=cadena[1]*pow(2,4)
pos3=cadena[2]*pow(2,3)
pos4=cadena[3]*pow(2,2)
pos5=cadena[4]*pow(2,1)
pos6=cadena[5]*pow(2,0)

res=str(pos1+pos2+pos3+pos4+pos5+pos6)

def creartxt():
    file=open('1.txt','w')
    file.close()

def grabar():
    file=open('1.txt','a')
    file.write('Binario: ')
    file.write(x)
    file.write('\nen Decimal: ')
    file.write(res)
    file.close()

creartxt()
grabar()
