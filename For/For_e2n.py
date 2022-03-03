N= int(input("Ingrese calificaciones:"))
suma=0
for i in range(N):
    nota=int(input("Ingrese su nota:"))
    suma= suma+nota

print("Suma total:", suma)
media_aritmetica =suma/N
print("Media aritmetica:", media_aritmetica)

if nota<7:
    print ('su nota es baja', media_aritmetica)