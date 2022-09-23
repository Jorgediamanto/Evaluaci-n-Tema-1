import math

class Punto:
    def __init__(self,X,Y):
        
        if X and Y == None:
            X = 0
            Y = 0

        else:
            self.X = X
            self.Y = Y

    def __str__(self):
        cadena="("+str(self.X)+","+str(self.Y)+")"
        return cadena

    def cuadrante(self):
        if self.X == 0 and self.Y != 0:
            print("Esta sobre el eje Y")

        if self.X != 0 and self.Y == 0:
            print("Esta sobre el eje X")

        if self.X == 0 and self.Y == 0:
            print("Esta sobre el origen de coordenadas")

        if self.X > 0 and self.Y > 0:
            print("Esta en el primer cuadrante")

        if self.X > 0 and self.Y < 0:
            print("Esta en el cuarto cuadrante")

        if self.X < 0 and self.Y > 0:
            print("Esta en el segundo cuadrante")

        if self.X < 0 and self.Y < 0:
            print("Esta en el tercer cuadrante")

    
    def vector(self,punto2):
        
        vector1 = Punto(punto2.X-self.X,punto2.Y-self.Y)

        print("Vector resultante entre el los dos puntos:"+ str(vector1))

    def distancia(self,punto2):
        distancia = abs(math.sqrt((self.X-punto2.X)**2+(self.Y-punto2.Y)**2))
        print("La distancia entre los dos puntos es de "+str(distancia))

    def distancia1(self,punto2):
        distancia = abs(math.sqrt((self.X-punto2.X)**2+(self.Y-punto2.Y)**2))
        return distancia        

class Rectangulo:
    def __init__(self,inicial,final):
        if inicial and final == None:
            inicial = Punto(0,0)
            final = Punto(0,0)

        else:
            self.inicial = Punto(inicial.X,inicial.Y)
            self.final = Punto(final.X,final.Y)

    
    def base(self):
        base = abs(self.inicial.X-self.final.X)
        print("Base del rectangulo tiene una distancia de "+str(base))
        if(self.inicial.Y<self.final.Y):
            print("Y va del punto ("+str(self.inicial.X)+","+str(self.inicial.Y)+") hasta el punto ("+str(self.final.X)+","+str(self.final.Y-self.altura1())+")")

        if(self.inicial.Y>self.final.Y):
            print("Y va del punto ("+str(self.inicial.X)+","+str(self.inicial.Y-self.altura1())+") hasta el punto ("+str(self.final.X)+","+str(self.final.Y)+")")
    
    
    def altura(self):
        altura = abs(self.inicial.Y-self.final.Y)
        print("Altura del rectangulo tiene una distancia de "+str(altura))



    def altura1(self):
        altura = abs(self.inicial.Y-self.final.Y)
        return altura


    def base1(self):
        base = abs(self.inicial.X-self.final.X)
        return base



    def area(self):
        area = self.base1()*self.altura1()
        print("El area del rectángulo es de "+ str(area))



A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)

print(A)
print(B)
print(C)
print(D)

A.cuadrante()
B.cuadrante()
C.cuadrante()
D.cuadrante()


A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)

x = A.distancia1(D)

if B.distancia1(D)>x:
    x=B.distancia1(D)

if C.distancia1(D)>x:
    x=C.distancia1(D)

if x == A.distancia1(D):
    print("El punto más lejano al origen es el A")

if x == B.distancia1(D):
    print("El punto más lejano al origen es el B")

if x == C.distancia1(D):
    print("El punto más lejano al origen es el C")


rectangulo1 = Rectangulo(A,B)

rectangulo1.altura()
rectangulo1.base()
rectangulo1.area()
