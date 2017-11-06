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


Access Modifiers
----------------

Classes and class members can have access modifiers. These modifiers define the visibility of the member and are mutually exclusive. Unlike Java or C#, access modifiers are not specified using keywords. Instead, they are specified by using annotations.

Public
    Visible to everyone

Module
    Visible to every class inside the current module.

Package
    Visible to every class inside the same package.

Protected
    Visible to every descendant (members) or compilation unit (types).

Private
    Only visible to the current class (members). This modifier cannot be used with types.

For example, to change the access modifier for a class, one could write:

.. code-block:: beagle

    @Package
    class Foo

Additionally, you can combine the annotation ``Static`` to indicate the member is accessible statically:

* Static variables and constants are stored in the class definition (i.e. they are shared among all instances) instead of type instances.
* Static methods can only access static members of the type (i.e. there is no ``this`` instance).
