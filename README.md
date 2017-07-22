Gramatica 
----------
		
		expression -> LAMBDA VARIABLE TWOPOINTS type POINT expression2
		expression -> expression2

		expression2 -> IF expression3 THEN expression3 ELSE expression3
		expression2 -> expression3

		expression3 -> expression4 F
		F -> expression4 F
		F -> lambda

		expression4 -> SUCC OPENPAREN expression5 CLOSEPAREN
		expression4 -> PRED OPENPAREN expression5 CLOSEPAREN
		expression4 -> ISZERO OPENPAREN expression5 CLOSEPAREN
		
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
