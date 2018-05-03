num='0 1 2 3 4 5 6 7 8 9 10,11,12,13,14,15,16,17,18,19,20,21,22'
letras='T R W A G M Y F P D X B N J Z S Q V H L C K E'


sms=' 0,2,3,4,1,3 '
x=num.split()
y=letras.split()
z=sms.split()

fin=[y,num]

for w in num:
    codigo=str(letras.find(w))

def creartxt():
    file=open('3.txt','w')
    file.close()

def grabar():
    file=open('3.txt','a')
    file.write(codigo)
    file.close()

creartxt()
grabar()

