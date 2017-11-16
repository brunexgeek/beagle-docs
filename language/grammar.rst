Grammar
=======

.. role:: bgram-string

.. role:: bgram-detail

Structure
---------

.. _section-Unit:

.. rst-class:: non-terminal

Unit
	: \ :ref:`Package<section-Package>`\ ? \ :ref:`Import<section-Import>`\ \* \ :ref:`Type<section-Type>`\ +

	;

.. _section-Package:

.. rst-class:: non-terminal

Package
	: \ :bgram-string:`"package"` \ :ref:`QualifiedName<section-QualifiedName>`

	;

.. _section-Import:

.. rst-class:: non-terminal

Import
	: \ :bgram-string:`"import"` \ :ref:`QualifiedName<section-QualifiedName>` \ ( \ :bgram-string:`"."` \ :bgram-string:`"*"` \ | \ :bgram-string:`"as"` \ :ref:`Name<section-Name>` \ )\ ?

	;

.. _section-Type:

.. rst-class:: non-terminal

Type
	: \ :ref:`Class<section-Class>`

	;

.. _section-Class:

.. rst-class:: non-terminal

Class
	: \ :ref:`Annotation<section-Annotation>`\ \* \ :bgram-string:`"class"` \ :ref:`QualifiedName<section-QualifiedName>` \ :ref:`Extends<section-Extends>`\ ? \ :ref:`ClassBody<section-ClassBody>`\ ?

	;

.. _section-Extends:

.. rst-class:: non-terminal

Extends
	: \ :bgram-string:`":"` \ :ref:`TypeReference<section-TypeReference>` \ ( \ :bgram-string:`","` \ :ref:`TypeReference<section-TypeReference>` \ )\ \*

	;

.. _section-Annotation:

.. rst-class:: non-terminal

Annotation
	: \ :bgram-string:`"@"` \ :ref:`QualifiedName<section-QualifiedName>`

	;

.. _section-ClassBody:

.. rst-class:: non-terminal

ClassBody
	: \ :bgram-string:`"{"` \ :ref:`Member<section-Member>`\ \* \ :bgram-string:`"}"`

	;

.. _section-Member:

.. rst-class:: non-terminal

Member
	: \ :ref:`Variable<section-Variable>`

	: \ :ref:`Constant<section-Constant>`

	: \ :ref:`Method<section-Method>`

	;

.. _section-Variable:

.. rst-class:: non-terminal

Variable
	: \ :ref:`Annotation<section-Annotation>`\ \* \ :bgram-string:`"var"` \ :ref:`Name<section-Name>` \ ( \ :bgram-string:`":"` \ :ref:`TypeReference<section-TypeReference>` \ )\ ? \ ( \ :bgram-string:`"="` \ :ref:`Expression<section-Expression>` \ )\ ?

	;

.. _section-Constant:

.. rst-class:: non-terminal

Constant
	: \ :ref:`Annotation<section-Annotation>`\ \* \ :bgram-string:`"const"` \ :ref:`Name<section-Name>` \ ( \ :bgram-string:`":"` \ :ref:`TypeReference<section-TypeReference>` \ )\ ? \ :bgram-string:`"="` \ :ref:`Expression<section-Expression>`

	;

.. _section-Method:

.. rst-class:: non-terminal

Method
	: \ :ref:`Annotation<section-Annotation>`\ \* \ :bgram-string:`"def"` \ :ref:`Name<section-Name>` \ :ref:`ParameterList<section-ParameterList>` \ ( \ :bgram-string:`":"` \ :ref:`TypeReference<section-TypeReference>` \ )\ ? \ :ref:`Block<section-Block>`\ ?

	;

.. _section-ParameterList:

.. rst-class:: non-terminal

ParameterList
	: \ :bgram-string:`"("` \ :bgram-string:`")"`

	: \ :bgram-string:`"("` \ :ref:`Parameter<section-Parameter>` \ ( \ :bgram-string:`","` \ :ref:`Parameter<section-Parameter>` \ )\ \* \ :bgram-string:`")"`

	;

