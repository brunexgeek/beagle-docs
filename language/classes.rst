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

Methods
-------

Methods are functions identified by name and bound to a class. You can define methods using the keyword ``def``.

.. code-block:: beagle

    def multiply( a : int, b : int ) : int
    {
        return a * b
    }

Methods are similar to :ref:`functions <section-functions>`. However, methods use blocks even when there is only one expression and don't use the operator ``=>`` before the block.

Access Modifiers
----------------

Class member can have access modifiers. These modifiers define the visibility of the member and are mutually exclusive.

public
    Visible to everyone

protected
    Visible to every descendant.

package
    Visible to every class inside the same package.

module
    Visible to every class inside the current module.

private
    Only visible to the current class.

Additionally, you can combine the keyword ``static`` to indicate the member is accessible statically:

* Static variables and constants are stored in the class definition (i.e. they are shared among all instances) instead of class instances.
* Static methods can only access static members of the class (i.e. there is no ``this`` instance).
