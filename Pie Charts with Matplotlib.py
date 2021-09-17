import matplotlib.pyplot as plt

nationalities = ['American', 'German', 'French', 'Other']
students = [60, 23, 21, 34]
#======Function Zip of Python============================
pairs = zip(students, nationalities)
pairs = sorted(list(pairs))
students, nationalities = zip(*pairs)
# print(list(pairs))
#========================================================
explode = [0,0,0.1,0]
plt.pie(students, labels=nationalities, autopct='%.2f%%',
        explode=explode, counterclock=False, startangle=90)
plt.title("Student Nationality")
#========================================================
plt.show()
''' 
La funcion Zip comprime los elementos de una lista,
relacionando cada index en pares dentro de una tupla,
cada par o tupla esta relacionado como Clave/Valor dentro de un diccionario,
luego, Sorted lista una version de los pares en forma ordenada,
finalmente los volvemos a descomprimir pero los devuelve de forma ordenada,
listo para representarlos en el grafico de torta de menor a mayor ,
en sentido de la agujas del relog, fijando como angulo de inico 90 grados. 
'''