.. _section-Parameter:

.. rst-class:: non-terminal

Parameter
	: \ ( \ :bgram-string:`"var"` \ | \ :bgram-string:`"const"` \ )\ ? \ :ref:`Name<section-Name>` \ :bgram-string:`":"` \ :ref:`TypeReference<section-TypeReference>`

	;

.. _section-QualifiedName:

.. rst-class:: non-terminal

QualifiedName
	: \ :ref:`Name<section-Name>` \ ( \ :bgram-string:`"."` \ :ref:`Name<section-Name>` \ )\ \*

	;

.. _section-TypeReference:

.. rst-class:: non-terminal

TypeReference
	: \ :ref:`QualifiedName<section-QualifiedName>`

	;

.. _section-Name:

.. rst-class:: non-terminal

Name
	: \ :bgram-detail:`<UTF-16 '_', 'a'-'z', 'A'-'Z' or '0'-'9'>`

	;

Expressions
-----------

.. _section-Expression:

.. rst-class:: non-terminal

Expression
	: \ :ref:`Disjunction<section-Disjunction>` \ ( \ :ref:`AssignmentOperator<section-AssignmentOperator>` \ :ref:`Disjunction<section-Disjunction>` \ )\ \*

	;

.. _section-Disjunction:

.. rst-class:: non-terminal

Disjunction
	: \ :ref:`Conjunction<section-Conjunction>` \ ( \ :bgram-string:`"or"` \ :ref:`Conjunction<section-Conjunction>` \ )\ \*

	;

.. _section-Conjunction:

.. rst-class:: non-terminal

Conjunction
	: \ :ref:`EqualityComparison<section-EqualityComparison>` \ ( \ :bgram-string:`"and"` \ :ref:`EqualityComparison<section-EqualityComparison>` \ )\ \*

	;

.. _section-EqualityComparison:

.. rst-class:: non-terminal

EqualityComparison
	: \ :ref:`Comparison<section-Comparison>` \ ( \ :ref:`EqualityOperation<section-EqualityOperation>` \ :ref:`Comparison<section-Comparison>` \ )\ \*

	;

.. _section-Comparison:

.. rst-class:: non-terminal

Comparison
	: \ :ref:`NamedInfix<section-NamedInfix>` \ ( \ :ref:`ComparisonOperation<section-ComparisonOperation>` \ :ref:`NamedInfix<section-NamedInfix>` \ )\ \*

	;

.. _section-NamedInfix:

.. rst-class:: non-terminal

NamedInfix
	: \ :ref:`AdditiveExpression<section-AdditiveExpression>` \ ( \ :ref:`InOperation<section-InOperation>` \ :ref:`AdditiveExpression<section-AdditiveExpression>` \ )\ \*

	: \ :ref:`AdditiveExpression<section-AdditiveExpression>` \ ( \ :ref:`IsOperation<section-IsOperation>` \ :ref:`TypeReference<section-TypeReference>` \ )\ ?

	;

.. _section-AdditiveExpression:

.. rst-class:: non-terminal

AdditiveExpression
	: \ :ref:`MultiplicativeExpression<section-MultiplicativeExpression>` \ ( \ :ref:`AdditiveOperation<section-AdditiveOperation>` \ :ref:`MultiplicativeExpression<section-MultiplicativeExpression>` \ )\ \*

	;

.. _section-MultiplicativeExpression:

.. rst-class:: non-terminal

MultiplicativeExpression
	: \ :ref:`PrefixUnaryExpression<section-PrefixUnaryExpression>` \ ( \ :ref:`MultiplicativeOperation<section-MultiplicativeOperation>` \ :ref:`PrefixUnaryExpression<section-PrefixUnaryExpression>` \ )\ \*

	;

.. _section-PrefixUnaryExpression:

.. rst-class:: non-terminal

PrefixUnaryExpression
	: \ :ref:`PrefixUnaryOperation<section-PrefixUnaryOperation>`\ \* \ :ref:`PostfixUnaryExpression<section-PostfixUnaryExpression>`

	;

