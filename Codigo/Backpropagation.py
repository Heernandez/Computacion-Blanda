# Backpropagation Neural Networks
import math, random

# Derivada de la funcion de activacion
def DerivadaFA(y):
    return 1.0 - y**2

# Funcion de activacion, se descoge la Tangente Hiperbolica porque es mejor que la Sigmoid, 1/(1+e^-x)
def FuncionActivacion(x):
    return math.tanh(x)

# Crear Matriz
def CrearMatriz(i, j):
    m = []
    for x in range(i):
        m.append([0.0]*j)
    return m
#Implementacion de la clase RedNeuronal
class RedNeuronal:
    def __init__(self, ni, nh, no,ri):
        # Numero de nodos de capa entradas, capa oculta, capa de salida
        self.ni = ni + 1 # +1 para el bias
        self.nh = nh
        self.no = no
        self.riesgo=ri
        #Variables
        self.ai = [1.0]*self.ni
        self.ah = [1.0]*self.nh
        self.ao = [1.0]*self.no

        # Crear matriz de pesos y asignar valores aleatorios
        self.wi = CrearMatriz(self.ni, self.nh)
        self.wo = CrearMatriz(self.nh, self.no)

        for i in range(self.ni):
            for j in range(self.nh):
                self.wi[i][j] = random.uniform(-0.1,0.1)
        for j in range(self.nh):
            for k in range(self.no):
                self.wo[j][k] = random.uniform(-0.1,0.1)

    def update(self, inputs):
        # Asigna las  entradas a la variable ai
        for i in range(self.ni-1):
            self.ai[i] = inputs[i]

        # Sumatoria de entradas * pesos, Activacion de la capa oculta
        for j in range(self.nh):
            sum = 0.0
            for i in range(self.ni):
                sum = sum + self.ai[i] * self.wi[i][j]
            self.ah[j] = FuncionActivacion(sum)

        # Sumatoria de entradas * pesos, Activacion de la capa salida
        for k in range(self.no):
            sum = 0.0
            for j in range(self.nh):
                sum = sum + self.ah[j] * self.wo[j][k]
            self.ao[k] = FuncionActivacion(sum)

        return self.ao

    def Backpropagation(self, outputs, N):
        # calcular errores en la capa de salida
        output_deltas = [0.0] * self.no
        for k in range(self.no):
            error = outputs[k]-self.ao[k]
            output_deltas[k] = DerivadaFA(self.ao[k]) * error

        # calcular errores en la capa oculta
        hidden_deltas = [0.0] * self.nh
        for j in range(self.nh):
            error = 0.0
            for k in range(self.no):
                error = error + output_deltas[k]*self.wo[j][k]
            hidden_deltas[j] = DerivadaFA(self.ah[j]) * error

        # Actualizar los pesos de la capa de salida
        for j in range(self.nh):
            for k in range(self.no):
                change = output_deltas[k]*self.ah[j]
                self.wo[j][k] = self.wo[j][k] + N*change

       # Actualizar los pesos de la capa de entrada
        for i in range(self.ni):
            for j in range(self.nh):
                change = hidden_deltas[j]*self.ai[i]
                self.wi[i][j] = self.wi[i][j] + N*change

        return error

    def Resultado(self):
        patron = entrance(self.riesgo)
        for p in patron:
            salida=self.update(p[0])
            aux1,aux2=[],[]
            for x in salida:
                aux1.append(format(x,".5f"))
                aux2.append(int(round(x)))
            salida = 0
            if aux2[0]==0 and aux2[1]==0:
                salida=0
            elif aux2[0]==0 and aux2[1]==1:
                salida=1
            elif aux2[0]==1 and aux2[1]==0:
                salida=2
            elif aux2[0]==1 and aux2[1]==1:
                salida
            return salida

    def Entrenamiento(self, patron, iteraciones=100, N=0.169):
        # N: Tasa de Aprendizaje
        for i in range(iteraciones):
            error = 0.0
            for p in patron:
                inputs = p[0]
                outputs = p[1]
                self.update(inputs)
                error = error + self.Backpropagation(outputs, N)

def entrance(riesgo):
    e=Binario(riesgo)
    d=[0,0,0,0]
    entrada=[[[e[0],e[1],e[2],e[3],e[4],e[5],e[6],d[0],d[1],d[2],d[3]],[0,0]]]
    return entrada
def Binario(decimal):
    binario = ''
    entrada=0
    riesgo_bin=[]
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2

    if len(str(decimal) + binario) == 7:
        entrada = str(decimal) + binario
    elif len(str(decimal) + binario) == 6:
        entrada =  "0" + str(decimal) + binario
    elif len(str(decimal) + binario) == 5:
        entrada = "00" + str(decimal) + binario
    elif len(str(decimal) + binario) == 4:
        entrada = "000" + str(decimal) + binario
    elif len(str(decimal) + binario) == 3:
        entrada = "0000" + str(decimal) + binario
    elif len(str(decimal) + binario) == 2:
        entrada = "00000" + str(decimal) + binario
    elif len(str(decimal) + binario) == 1:
        entrada = "000000" + str(decimal) + binario

    for x in entrada:
        riesgo_bin.append(int(x))

    return riesgo_bin

def crear_patron():
    d1 =[0,0,0,0]
    d2 =[0,0,0,1]
    d3 =[0,0,1,0]
    d4 =[0,0,1,1]
    d5 =[0,1,0,0]
    d6 =[0,1,0,1]
    d7 =[0,1,1,0]
    d8 =[0,1,1,1]
    d9 =[1,0,0,0]
    d10=[1,0,0,1]
    d11=[1,0,1,0]
    d12=[1,0,1,1]
    d13=[1,1,0,0]
    d14=[1,1,0,1]
    d15=[1,1,1,0]
    d16=[1,1,1,1]
    patron=[]
    r=0
    for x in xrange(101):
        r=Binario(x)
        if x>=0 and x<=32:
            patron.append([[r[0],r[1],r[2],r[3],r[4],r[5],r[6],d1[0],d1[1],d1[2],d1[3]],[0,1]])
        elif x>=33 and x<=64:
            patron.append([[r[0],r[1],r[2],r[3],r[4],r[5],r[6],d1[0],d1[1],d1[2],d1[3]],[1,0]])
        elif x>=65 and x<=100:
            patron.append([[r[0],r[1],r[2],r[3],r[4],r[5],r[6],d1[0],d1[1],d1[2],d1[3]],[1,1]])
    return patron
