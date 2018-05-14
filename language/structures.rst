.. _section-Structures:

Structures
==========

A structure is a composite data type that groups variables and constants.

.. code-block:: beagle

    struct Person
    {
        var name : string
        var age : int
    }


Structures can also be inherited. Inheritance enable one structure to reuse members from another structure. The derived structure cannot have any member with the same name as its parents.

.. code-block:: beagle

    struct Hero : Person
    {
        var abilities : int[]?
        var name : string  // ERROR: Person already have the member 'name'
    }

    struct Student : Person
    {
        var course : string
    }

Unless you give an initialization value, variables and constants inside structures will assume the default value for the corresponding type.

.. code-block:: beagle

    struct Fruit
    {
        var name : string   // empty string
        var weight : int    // 0
    }