.. _section-PostfixUnaryExpression:

.. rst-class:: non-terminal

PostfixUnaryExpression
	: \ :ref:`AtomicExpression<section-AtomicExpression>` \ :ref:`PostfixUnaryOperation<section-PostfixUnaryOperation>`\ \*

	;

.. _section-AtomicExpression:

.. rst-class:: non-terminal

AtomicExpression
	: \ :bgram-string:`"("` \ :ref:`expression<section-expression>` \ :bgram-string:`")"`

	: \ :ref:`LiteralConstant<section-LiteralConstant>`

	: \ :ref:`Name<section-Name>`

	;

.. _section-LiteralConstant:

.. rst-class:: non-terminal

LiteralConstant
	: \ :ref:`BooleanLiteral<section-BooleanLiteral>`

	: \ :ref:`StringLiteral<section-StringLiteral>`

	: \ :ref:`IntegerLiteral<section-IntegerLiteral>`

	: \ :ref:`HexadecimalLiteral<section-HexadecimalLiteral>`

	: \ :bgram-string:`"null"`

	;

.. _section-BooleanLiteral:

.. rst-class:: non-terminal

BooleanLiteral
	: \ :bgram-string:`"true"`

	: \ :bgram-string:`"false"`

	;

.. _section-StringLiteral:

.. rst-class:: non-terminal

StringLiteral
	: \ :bgram-string:`"'"` \ :ref:`Character<section-Character>`\ \* \ :bgram-string:`"'"`

	;

.. _section-IntegerLiteral:

.. rst-class:: non-terminal

IntegerLiteral
	: \ :ref:`Digit<section-Digit>` \ ( \ :ref:`Digit<section-Digit>` \ | \ :bgram-string:`"_"` \ )\ \*

	;

.. _section-HexadecimalLiteral:

.. rst-class:: non-terminal

HexadecimalLiteral
	: \ :bgram-string:`"0x"` \ :ref:`HexDigit<section-HexDigit>` \ ( \ :ref:`HexDigit<section-HexDigit>` \ | \ :bgram-string:`"_"` \ )\ \*

	;

.. _section-Character:

.. rst-class:: non-terminal

Character
	: \ :bgram-detail:`<UTF-16 character>`

	;

.. _section-MultiplicativeOperation:

.. rst-class:: non-terminal

MultiplicativeOperation
	: \ :bgram-string:`"*"`

	: \ :bgram-string:`"/"`

	: \ :bgram-string:`"%"`

	;

.. _section-AdditiveOperation:

.. rst-class:: non-terminal

AdditiveOperation
	: \ :bgram-string:`"+"`

	: \ :bgram-string:`"-"`

	;

.. _section-InOperation:

.. rst-class:: non-terminal

InOperation
	: \ :bgram-string:`"in"`

	: \ :bgram-string:`"!in"`

	;

.. _section-IsOperation:

.. rst-class:: non-terminal

IsOperation
	: \ :bgram-string:`"is"`

	: \ :bgram-string:`"!is"`

	;

.. _section-ComparisonOperation:

.. rst-class:: non-terminal

ComparisonOperation
	: \ :bgram-string:`"<"`

	: \ :bgram-string:`">"`

	: \ :bgram-string:`">="`

	: \ :bgram-string:`"<="`

	;

.. _section-EqualityOperation:

.. rst-class:: non-terminal

EqualityOperation
	: \ :bgram-string:`"!="`

	: \ :bgram-string:`"=="`

	;

.. _section-AssignmentOperator:

.. rst-class:: non-terminal

AssignmentOperator
	: \ :bgram-string:`"="`

	: \ :bgram-string:`"+="`

	: \ :bgram-string:`"-="`

	: \ :bgram-string:`"*="`

	: \ :bgram-string:`"/="`

	: \ :bgram-string:`"%="`

	;

.. _section-PrefixUnaryOperation:

.. rst-class:: non-terminal

PrefixUnaryOperation
	: \ :bgram-string:`"-"`

	: \ :bgram-string:`"+"`

	: \ :bgram-string:`"++"`

	: \ :bgram-string:`"--"`

	: \ :bgram-string:`"not"`

	;

