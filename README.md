
* x  pincha

	falta el manejo de estos casos deberiamos decir ERROR: El término no es cerrado (x está libre)
	
	
* Alguno de estos casos creeeo que deberian andar pero dan error de tipos...

	(\x:Nat.succ(x))(\y:Nat.succ(y)) succ(0)
	(\x:Nat.succ(x))( (\y:Nat.succ(y)) succ(0) )


*isZero :

	-no chequea tipos
		iszero(false)   -------> iszero(false):Bool
		iszero(\x:Bool.x)----> iszero(\x:Bool.x):Bool
		iszero( (\x:Bool.x) true) -> iszero(true):Bool
		
	-nunca da false, cuando el resultado es false

		iszero(pred(0)) --------> iszero(pred(0)):Bool  
		iszero(succ(0)) --------> iszero(succ(0)):Bool 

	-entonces no reduce cosas como esta:
		
		if iszero(pred(0)) then true else false


este anda bien:		isZero(pred(succ(0)))---> true:Bool



--estas cosas son menos importantes
	
	
* No aclaramos que expresion es la que espera un tipo distinto al pasado

	if result.dic[self.variable].value() != self.type.value():
						return Error( 'esperaba un valor de tipo ' + result.type.value())    
		

	podriamos hacer, por ejemplo:

	if result.dic[self.variable].value() != self.type.value():
						return Error( self.expression.toStringParaError() +'La expresion esperaba un valor de tipo ' + result.type.value())


	agregando la funcion, por ejemplo para succ:

	def toStringParaError(self):
			return 'succ' 
			
			
			
* interpreta cualquier numero como cero, estan usando la macro n= succ^n(0) y no creo que sea obligatorio admitirla

	(\x:Nat.succ(succ(x))) 3 --------> succ(succ(0)):Nat

  podriamos hacer una funcioncita q si lee numeros en la cadena de entrada
  los transforme a succ(succ(..))