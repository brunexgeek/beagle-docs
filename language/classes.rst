.. _section-Classes:

Classes
=======

In Beagle you build applications and frameworks using classes. Classes are defined using the ``class`` keyword followed by a name and an optional class body.

.. code-block:: beagle

    class Empty

    class Rectangle
    {
        var x, y, width, height : int
    }

Objects are created from classes using the ``new`` keyword.

.. code-block:: beagle

    var rect = new Rectangle

Classes can contain methods, variables and constants. Every element inside a class is denoted as class member.

.. _section-Classes-Methods:

Methods
-------

Methods are functions identified by name and bound to a class. You can define methods using the keyword ``def``.

.. code-block:: beagle

    def multiply( a : int, b : int ) : int
    {
        return a * b
    }

Methods are similar to :ref:`functions <section-functions>`. However, methods use blocks even when there is only one expression and don't use the operator ``=>`` before the block.

.. _section-Classes-Modifiers:

Annotations
-----------

Annotations enable the programmer to introduce meta-informations to types or type members. These informations can be used by the compiler to perform special actions or to change the way annotated elements are processed during the compilation process. An annotation is a special class that extends ``Annotation`` class.

To append an annotation to some element, you must use the symbol ``@`` followed by the annotation type name.

.. code-block:: beagle

    class Something {
        @Public
        var name : String
    }

In the example above, the member variable ``name`` is annotated with the ``Public`` annotation, which tells the compiler to apply public visibility to that member.


