#Python define una serie de valores constantes en su propio namespace. Los más importantes son:

#False: El valor false del tipo bool.

#True: El valor true del tipo bool.

#None: El valor del tipo NoneType. Generalmente None se utiliza para representar la ausencia de valor de una variable.
"""
Declarar variables del tipo int, str, bool y float sumarlas, multiplicarlas
y dividirlas.
investigar cuales son las operaciones no permitidas entre ellas y guardar los errores 
que nos devuelven.
"""
nota:int = 9;
nota2:str = "7";
nota3:bool = False;
nota4:float = 9.5;

print(nota+(int)(nota2));
#print(nota3+nota2); No se puede sumar str y bool
#print(nota+nota3); No se puede sumar int y bool
#print(nota3+nota4); No se puede sumar float y bool
print(nota+nota4);
print(nota4+(int)(nota2));

print(nota*(int)(nota2));
#print(nota3+nota2); No se puede multiplicar str y bool
#print(nota+nota3); No se puede multiplicar int y bool
#print(nota3+nota4); No se puede multiplicar float y bool
print(nota*nota4);
print(nota4*(int)(nota2));

print(nota/(int)(nota2));
#print(nota3+nota2); No se puede dividir str y bool
#print(nota+nota3); No se puede dividir int y bool
#print(nota3+nota4); No se puede dividir float y bool
print(nota/nota4);
print(nota4/(int)(nota2));