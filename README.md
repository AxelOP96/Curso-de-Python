# Curso-de-Python 

Para utilizar Python, se debe descargar desde la pagina oficial https://www.python.org/downloads/
al descargar el instalador, se debe seleccionar la opcion añadir path para poder ejecutarla desde cualquier ruta desde nuestro sistema. Al instalar para 
comprobar que se instaló correctamente, se puede usar el cmd o consola. Al utilizar la palabra python la consola muestra la version y permite ejecutar 
cualquier sentencia python que deseemos como por ejemplo print("Hola mundo").
Una variable es una direccion de memoria con un valor que puede o no cambiar en el tiempo
Reglas para nombrar variables:
-debe comenzar con una letra
-despues de la primer letra se pueden usar, letras, numeros y guiones
-No se pueden usar espacios o caracteres especiales.
las variables tienen varios tipos entre ellos estan los floats que representan los enteros y decimales y los strings que representan texto.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Python para Backend(Codigofacilito.com) 
La extension para los archivos python es .py.
print("Hola mundo")

## Variable: dato que puede cambiar de valor y que funciona como una etiqueta en Python.
Declaracion de una variable:
<nombre> = <valor>
  
## Constante: Dato que no varia su valor en toda la ejecucion del programa.
  TITULO_CURSO = "Curso profesional de Python"
  
 ## Listado de palabras reservadas:
  

