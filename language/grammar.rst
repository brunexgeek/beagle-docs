Grammar
=======

.. role:: bgram-string

.. role:: bgram-detail

.. container:: grammar

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
		: \ :bgram-string:`"{"` \ :ref:`TypeMember<section-TypeMember>`\ \* \ :bgram-string:`"}"`

		;

	.. _section-TypeMember:
	.. rst-class:: non-terminal

	TypeMember
		: \ :ref:`TypeVariable<section-TypeVariable>`

		: \ :ref:`TypeConstant<section-TypeConstant>`

		: \ :ref:`TypeFunction<section-TypeFunction>`

		;

	.. _section-TypeVariable:
	.. rst-class:: non-terminal

	TypeVariable
		: \ :ref:`Annotation<section-Annotation>`\ \* \ :ref:`Variable<section-Variable>`

		;

	.. _section-TypeConstant:
	.. rst-class:: non-terminal

	TypeConstant
		: \ :ref:`Annotation<section-Annotation>`\ \* \ :ref:`Constant<section-Constant>`

		;

	.. _section-TypeFunction:
	.. rst-class:: non-terminal

	TypeFunction
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
		: \ :ref:`QualifiedName<section-QualifiedName>` \ ( \ :bgram-string:`"?"` \ )\ ?

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
		: \ :ref:`Disjunction<section-Disjunction>` \ ( \ :ref:`AssignmentOperator<section-AssignmentOperator>` \ :ref:`Expression<section-Expression>` \ )\ \*

		;

	.. _section-Disjunction:
	.. rst-class:: non-terminal

	Disjunction
		: \ :ref:`Conjunction<section-Conjunction>` \ ( \ :bgram-string:`"or"` \ :ref:`Disjunction<section-Disjunction>` \ )\ \*

		;

	.. _section-Conjunction:
	.. rst-class:: non-terminal

	Conjunction
		: \ :ref:`EqualityComparison<section-EqualityComparison>` \ ( \ :bgram-string:`"and"` \ :ref:`Conjunction<section-Conjunction>` \ )\ \*

		;

	.. _section-EqualityComparison:
	.. rst-class:: non-terminal

	EqualityComparison
		: \ :ref:`Comparison<section-Comparison>` \ ( \ :ref:`EqualityOperator<section-EqualityOperator>` \ :ref:`EqualityComparison<section-EqualityComparison>` \ )\ \*

		;

	.. _section-Comparison:
	.. rst-class:: non-terminal

	Comparison
		: \ :ref:`NamedInfix<section-NamedInfix>` \ ( \ :ref:`ComparisonOperator<section-ComparisonOperator>` \ :ref:`Comparison<section-Comparison>` \ )\ \*

		;

	.. _section-NamedInfix:
	.. rst-class:: non-terminal

	NamedInfix
		: \ :ref:`AdditiveExpression<section-AdditiveExpression>` \ ( \ :ref:`InOperator<section-InOperator>` \ :ref:`AdditiveExpression<section-AdditiveExpression>` \ )\ \*

		: \ :ref:`AdditiveExpression<section-AdditiveExpression>` \ :ref:`IsOperator<section-IsOperator>` \ :ref:`TypeReference<section-TypeReference>`

		;

	.. _section-AdditiveExpression:
	.. rst-class:: non-terminal

	AdditiveExpression
		: \ :ref:`MultiplicativeExpression<section-MultiplicativeExpression>` \ ( \ :ref:`AdditiveOperator<section-AdditiveOperator>` \ :ref:`AdditiveExpression<section-AdditiveExpression>` \ )\ \*

		;

	.. _section-MultiplicativeExpression:
	.. rst-class:: non-terminal

	MultiplicativeExpression
		: \ :ref:`PrefixUnaryExpression<section-PrefixUnaryExpression>` \ ( \ :ref:`MultiplicativeOperator<section-MultiplicativeOperator>` \ :ref:`MultiplicativeExpression<section-MultiplicativeExpression>` \ )\ \*

		;

	.. _section-PrefixUnaryExpression:
	.. rst-class:: non-terminal

	PrefixUnaryExpression
		: \ :ref:`PrefixUnaryOperator<section-PrefixUnaryOperator>`\ ? \ :ref:`PostfixUnaryExpression<section-PostfixUnaryExpression>`

		;

	.. _section-PostfixUnaryExpression:
	.. rst-class:: non-terminal

	PostfixUnaryExpression
		: \ :ref:`AtomicExpression<section-AtomicExpression>` \ :ref:`PostfixUnaryOperator<section-PostfixUnaryOperator>`\ ?

		;

	.. _section-AtomicExpression:
	.. rst-class:: non-terminal

	AtomicExpression
		: \ :bgram-string:`"("` \ :ref:`Expression<section-Expression>` \ :bgram-string:`")"`

		: \ :ref:`LiteralConstant<section-LiteralConstant>`

		: \ :ref:`Name<section-Name>`

		;

	.. _section-LiteralConstant:
	.. rst-class:: non-terminal

	LiteralConstant
		: \ :ref:`BooleanLiteral<section-BooleanLiteral>`

		: \ :ref:`StringLiteral<section-StringLiteral>`

		: \ :ref:`IntegerLiteral<section-IntegerLiteral>`

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
		: \ :bgram-detail:`<UTF-16 string>`

		;

	.. _section-IntegerLiteral:
	.. rst-class:: non-terminal

	IntegerLiteral
		: \ :bgram-detail:`<hexadecimal, decimal, octal or binary integral number>`

		;

	.. _section-Character:
	.. rst-class:: non-terminal

	Character
		: \ :bgram-detail:`<UTF-16 character>`

		;

	.. _section-MultiplicativeOperator:
	.. rst-class:: non-terminal

	MultiplicativeOperator
		: \ :bgram-string:`"*"`

		: \ :bgram-string:`"/"`

		: \ :bgram-string:`"%"`

		;

	.. _section-AdditiveOperator:
	.. rst-class:: non-terminal

	AdditiveOperator
		: \ :bgram-string:`"+"`

		: \ :bgram-string:`"-"`

		;

	.. _section-InOperator:
	.. rst-class:: non-terminal

	InOperator
		: \ :bgram-string:`"in"`

		: \ :bgram-string:`"not"` \ :bgram-string:`"in"`

		;

	.. _section-IsOperator:
	.. rst-class:: non-terminal

	IsOperator
		: \ :bgram-string:`"is"`

		: \ :bgram-string:`"not"` \ :bgram-string:`"is"`

		;

	.. _section-ComparisonOperator:
	.. rst-class:: non-terminal

	ComparisonOperator
		: \ :bgram-string:`"<"`

		: \ :bgram-string:`">"`

		: \ :bgram-string:`">="`

		: \ :bgram-string:`"<="`

		;

	.. _section-EqualityOperator:
	.. rst-class:: non-terminal

	EqualityOperator
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

		: \ :bgram-string:`"&="`

		: \ :bgram-string:`"|="`

		: \ :bgram-string:`">>="`

		: \ :bgram-string:`"<<="`

		;

	.. _section-PrefixUnaryOperator:
	.. rst-class:: non-terminal

	PrefixUnaryOperator
		: \ :bgram-string:`"-"`

		: \ :bgram-string:`"+"`

		: \ :bgram-string:`"++"`

		: \ :bgram-string:`"--"`

		: \ :bgram-string:`"not"`

		;

	.. _section-PostfixUnaryOperator:
	.. rst-class:: non-terminal

	PostfixUnaryOperator
		: \ :bgram-string:`"++"`

		: \ :bgram-string:`"--"`

		: \ :ref:`ArgumentList<section-ArgumentList>`

		: \ :ref:`ArrayAccess<section-ArrayAccess>`

		: \ :ref:`MemberAccessOperator<section-MemberAccessOperator>` \ :ref:`PostfixUnaryExpression<section-PostfixUnaryExpression>`

		;

	.. _section-MemberAccessOperator:
	.. rst-class:: non-terminal

	MemberAccessOperator
		: \ :bgram-string:`"."`

		;

	.. _section-ArgumentList:
	.. rst-class:: non-terminal

	ArgumentList
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
		: \ :ref:`Variable<section-Variable>`

		: \ :ref:`Constant<section-Constant>`

		: \ :ref:`IfThenElse<section-IfThenElse>`

		: \ :ref:`Return<section-Return>`

		: \ :ref:`Expression<section-Expression>`

		;

	.. _section-Variable:
	.. rst-class:: non-terminal

	Variable
		: \ :bgram-string:`"var"` \ :ref:`Name<section-Name>` \ ( \ :bgram-string:`":"` \ :ref:`TypeReference<section-TypeReference>` \ )\ ? \ ( \ :bgram-string:`"="` \ :ref:`Expression<section-Expression>` \ )\ ?

		;

	.. _section-Constant:
	.. rst-class:: non-terminal

	Constant
		: \ :bgram-string:`"const"` \ :ref:`Name<section-Name>` \ ( \ :bgram-string:`":"` \ :ref:`TypeReference<section-TypeReference>` \ )\ ? \ :bgram-string:`"="` \ :ref:`Expression<section-Expression>`

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

