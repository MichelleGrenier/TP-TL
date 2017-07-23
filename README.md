Testeo 2:
----------

* pincha

		(\x.Nat.iszero(x)) ---> Hubo un error en el parseo.
					Hubo un error en el parseo.
					Traceback (most recent call last):
					  File "C:\Users\Michelle\Documents\T Leng\TP-TL\main.py", line 11, in <module>
					    result = parse(exp_str).calculate()
					AttributeError: 'NoneType' object has no attribute 'calculate'
					
* iszero:

Creo que esto deberia dar error cuando chequea tipos en vez de false:

		iszero(false) ---> OK: false:Bool
		iszero(\x:Bool.x) ---> OK: false:Bool

esto no deberia reducir:

		(\x:Nat.iszero(x))  (\y:Nat.pred(y)) 	----> OK: false:Bool
		(\x:Nat.iszero(x))  (\y:Nat.y)		----> OK: false:Bool

esto deberia ser true:

		(\x:Nat.iszero(pred(x))) succ(0)	----> OK: false:Bool
		

* if:


esto deberia reducir:

		if( (\x:Nat.iszero(pred(x))) succ(0) ) then true else false ----> OK: if (false) then true else false:Bool		
		if ( iszero(0)) then true else false			    ----> OK: if (true) then true else false:Bool
		

* Asociatividad:

Se pueden agregar paréntesis para forzar a una asociatividad/precedencia determinada. Adicionalmente, puede ser que haya paréntesis de más, y esas expresiones deben ser soportadas (e.g., en (\x:T1.M1) ((\y:T2.M2) M), se aplica la función con la variable x al resultado de la aplicación de la función con la variable y a M, por lo que se cambia a precedencia y asociatividad de la abstracción)

Aceptamos bien una cadena con presedencia y asociatividad a derecha forzada con parentesis:
		
		(\x:Nat.succ(x)) ((\y:Nat.pred(y)) succ(succ(0)) ) ----> OK: succ((succ(0))):Nat    
		
Una sin parentesis, deberia ser lo mismo que tener parentesis que fuercen asociatividad a izq:

Sin parentesis:

		(\x:Nat.x) (\y:Nat.succ(y))  succ(succ(0)) ----> OK: succ(succ(succ(0))):Nat
Con:

		((\x:Nat.x) (\y:Nat.succ(y)) ) succ(succ(0))----> OK: succ(succ(succ(0))):Nat


Sin parentesis:

		(\x:Nat.succ(x))  (\y:Nat.pred(y))  succ(succ(0)) ----> ERROR: La parte izquierda de la aplicacion no es una funcion con dominio en Nat
Con:

		( (\x:Nat.succ(x)) (\y:Nat.pred(y)) ) succ(succ(0))----> ERROR: La parte izquierda de la aplicacion no es una funcion con dominio en Nat 

Funcionan igual, debemos estar asociando bien !


Me queda la duda de si estamos resolviendo bien la aplicacion, porque una cosa asi anda bien

		 (\x:Nat.succ(x)) (\y:Nat.pred(y)) --> OK: succ((\y:Nat.pred(y))):Nat

Pero no hay manera de asignarle un valor a Y para que reduzca
		
		succ((\y:Nat.pred(y))) 0 ---> ERROR: La parte izquierda de la aplicacion no es una funcion con dominio en Nat

Entonces esto no reduce

		(\x:Nat.iszero(x))  (\y:Nat.pred(y))  succ(succ(0))
		
 a menos que la primer lambda no aplique ninguna funcion
 		
		(\x:Nat.x)  (\y:Nat.pred(y))  succ(succ(0)) ---> OK: succ(0):Nat



Gramatica 
----------
		
		expression -> LAMBDA VARIABLE TWOPOINTS type POINT expression2
		expression -> expression2

		expression2 -> IF expression3 THEN expression3 ELSE expression3
		expression2 -> expression3

		expression3 -> expression4 F
		F -> expression4 F
		F -> lambda

		expression4 -> SUCC OPENPAREN expression4 CLOSEPAREN
		expression4 -> PRED OPENPAREN expression4 CLOSEPAREN
		expression4 -> ISZERO OPENPAREN expression4 CLOSEPAREN
		
		expression4 -> expression5
		expression4 -> OPENPAREN expression CLOSEPAREN
		expression4 -> expression

		expression5 -> ZERO
		expression5 -> VARIABLE
		expression5 -> TRUE
		expression5 -> FALSE

		type -> BOOL T
		type -> NAT T
		T ->  ARROW type
		T -> lambda
		
			
----------------------------------------------------------------------

		E -> expression F
		F -> expression F
		F -> lambda
		expression -> LAMBDA VARIABLE TWOPOINTS type POINT expression
		expression -> IF expression THEN expression ELSE expression
		expression -> SUCC OPENPAREN expression CLOSEPAREN
		expression -> PRED OPENPAREN expression CLOSEPAREN
		expression -> ISZERO OPENPAREN expression CLOSEPAREN
		expression -> OPENPAREN expression CLOSEPAREN
		expression -> ZERO
		expression -> VARIABLE
		expression -> TRUE
		expression -> FALSE
		type -> BOOL T
		type -> NAT T
		T ->  ARROW type
		T -> lambda


Testeo
--------

* x  pincha

	falta el manejo de estos casos deberiamos decir ERROR: El término no es cerrado (x está libre)
	
	
* Alguno de estos casos creeeo que deberian andar pero dan error de tipos...


		(\x:Nat.succ(x))(\y:Nat.succ(y)) succ(0)
		(\x:Nat.succ(x))( (\y:Nat.succ(y)) succ(0) )


* isZero :

	-no chequea tipos
	
		iszero(false)   -------> iszero(false):Bool
		iszero(\x:Bool.x)----> iszero(\x:Bool.x):Bool
		iszero( (\x:Bool.x) true) -> iszero(true):Bool
		
	-nunca da false, cuando el resultado es false

		iszero(pred(0)) --------> iszero(pred(0)):Bool  
		iszero(succ(0)) --------> iszero(succ(0)):Bool 

	-entonces no reduce cosas como esta:
		
		if iszero(pred(0)) then true else false


	-este anda bien:   
		
		isZero(pred(succ(0)))---> true:Bool




Estas cosas son menos importantes
-----------------------------------	


* No aclaramos que expresion es la que espera un tipo distinto al pasado

		if result.dic[self.variable].value() != self.type.value():
			return Error( 'La expresion esperaba un valor de tipo ' + result.type.value())    
		

	podriamos hacer, por ejemplo:

		if result.dic[self.variable].value() != self.type.value():
			return Error( self.expression.toStringParaError() +' esperaba un valor de tipo ' + result.type.value())


	agregando la funcion, por ejemplo para succ:

		def toStringParaError(self):
			return 'succ' 
			
			
			
* interpreta cualquier numero como cero, estan usando la macro n= succ^n(0) y no creo que sea obligatorio admitirla

		(\x:Nat.succ(succ(x))) 3 --------> succ(succ(0)):Nat

  podriamos hacer una funcioncita q si lee numeros en la cadena de entrada
  los transforme a succ(succ(..))