*False	  *class	    *is	         *return 
*None	    *continue	  *lambda	    *try
*True	    *def	      *nonlocal	  *while
*and	    *del	      *not	      *with
*as	      *elif	      *or	        *yield
*assert	  *else	      *pass	
*break	  *except	    *raise	
  
  
  https://www.programiz.com/python-programming/keyword-list
  
  ## Comentarios:
  Los comentarios son piezas de codigo o mensajes que no se ejecutan.
  Para realizar comentarios de una linea se usa # y para comentarios largos se usa """ al inicio y tambien  al final
  
  
  ## tipos de datos: 
    String, Int, Float y Bool
  Si es un texto largo es conveniente usar triples comillas dobles o triples comillas simples. 
  Int incluye los numeros positivos y negativos
  Float incluye los numeros de punto decimal
  Bool tipo de dato que solo puede almacenar dos tipos de valor, True o False
  
  
  ## Operadores relacionales:
    <, <=, >, >=, == , !=.
  
  
  ## Operadores logicos:
    and, or y not
  and es verdadero si todas las proposiciones son verdaderas, or es verdadero si al menos una es verdadera, not niega el valor de una proposicion.
  
  
  Para leer valores por teclado se usa input().
  Las funciones int(), float(), y == permiten cambiar el tipo de dato para una conversion. 
  
  ## Listas:
  	Crear una lista
	Para crear una lista, asigne una secuencia de valores a una variable. Cada valor está separado por una coma y están entre corchetes ([]). En el 
	ejemplo siguiente se almacena la lista de todos los planetas de la variable planets:
	planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    	lista = list()
    	lista = []
	Puede acceder a cualquier elemento de una lista colocando el índice entre corchetes [] después del nombre de la variable de lista. Los índices comienzan 
	a partir de 0, por lo que en el código siguiente, planets[0] es el primer elemento de la lista planets:
	print("The first planet is", planets[0])
	print("The second planet is", planets[1])
	print("The third planet is", planets[2])
	Para obtener la longitud de una lista, use la función integrada len()
	
	Las listas de Python son dinámicas: puede agregar y quitar elementos después de crearlas. Para agregar un elemento a una lista, use el 
	método .append(value).

	Por ejemplo, el código siguiente agrega la cadena "Pluto" al final de la lista planets:
	planets.append("Pluto")
	number_of_planets = len(planets)
	print("There are actually", number_of_planets, "planets in the solar system.")

	 Output:
	 There are actually 9 planets in the solar system.
	 Puede quitar el último elemento de una lista llamando al método .pop() en la variable de lista:
	 Los índices comienzan en cero y van en aumento. Los índices negativos comienzan al final de la lista y van hacia atrás.

	En el ejemplo siguiente, un índice de -1 devuelve el último elemento de una lista. Un índice de -2 devuelve el penúltimo
	print("The last planet is", planets[-1])
	print("The penultimate planet is", planets[-2])

	Output
	The last planet is Neptune
	The penultimate planet is Uranus
	Para determinar dónde se almacena un valor en una lista, use el método index de la lista. Este método busca el valor y devuelve el índice de ese elemento 
	en la lista. Si no encuentra ninguna coincidencia, devuelve -1.
	Python tiene funciones integradas para calcular los números más grandes y más pequeños de una lista. La función max() devuelve el número más grande y 
	min() devuelve el más pequeño
	Para ordenar una lista, use el método .sort() de la lista. Python ordenará una lista de cadenas en orden alfabético y una lista de números en orden numérico
	Para ordenar una lista en orden inverso, llame a .sort(reverse=True) en la lista:
	



  
  sub_lista = lista_cursos[0:3]
  sub_lista = lista_cursos[0:]
  sub_lista = lista_cursos[0:100]
  
  ## Metodos utiles para trabajar con listas
    .append(" ") agrega un elemento al final de nuestra lista
    .len() nos dice la longitud del string o array
    .insert(1, "C#") el primer argumento especifica la posicion y el segundo el elemento que queremos que este ahi, los siguientes elementos se mueven un lugar
    .extend() agrega los elementos de una lista a otra
    .remove()busca y remueve ese elemento de la lista
    del lista_cursos[0] borra ese indice de la lista
    .clear() reinicia los valores de una lista
    .sort() ordena ascendentemente los valores de una lista
    .sort(reverse=true) ordena descendentemente los valores
    min(lista)
    max(lista)
    lista.index(5) retorna el indice donde se encuentra el valor 5
  ### El método format()
	El método .format() usa llaves ({}) como marcadores de posición dentro de una cadena y utiliza la asignación de variables para reemplazar texto.
	>>> mass_percentage = "1/6"
	>>> print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage))
	No es necesario asignar variables repetidas varias veces, lo que hace que sea menos detallado porque es necesario asignar menos variables:On the Moon, 
	you would weigh about 1/6 of your weight on Earth.
	>>> print("""You are lighter on the {0}, because on the {0} 
	... you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))
	You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth
	En lugar de llaves vacías, la sustitución consiste en usar números. {0} significa usar el primer argumento (índice cero) de .format(), que en este caso 
	es Moon. {0} funciona bien para una repetición simple, pero reduce la legibilidad. Para mejorar la legibilidad, use argumentos de palabra clave en 
	.format() y, después, haga referencia a los mismos argumentos entre llaves:
	>>> print("""You are lighter on the {moon}, because on the {moon} 
	... you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))
	You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth
	A partir de la versión 3.6 de Python, es posible usar f-strings. Estas cadenas parecen plantillas y usan los nombres de variable del código. El uso de 
	f-strings en el ejemplo anterior tendría el siguiente aspecto:
	>>> print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")
	On the Moon, you would weigh about 1/6 of your weight on Earth
	Las variables se incluyen entre llaves y la cadena debe usar el prefijo f.
	Además de que las f-strings son menos detalladas que cualquier otra opción de formato, es posible usar expresiones entre llaves. Estas expresiones pueden 
	ser funciones u operaciones directas
	-Use abs para convertir el valor negativo en su valor absoluto
	
	## Biblioteca matemática
		Python tiene bibliotecas para proporcionar operaciones y cálculos más avanzados. Una de las más comunes es la biblioteca math. math permite hacer 
		el redondeo con floor y ceil, proporcionar el valor de pi y muchas otras operaciones. Veamos cómo usar esta biblioteca para redondear hacia arriba 
		o hacia abajo.

		El redondeo de números permite quitar la parte decimal de un número de punto flotante. Puede optar por redondear siempre hacia arriba al 
		número entero más cercano si usa ceil, o hacia abajo si usa floor.
		from math import ceil, floor

		round_up = ceil(12.5)
		print(round_up)

		round_down = floor(12.5)
		print(round_down)

		 Output
		 13
		 12
		 
	
  ## Tuplas:
    No pueden cambiar su valor pero si modificar su contenido
    sub_tupla = cursos[0:3]
    print(sub_tupla)
    * lo guarda como lista
    _ omite el valor
    zip() comprime los valores
    .split() divide el array en strings separados por espacios
    .join() une formando un String
  
 ## Strings:
    Concatenacion: unir strings
    -Con +
    -nombre_completo = 'Mr. %s %s' %(nombre, apellido)
    nombre_completo = 'Mr. {} {}.'.format(nombre, apellido)
    nombre_completo = f'Mr. {nombre} {apellido}.'