.. _section-PostfixUnaryOperation:

.. rst-class:: non-terminal

PostfixUnaryOperation
	: \ :bgram-string:`"++"`

	: \ :bgram-string:`"--"`

	: \ :ref:`ArrayAccess<section-ArrayAccess>`

	: \ :ref:`MemberAccessOperation<section-MemberAccessOperation>` \ :ref:`PostfixUnaryExpression<section-PostfixUnaryExpression>`

	;

.. _section-MemberAccessOperation:

.. rst-class:: non-terminal

MemberAccessOperation
	: \ :bgram-string:`"."`

	;

.. _section-ValueArguments:

.. rst-class:: non-terminal

ValueArguments
	: \ :bgram-string:`"("` \ :bgram-string:`")"`

	: \ :bgram-string:`"("` \ :ref:`Argument<section-Argument>` \ ( \ :bgram-string:`","` \ :ref:`Argument<section-Argument>` \ )\ \* \ :bgram-string:`")"`

	;

.. _section-Argument:

.. rst-class:: non-terminal

Argument
	: \ ( \ :ref:`Name<section-Name>` \ :bgram-string:`"="` \ )\ ? \ :ref:`Expression<section-Expression>`

	;

.. _section-ArrayAccess:

.. rst-class:: non-terminal

ArrayAccess
	: \ :bgram-string:`"["` \ :ref:`Expression<section-Expression>` \ ( \ :bgram-string:`","` \ :ref:`Expression<section-Expression>` \ )\ \* \ :bgram-string:`"]"`

	;

.. _section-Digit:

.. rst-class:: non-terminal

Digit
	: \ :bgram-string:`"0"` \ | \ :bgram-string:`"1"` \ | \ :bgram-string:`"2"` \ | \ :bgram-string:`"3"` \ | \ :bgram-string:`"4"` \ | \ :bgram-string:`"5"` \ | \ :bgram-string:`"6"` \ | \ :bgram-string:`"7"` \ | \ :bgram-string:`"8"` \ | \ :bgram-string:`"9"`

	;


.. _section-HexDigit:

.. rst-class:: non-terminal

HexDigit
	: \ :ref:`Digit<section-Digit>` \ | \ :bgram-string:`"a"` \ | \ :bgram-string:`"b"` \ | \ :bgram-string:`"c"` \ | \ :bgram-string:`"d"` \ | \ :bgram-string:`"e"` \ | \ :bgram-string:`"f"` \ | \ :bgram-string:`"A"` \ | \ :bgram-string:`"B"` \ | \ :bgram-string:`"C"` \ | \ :bgram-string:`"D"` \ | \ :bgram-string:`"E"` \ | \ :bgram-string:`"F"`

	;



Statements
----------

.. _section-Block:

.. rst-class:: non-terminal

Block
	: \ :bgram-string:`"{"` \ :ref:`Statement<section-Statement>`\ \* \ :bgram-string:`"}"`

	;

.. _section-Statement:

.. rst-class:: non-terminal

Statement
	: \ :ref:`IfThenElse<section-IfThenElse>`

	: \ :ref:`Return<section-Return>`

	: \ :ref:`Expression<section-Expression>`

	;

.. _section-IfThenElse:

.. rst-class:: non-terminal

IfThenElse
	: \ :bgram-string:`"if"` \ :ref:`Expression<section-Expression>` \ :bgram-string:`"then"` \ :ref:`BlockOrStatement<section-BlockOrStatement>` \ ( \ :bgram-string:`"else"` \ :ref:`BlockOrStatement<section-BlockOrStatement>` \ )\ ?

	;

.. _section-BlockOrStatement:

.. rst-class:: non-terminal

BlockOrStatement
	: \ :ref:`Block<section-Block>`

	: \ :ref:`Statement<section-Statement>`

	;

.. _section-Return:

.. rst-class:: non-terminal

Return
	: \ :bgram-string:`"return"` \ :ref:`Expression<section-Expression>`

	;

