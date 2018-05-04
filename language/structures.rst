.. _section-Structures:

Structures
==========


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
        var habilities : table<int>
        var name : string  // ERROR: Person already have the member 'name'
    }

    struct Student : Person
    {
        var course : string
    }