la funcion print() cuenta con un atributo llamado sep=' ' que indica como se van a separar los elementos
  
 ## Diccionarios:
 	Python usa llaves ({ }) y dos puntos (:) para indicar un diccionario. Puede crear un diccionario vacío y agregar valores más adelante, o bien rellenarlo 
	en el momento de la creación. Cada clave o valor está separado por dos puntos y el nombre de cada clave se incluye entre comillas como un literal de 
	cadena. Como la clave es un literal de cadena, puede usar el nombre que sea adecuado para describir el valor.

	Ahora se creará un diccionario para almacenar el nombre del planeta Tierra y el número de lunas que tiene:
	planet = {
    	'name': 'Earth',
    	'moons': 1
	}
    	diccionario = {}
    	diccionario = dict()
	Tiene dos claves, 'name' y 'moons'. Cada clave se comporta igual que una variable: tienen un nombre único y almacenan un valor. Pero se incluyen dentro 
	de una única variable más grande, denominada planet.

	Como sucede con las variables convencionales, debe asegurarse de que usa los tipos de datos correctos. En el valor moons de 1 en el ejemplo anterior, no 
	se han incluido comillas alrededor del número, porque se quiere usar un entero. Si hubiera usado '1', Python vería esta variable como una cadena, lo 
	que afectaría a la capacidad de realizar cálculos.

	A diferencia de las variables convencionales, los nombres de clave no necesitan seguir las reglas de nomenclatura estándar para Python. Puede usar 
	nombre clave para que sea más descriptivo en el código.
	Puede leer valores dentro de un diccionario. Los objetos de diccionario tienen un método get que puede usar para acceder a un valor mediante su clave. 
	Si quiere imprimir name, puede usar el código siguiente:
	print(planet.get('name'))

	Displays Earth
	Otra forma:
	print(planet['name'])
	Aunque el comportamiento de get y los corchetes ([ ]) suele ser el mismo para recuperar elementos, hay una diferencia principal. Si una clave no 
	está disponible, get devuelve None y [ ] genera un error KeyError
	También puede modificar valores dentro de un objeto de diccionario, con el método update. Este método acepta un diccionario como parámetro y actualiza 
	los valores existentes con los nuevos que proporcione. Si quiere cambiar name para el diccionario planet, puede usar lo siguiente, por ejemplo:
	planet.update({'name': 'Makemake'})
	planet['name'] = 'Makemake'
	Para quitar una clave, use pop
	Los diccionarios pueden almacenar cualquier tipo de valor, incluidos otros diccionarios. Esto le permite modelar datos complejos según sea necesario

    	diccionario = {"total":55}
	El método keys() devuelve un objeto de lista que contiene todas las claves. Puede usar este método para iterar por todos los elementos del diccionario.
    	diccionario.keys()
	De forma similar a keys(), values() devuelve la lista de todos los valores de un diccionario sin sus claves correspondientes. values() puede resultar 
	útil cuando se usa la clave con fines de etiquetado, como en el ejemplo anterior, en el que las claves son el nombre del mes. Puede usar para 
	values() determinar el importe total de las precipitaciones:
    	diccionario.values()
	total_rainfall = 0
	for value in rainfall.values():
    		total_rainfall = total_rainfall + value

	print(f'There was {total_rainfall}cm in the last quarter')

	 Output:
	 There was 10.8cm in the last quarter
	 
   
  	## Condicionales
    		if <Bool>:
    			print("Hola")
 	## Operador ternario
    		color= 'verde' if calificacion >=7 else 'rojo'
  	## For
    		for valor in range(5, 21)
        		print(valor)
  
  	## Funcion lambda
    	funcion_grados = lambda grados : grados * 1.8 + 32
  
  	## Decoradores:
    def funcion_a(funcion_b):
	    def funcion_c():
		    pass

	    return funcion_c
  
--------------------------------------------------------------------------------------------------------------------------------------------------------------------

* 100 days of Python: *
# Dia 1: Printing, commenting, debugging, string manipulation and variables.

Para empezar se puede usar un IDE online (repl.it)
Para mostrar un texto se usa la palabra reservada print() y lo que se quiere mostrar entre comillas.
Para que el usuario ingrese datos y estos queden guardados se usa la palabra reservada input()
Se escriben comentarios con el caracter #, todo lo que siga al caracter no se va a imprimir, sirve de guia para un futuro o como guia de lo que se hace.
Para calcular la longitud de un string se usa la palabra reservada len()

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# PYTHON para Data Science:
  
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
