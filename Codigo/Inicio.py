#!/usr/bin/env python
# -*- coding: utf-8 -*-
from LogicaDifusa import *
from Backpropagation import *
from SistemaExperto import *
import os
def principal():
    var = 0
    while True:

        A = input("Estado de la via : \n0 --> Buena\n100 --> Mala\n")
        C = input("Intensidad de LLuvia\n0 --> Mucha\n100 --> Poca\n")
        B = input("Hora :\n00 --> 12 AM\n23 --> 11 PM\n")
        D = input("Dia de la Semana (numero):\nLunes 1 - Martes 2- Miercoles 3 - Jueves 4 - Viernes 5 - Sabado 6 - Domingo 7\n")
        E = input("Mes del año(numero):\nEnero (1) - Febrero (2) - Marzo (3) - Abril (4) - Mayo (5) - Junio (6)\n - Julio (7) - Agosto (8) -Septiembre (9) - Octubre (10)- Noviembre (11) - Diciembre (12)\n")

        if A >=0 and  A <=100:
            var=var+1
        if B >=0 and B <= 23:
            var=var+1
        if C >=0 and  C <=100:
            var=var+1
        if D >=1 and  D <=7:
            var=var+1
        if E >=1 and  E <=12:
            var=var+1
        if var == 5:
            break;
        else :
            var = 0
            os.system("cls")
            print("hay un dato incorrecto por favor vuelva a ingresar la informacion\nEn el formato recomendado\n")


    riesgo = CalcularRiesgo(A,C,B,D,E)

    red = RedNeuronal(11,7,2,riesgo)

    red.Entrenamiento(crear_patron())

    accidentalidad =red.Resultado()

    V(accidentalidad,Velocidad_Sugerida)

    print "Velocidad Sugerida:",Velocidad_Sugerida.v(),"km/h"


if __name__ =='__main__':
    i = 0
    while(True):
        os.system("cls")
        print("\n-----------------------\n")
        print("Sistema de Sugerencia de Velocidad \n")
        print("1.Realizar Consulta\n")
        print("2.Salir\n")
        op=input("Ingrese opcion: ")
        print('\n')

        if op == 1:
            principal()
            os.system("pause")
        elif op == 2:
            break;
