Basics
======

Statements
----------

Statements are syntatic elements that perform some action. There are different categories of statements that perform certain classes of actions, like assignments and control flow.

.. code-block:: beagle

    x = 10   // an assignment
    return x // a return

Expressions
-----------

Expressions are syntatic elements that produce a result. They are composed by any kind of `rvalues <https://en.wikipedia.org/wiki/Value_(computer_science)#lrvalue>`_ (e.g. constants and variables) and operators.

.. code-block:: beagle

    // expression (multiplication) composed by two
    // subexpressions (constant and method call)
    5 * getQuantity()



Constants
---------

Constants are read-only and limited-scope storages for results of expressions. You can create constants using the ``const`` keyword. Constants must be initialized when declared.

.. code-block:: beagle

	const result = 5 * 4 / 2   // 'int' constant
	Console.print(result)      // 10

Usually, the type of the constant can be inferred by the compiler in the moment of the declaration by inspecting the initialization value. In the above example, the compiler will infer the type is ``int``. You can also specify manually the type using the following syntax:

.. code-block:: beagle

	const result : int = 5 * 4 / 2   // explicitly an 'int' constant

Being read-only, constants cannot be changed after initialization.

.. code-block:: beagle

	const result = 5 * 4 / 2
	result = 0  // compilation error!


Variables
---------

Variables are read-write and limited-scope storages. They are pretty much like constants, but their content can change after initialization. Variable declarations are made using the ``var`` keyword. Like with constants, the compiler usually can infer the variable type.

.. code-block:: beagle

	var result = 0
	result = 16 / 2

Since variables are read-write storages, you are not required to initialize them in the declaration. In this case, you will be required to provide the variable type and the compiler will try to give it a default initialization value.

.. code-block:: beagle

    var result : int  // initialized with 0 by default
    result = 16 / 2

If the compiler cannot assign a default value (e.g. variable of class without empty constructor) a compilation error will be raised.

Blocks
------

A block is a statement that group one or more expressions inside a scope. Blocks are delimited with ``{`` and ``}``. Expressions inside blocks are separated from each other by line breaks.

.. code-block:: beagle

    {
       const x = 10 * 5
       var y = x + 2
       return y * x
    }

Variables and constants declared inside a block are only visible from the point they are defined until the end of the block, including nested blocks.

.. code-block:: beagle

    {
       const x = 10 * 5
       {
          var y = x + 2  // we can use 'x' here!
       }
       return y * x   // 'y' is not accessible here!
    }

..  You can also use blocks to create anonymouns functions without parameters. This use of blocks will be discussed later.

    .. code-block:: beagle

        const x = 10

        // print 100
        Console.print({
            return 10 * x
        })

.. _section-functions:

Functions
---------

Beagle introduces the concept of functional programming with `anonymous functions <https://en.wikipedia.org/wiki/Anonymous_function>`_. These functions can receive arguments, contain one or more expressions and return a result. When using more than one expression, you must put them inside a block.

.. code-block:: beagle

    // function with single expression
    (x : int) : int => return x * x

    // a little more complex function
    (x : int, y : int) : int => {
        var z = x * y
        return z
    }

Return type can be omited if the compiler can deduce it.

.. code-block:: beagle

    (x : int) => return x * x

Functions are `first-class citizens <https://en.wikipedia.org/wiki/First-class_citizen>`_ so you can assign them to variables or pass as arguments for other functions or methods.

.. code-block:: beagle

    var function = (a : int, b : int) => return a < b
    var numbers = 10..0
    numbers.sort(function)

..  If the function does not require any parameter, the parameter list can be omited completely.

    .. code-block:: beagle

        Console.print({
            const x = 10
            var y = x + 6
            return y
        });
