Modules
=======

A module is a binary file containing one or more :ref:`compilation units <section-CompulationUnit>`. Everytime you compile Beagle code, the compiler creates a module.

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

.. _section-CompilationUnit-Type:

Type declarations
-----------------

See :ref:`section-Classes`.