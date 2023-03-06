## Curso-de-Python##

Para utilizar Python, se debe descargar desde la pagina oficial https://www.python.org/downloads/
al descargar el instalador, se debe seleccionar la opcion añadir path para poder ejecutarla desde cualquier ruta desde nuestro sistema. Al instalar para 
comprobar que se instaló correctamente, se puede usar el cmd o consola. Al utilizar la palabra python la consola muestra la version y permite ejecutar 
cualquier sentencia python que deseemos como por ejemplo print("Hola mundo").
Una variable es una direccion de memoria con un valor que puede o no cambiar en el tiempo
Reglas para nombrar variables:
-debe comenzar con una letra
-despues de la primer letra se pueden usar, letras, numeros y guiones
-No se pueden usar espacios o caracteres especiales.
las variables tienen varios tipos entre ellos estan los floats que representan los enteros y decimales y los strings que representan texto
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Python para Backend(Codigofacilito.com)**
La extension para los archivos python es .py.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

100 days of Python:
#Dia 1: Printing, commenting, debugging, string manipulation and variables.

Para empezar se puede usar un IDE online (repl.it)
Para mostrar un texto se usa la palabra reservada print() y lo que se quiere mostrar entre comillas.
Para que el usuario ingrese datos y estos queden guardados se usa la palabra reservada input()
Se escriben comentarios con el caracter #, todo lo que siga al caracter no se va a imprimir, sirve de guia para un futuro o como guia de lo que se hace.
Para calcular la longitud de un string se usa la palabra reservada len()

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#PYTHON para Data Science:
Los modulos agrupan herramientas relacionadas en Python. Por ejemplo:
-matplotlib(crea graficos)
-pandas(carga datos tabulares)
-scikit-learn(realiza machine learning)
-scipy(realiza funciones estadisticas)
-nltk(funciona con datos de texto)

Importing Python modules
Modules (sometimes called packages or libraries) help group together related sets of tools in Python. In this exercise, we'll examine two modules that are 
frequently used by Data Scientists:
para importar un modulo simplemente se escribe import seguido de un espacio y el nombre del modulo.
Para acortar los nombres se puede usar un alias, es decir luego de import y el nombre del modulo se sigue con la palabra as y el alias
statsmodels: used in machine learning; usually aliased as sm
seaborn: a visualization library; usually aliased as sns
Note that each module has a standard alias, which allows you to access the tools inside of the module without typing as many characters. For example, 
aliasing lets us
shorten seaborn.scatterplot() to sns.scatterplot().

In this exercise, we'll learn to import numpy, a module for performing mathematical operations on lists of data. The standard alias for numpy is np.

pd.read_csv() convierte un archivo en una tabla en Python
plt.plot() convierte datos en un grafico de lineas
plt.show() muestra el grafico en una nueva ventana

plt.plot(df.letter_index, df.frequency, label=`Ransom')
La funcion comienza con el modulo en el que la funcion vive (plt)
se sigue por el nombre de la funcion (plot)
Los argumentos claves dben ir tras los argumentos posicionales
Comienzan con el nombre del argumento(label) seguido del signo igual(=)
Seguido por el argumento(Ransom)
# Import pandas
import pandas as pd

# Load the 'ransom.csv' into a DataFrame
r = pd.read_csv('ransom.csv')

# Display DataFrame
print(r)
-------------------
# Plot a graph
plt.plot(x_values, y_values)

# Display the graph
plt.show()
----------------------
plate = 'FRQ****'

# Call the function lookup_plate()
lookup_plate(plate)

# Call lookup_plate() with the keyword argument for color
lookup_plate(plate, color='Green')
