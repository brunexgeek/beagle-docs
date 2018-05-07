.. _section-CompulationUnit:

Compilation units
=================

Each source file is a compilation unit in Beagle. Compilation units contain:

* Optional package declaration
* Optional import declarations
* One or more type declarations

.. _section-CompilationUnit-Package:

Package declaration
-------------------

Every piece of code is organized in packages. Packages define logical groups, similar to C++ namespaces or Java packages, helping to prevent name collisions. Every package have a name and can contain several types (e.g. classes).

To indicate the package in a compilation unit, use the keyword ``package``. Package declarations, when present, must be the first statement in the source file.

.. code-block:: beagle

    package beagle.collection

.. Package names can be qualified, enabling hierarchical organization. The first name in a qualified name is the *root package*. Each :ref:`module<section-Module>` have its own *root package* and different modules cannot expand existing modules by using the same *root package*. This is done for security reasons. Without this restriction, one could inject untrusted classes inside an existing trusted package as if it was originally provided by the corresponding module creator.

You can omit package declarations by using qualified names in the type declaration. However, if both package declaration and type qualified name are present, the effect package name for the corresponding type is a concatenation of the both names.

.. code-block:: beagle

    package beagle

    // the package for "List" class is "beagle.foo"
    class foo.List
    // the package for "Password" class is "beagle.bar.baz"
    class bar.baz.Password

Note that unlike Java, Beagle do not enforce you to organize source files according to package names. You can put every source file in the same directory and still have a complex subpackage hierarchy.

.. _section-CompilationUnit-Import:

Import declaration
------------------

After the package declaration, you can include import declarations using ``import`` keyword. Import declarations enable you to use types declared in other compilation units without specifying their qualified names. Types inside the same compilation unit are automatically imported.

You can import a single type or every type inside a subpackage.

.. code-block:: beagle

    import beagle.collection.List
    import beagle.network.*

    ...
    var users : List   // OK!
    var numbers : Array // ERROR: who is "Array"?
    var hasher : beagle.security.SHA256 // if really exists, OK!

By default, Beagle import every type inside the package ``beagle`` and provide the following aliases:

======== ====== ========================
Type     Alias  Description
======== ====== ========================
int64    long   Signed integer 64-bits
int32    int    Signed integer 32-bits
int16    short  Signed integer 16-bits
int8            Unsigned integer 8-bits
uint64   ulong  Unsigned integer 64-bits
uint32   uint   Unsigned integer 32-bits
uint16   ushort Unsigned integer 16-bits
         char
uint8    byte   Unsigned integer 8-bits
float32  float  Float-point 32-bits
float64  double Float-point 64-bits
String   string Immutable string
======== ====== ========================

.. It's recommended to avoid importing entire subpackages since this can cause an unnecessary extra overhead in the compilation process.


Hashtags
--------

Hashtags enables you to associate meta-information to some Beagle statements. These meta-informations can be used by the compiler to perform special actions or to change the way tagged elements are processed during the compilation.

To add a hashtag to some statement, you must use the symbol ``#`` followed by the tag name. Tag names are any term starting with a alphabethic character, followed by any number of alphanumeric characters and dashes. For example, ``#myhastag`` and ``#a-very-long-hashtag-name`` are both valid hashtags.

.. code-block:: beagle

    #public #deprecated
    var name : string

Unrecognized hashtags are ignored by the compiler.


.. _section-AcessModifiers:

Access Modifiers
----------------

Variables, constants and functions can be tagged with hashtags that define the visibility of the element. These hashtags are mutually exclusive.

#public
    Visible everywhere

#module
    Visible inside the current module.

#package
    Visible inside the current package or subpackages (i.e. parent packages cannot access).

#protected
    Visible to every descendant (members inside classes) or inside the compilation unit (globals).

#private
    Only visible to the current class (members). This modifier cannot be used with types.

The following table shows when each hashtag is applicable considering the location of the element being tagged. For example, you cannot use ``#private`` in a global variable.

.. raw:: html

    <style>table.bgl-aligned tbody td, table thead th { text-align: center; }</style>

.. rst-class:: bgl-aligned

========== ====== ========= =====
Hashtag    Global Structure Class
========== ====== ========= =====
#public    X      X         X
#module    X      X         X
#package   X      X         X
#protected X                X
#private                    X
========== ====== ========= =====

For example, to change the access modifier for a class, one could write:

.. code-block:: beagle

    #package
    class Foo

.. _
    Additionally, you can combine the annotation ``Static`` to indicate the member is accessible statically:
    * Static variables and constants are stored in the class definition (i.e. they are shared among all instances) instead of type instances.
    * Static methods can only access static members of the type (i.e. there is no ``this`` instance).


Type system
-----------

Beagle uses a strong type system with type inference.

+---------+-------------+-------------------------------------------------------------+
|Category |Type         |Description                                                  |
+=========+=============+=============================================================+
| Basic   | long        | Signed integer 64-bits                                      |
|         +-------------+-------------------------------------------------------------+
|         | int         | Signed integer 32-bits                                      |
|         +-------------+-------------------------------------------------------------+
|         | short       | Signed integer 16-bits                                      |
|         +-------------+-------------------------------------------------------------+
|         | byte        | Signed integer 8-bits                                       |
|         +-------------+-------------------------------------------------------------+
|         | ulong       | Unsigned integer 64-bits                                    |
|         +-------------+-------------------------------------------------------------+
|         | uint        | Unsigned integer 32-bits                                    |
|         +-------------+-------------------------------------------------------------+
|         | ushort      | Unsigned integer 16-bits                                    |
|         +-------------+-------------------------------------------------------------+
|         | char        | Unsigned integer 16-bits                                    |
|         +-------------+-------------------------------------------------------------+
|         | ubyte       | Unsigned integer 8-bits                                     |
|         +-------------+-------------------------------------------------------------+
|         | float       | Float-point 32-bits                                         |
|         +-------------+-------------------------------------------------------------+
|         | double      | Float-point 64-bits                                         |
|         +-------------+-------------------------------------------------------------+
|         | string      | Immutable string                                            |
+---------+-------------+-------------------------------------------------------------+
| Complex | array       | Fixed size sequence of elements (any type)                  |
|         +-------------+-------------------------------------------------------------+
|         | structure   | Custom type containing variables                            |
|         +-------------+-------------------------------------------------------------+
|         | object      | Custom type containing variables, constants and functions   |
+---------+-------------+-------------------------------------------------------------+

