
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'expressionVARIABLE TRUE FALSE IF THEN ELSE LAMBDA TWOPOINTS POINT ZERO SUCC OPENPAREN CLOSEPAREN PRED ISZERO BOOL NAT ARROWexpression : LAMBDA VARIABLE TWOPOINTS type POINT expressionexpression : expression2expression2 : IF expression THEN expression ELSE expressionexpression2 : expression3expression3 : expression4 expression5expression5 : expressionexpression5 :expression4 : SUCC OPENPAREN expression CLOSEPARENexpression4 : PRED OPENPAREN expression CLOSEPARENexpression4 : ISZERO OPENPAREN expression CLOSEPARENexpression4 : expression6expression6 : TRUEexpression6 : FALSEexpression6 : ZEROexpression6 : VARIABLEexpression6 : OPENPAREN expression CLOSEPARENtype : BOOL Ttype : NAT TT : ARROW typeT :'
    
_lr_action_items = {'$end':([3,6,7,8,9,10,11,12,14,20,21,26,30,31,33,42,44,],[-12,-14,-15,-4,-2,-7,-11,-13,0,-5,-6,-16,-8,-10,-9,-3,-1,]),'FALSE':([0,3,4,5,6,7,10,11,12,16,17,22,26,27,30,31,33,37,40,],[12,-12,12,12,-14,-15,12,-11,-13,12,12,12,-16,12,-8,-10,-9,12,12,]),'NAT':([29,38,],[34,34,]),'THEN':([3,6,7,8,9,10,11,12,19,20,21,26,30,31,33,42,44,],[-12,-14,-15,-4,-2,-7,-11,-13,27,-5,-6,-16,-8,-10,-9,-3,-1,]),'PRED':([0,3,4,5,6,7,10,11,12,16,17,22,26,27,30,31,33,37,40,],[13,-12,13,13,-14,-15,13,-11,-13,13,13,13,-16,13,-8,-10,-9,13,13,]),'CLOSEPAREN':([3,6,7,8,9,10,11,12,18,20,21,24,25,26,28,30,31,33,42,44,],[-12,-14,-15,-4,-2,-7,-11,-13,26,-5,-6,30,31,-16,33,-8,-10,-9,-3,-1,]),'POINT':([34,35,36,39,41,43,],[-20,40,-20,-18,-17,-19,]),'ARROW':([34,36,],[38,38,]),'SUCC':([0,3,4,5,6,7,10,11,12,16,17,22,26,27,30,31,33,37,40,],[1,-12,1,1,-14,-15,1,-11,-13,1,1,1,-16,1,-8,-10,-9,1,1,]),'ELSE':([3,6,7,8,9,10,11,12,20,21,26,30,31,32,33,42,44,],[-12,-14,-15,-4,-2,-7,-11,-13,-5,-6,-16,-8,-10,37,-9,-3,-1,]),'ISZERO':([0,3,4,5,6,7,10,11,12,16,17,22,26,27,30,31,33,37,40,],[2,-12,2,2,-14,-15,2,-11,-13,2,2,2,-16,2,-8,-10,-9,2,2,]),'ZERO':([0,3,4,5,6,7,10,11,12,16,17,22,26,27,30,31,33,37,40,],[6,-12,6,6,-14,-15,6,-11,-13,6,6,6,-16,6,-8,-10,-9,6,6,]),'BOOL':([29,38,],[36,36,]),'TWOPOINTS':([23,],[29,]),'VARIABLE':([0,3,4,5,6,7,10,11,12,15,16,17,22,26,27,30,31,33,37,40,],[7,-12,7,7,-14,-15,7,-11,-13,23,7,7,7,-16,7,-8,-10,-9,7,7,]),'IF':([0,3,4,5,6,7,10,11,12,16,17,22,26,27,30,31,33,37,40,],[5,-12,5,5,-14,-15,5,-11,-13,5,5,5,-16,5,-8,-10,-9,5,5,]),'TRUE':([0,3,4,5,6,7,10,11,12,16,17,22,26,27,30,31,33,37,40,],[3,-12,3,3,-14,-15,3,-11,-13,3,3,3,-16,3,-8,-10,-9,3,3,]),'OPENPAREN':([0,1,2,3,4,5,6,7,10,11,12,13,16,17,22,26,27,30,31,33,37,40,],[4,16,17,-12,4,4,-14,-15,4,-11,-13,22,4,4,4,-16,4,-8,-10,-9,4,4,]),'LAMBDA':([0,3,4,5,6,7,10,11,12,16,17,22,26,27,30,31,33,37,40,],[15,-12,15,15,-14,-15,15,-11,-13,15,15,15,-16,15,-8,-10,-9,15,15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,4,5,10,16,17,22,27,37,40,],[14,18,19,21,24,25,28,32,42,44,]),'T':([34,36,],[39,41,]),'type':([29,38,],[35,43,]),'expression3':([0,4,5,10,16,17,22,27,37,40,],[8,8,8,8,8,8,8,8,8,8,]),'expression2':([0,4,5,10,16,17,22,27,37,40,],[9,9,9,9,9,9,9,9,9,9,]),'expression5':([10,],[20,]),'expression4':([0,4,5,10,16,17,22,27,37,40,],[10,10,10,10,10,10,10,10,10,10,]),'expression6':([0,4,5,10,16,17,22,27,37,40,],[11,11,11,11,11,11,11,11,11,11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> LAMBDA VARIABLE TWOPOINTS type POINT expression','expression',6,'p_expression_lambda','parser.py',9),
  ('expression -> expression2','expression',1,'p_expression_expression2','parser.py',13),
  ('expression2 -> IF expression THEN expression ELSE expression','expression2',6,'p_expression2_if','parser.py',17),
  ('expression2 -> expression3','expression2',1,'p_expression2_expression3','parser.py',21),
  ('expression3 -> expression4 expression5','expression3',2,'p_expression3_expression4_expression5','parser.py',25),
  ('expression5 -> expression','expression5',1,'p_expression5_expression','parser.py',29),
  ('expression5 -> <empty>','expression5',0,'p_expression5_none','parser.py',33),
  ('expression4 -> SUCC OPENPAREN expression CLOSEPAREN','expression4',4,'p_expression4_succ','parser.py',37),
  ('expression4 -> PRED OPENPAREN expression CLOSEPAREN','expression4',4,'p_expression4_pred','parser.py',41),
  ('expression4 -> ISZERO OPENPAREN expression CLOSEPAREN','expression4',4,'p_expression4_izsero','parser.py',45),
  ('expression4 -> expression6','expression4',1,'p_expression4_expression6','parser.py',49),
  ('expression6 -> TRUE','expression6',1,'p_expression6_true','parser.py',53),
  ('expression6 -> FALSE','expression6',1,'p_expression6_false','parser.py',57),
  ('expression6 -> ZERO','expression6',1,'p_expression6_zero','parser.py',61),
  ('expression6 -> VARIABLE','expression6',1,'p_expression6_variable','parser.py',65),
  ('expression6 -> OPENPAREN expression CLOSEPAREN','expression6',3,'p_expression6_expression','parser.py',69),
  ('type -> BOOL T','type',2,'p_type_bool','parser.py',73),
  ('type -> NAT T','type',2,'p_type_nat','parser.py',77),
  ('T -> ARROW type','T',2,'p_T_type','parser.py',81),
  ('T -> <empty>','T',0,'p_T_none','parser.py',85),
]
