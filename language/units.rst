Compilation units
=================

Each source file is a compilation unit in Beagle. Compilation units contains:

* Optional package declaration
* Optional import declarations
* One or more type declarations


Package declaration
-------------------

Every piece of code is organized in packages. Packages define logical groups, similar to C++ namespaces or Java packages, helping to prevent name collision. Every package have a name and can contain several types (e.g. classes).

To indicate the package in a compilation unit, use the keyword ``package``. Package declarations, when present, must be the first statement in the source file.

.. code-block:: beagle

    package beagle.collection

Package names can be qualified, enabling hierarchical organization. The first name in a qualified name is the *root package*. Each :ref:`module<section-Module>` have its own *root package* and different modules cannot expand existing modules by using the same *root package*.

.. note::

    This is done for security reasons. Without this restriction, one could inject untrusted classes inside an existing trusted package as if it was originally provided by the corresponding module creator.

You can omit package declarations by using qualified names in the type declaration. If both package declaration and type qualified name are present, the resulting package name for the corresponding type is a concatenation of the both names.

.. code-block:: beagle

    package beagle

    // the package for "List" class is "beagle.collection"
    class collection.List
    // the package for "Password" class is "beagle.security"
    class security.Password

Note that, unlike Java, Beagle do not enforce you to organize the source files according to package names. You can put every source file in the same directory and still have a complex subpackage hierarchy.

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

Note that you should avoid importing entire subpackages since this can cause an unnecessary extra overhead in the compilation process.
