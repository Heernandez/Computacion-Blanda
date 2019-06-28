from pyDatalog import pyDatalog

pyDatalog.create_terms('Velocidad, V, Accidentalidad, Velocidad_Sugerida')

#Base del Conocimiento
+Velocidad(0,"61-80")
+Velocidad(1,"46-60")
+Velocidad(2,"25-45")
+Velocidad(3,"5-25")
#Reglas
V(Accidentalidad,Velocidad_Sugerida) <= Velocidad(Accidentalidad,Velocidad_Sugerida)
