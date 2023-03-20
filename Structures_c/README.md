A **struct** in the [C programming language](https://en.wikipedia.org/wiki/C_programming_language "C programming language") (and many derivatives) is a [composite data type](https://en.wikipedia.org/wiki/Composite_data_type "Composite data type") (or [record](https://en.wikipedia.org/wiki/Record_(computer_science) "Record (computer science)")) declaration that defines a physically grouped list of variables under one name in a block of memory, allowing the different variables to be accessed via a single [pointer](https://en.wikipedia.org/wiki/Pointer_(computer_programming) "Pointer (computer programming)") or by the struct declared name which returns the same address. The struct data type can contain other data types so is used for mixed-data-type records such as a hard-drive directory entry (file length, name, extension, physical address, etc.), or other mixed-type records (name, address, telephone, balance, etc.).

The C struct directly references a _contiguous block_ of physical memory, usually delimited (sized) by word-length boundaries. It corresponds to the similarly named feature available in some [assemblers](https://en.wikipedia.org/wiki/Assembly_language "Assembly language") for Intel processors. Being a block of contiguous memory, each field within a struct is located at a certain fixed offset from the start.

Because the contents of a struct are stored in contiguous memory, the [sizeof](https://en.wikipedia.org/wiki/Sizeof "Sizeof") operator must be used to get the number of bytes needed to store a particular type of struct, just as it can be used for [primitives](https://en.wikipedia.org/wiki/Primitive_data_type "Primitive data type"). The alignment of particular fields in the struct (with respect to [word](https://en.wikipedia.org/wiki/Word_(computer_architecture) "Word (computer architecture)") boundaries) is implementation-specific and may include padding, although modern compilers typically support the `#pragma pack` directive, which changes the size in bytes used for alignment.<sup id="cite_ref-1" class="reference"><a href="https://en.wikipedia.org/wiki/Struct_(C_programming_language)#cite_note-1">[1]</a></sup>

In the [C++](https://en.wikipedia.org/wiki/C%2B%2B "C++") language, a struct is identical to a [C++ class](https://en.wikipedia.org/wiki/C%2B%2B_classes "C++ classes") but has a different default visibility: class members are private by default, whereas struct members are public by default.

## In other languages\[[edit](https://en.wikipedia.org/w/index.php?title=Struct_(C_programming_language)&action=edit&section=1 "Edit section: In other languages")\]

The struct data type in C was derived from the [ALGOL 68](https://en.wikipedia.org/wiki/ALGOL_68 "ALGOL 68") struct data type.<sup id="cite_ref-sigplan_2-0" class="reference"><a href="https://en.wikipedia.org/wiki/Struct_(C_programming_language)#cite_note-sigplan-2">[2]</a></sup>

Like its C counterpart, the struct data type in [C#](https://en.wikipedia.org/wiki/C_Sharp_(programming_language) "C Sharp (programming language)") (_Structure_ in [Visual Basic .NET](https://en.wikipedia.org/wiki/Visual_Basic_.NET "Visual Basic .NET")) is similar to a [class](https://en.wikipedia.org/wiki/Class_(computer_programming) "Class (computer programming)"). The biggest difference between a struct and a class in these languages is that when a struct is passed as an argument to a function, any modifications to the struct in that function will not be reflected in the original variable (unless pass-by-reference is used).<sup id="cite_ref-3" class="reference"><a href="https://en.wikipedia.org/wiki/Struct_(C_programming_language)#cite_note-3">[3]</a></sup>

This differs from C++, where classes or structs can be statically allocated or dynamically allocated either on the stack (similar to C#) or on the heap, with an explicit pointer. In [C++](https://en.wikipedia.org/wiki/C%2B%2B "C++"), the only difference between a struct and a [class](https://en.wikipedia.org/wiki/C%2B%2B_classes "C++ classes") is that the members and base classes of a struct are [public](https://en.wikipedia.org/wiki/Access_modifiers "Access modifiers") by default. (A class defined with the `class` keyword has [private](https://en.wikipedia.org/wiki/Access_modifiers "Access modifiers") members and base classes by default.)

## Declaration\[[edit](https://en.wikipedia.org/w/index.php?title=Struct_(C_programming_language)&action=edit&section=2 "Edit section: Declaration")\]

The general syntax for a struct declaration in C is:

```
struct tag_name {
   type member1;
   type member2;
   /* declare as many members as desired, but the entire structure size must be known to the compiler. */
};

```

Here `tag_name` is optional in some contexts.

Such a `struct` declaration may also appear in the context of a [typedef](https://en.wikipedia.org/wiki/Typedef "Typedef") declaration of a type alias or the declaration or definition of a variable:

```
typedef struct tag_name {
   type member1;
   type member2;
} struct_alias;

```

## Initialization\[[edit](https://en.wikipedia.org/w/index.php?title=Struct_(C_programming_language)&action=edit&section=3 "Edit section: Initialization")\]

There are three ways to initialize a structure. For the `struct` type

```
/* Declare the struct with integer members x, y */
struct point {
   int    x;
   int    y;
};

```

_C89-style initializers_ are used when contiguous members may be given.<sup id="cite_ref-4" class="reference"><a href="https://en.wikipedia.org/wiki/Struct_(C_programming_language)#cite_note-4">[4]</a></sup>

```
/* Define a variable p of type point, and initialize its first two members in place */
struct point p = { 1, 2 };

```

For non contiguous or out of order members list, _designated initializer_ style<sup id="cite_ref-5" class="reference"><a href="https://en.wikipedia.org/wiki/Struct_(C_programming_language)#cite_note-5">[5]</a></sup> may be used

```
/* Define a variable p of type point, and set members using designated initializers */
struct point p = { .y = 2, .x = 1 };

```

If an initializer is given or if the object is [statically allocated](https://en.wikipedia.org/wiki/Static_memory_allocation "Static memory allocation"), omitted elements are initialized to 0.<sup id="cite_ref-6" class="reference"><a href="https://en.wikipedia.org/wiki/Struct_(C_programming_language)#cite_note-6">[6]</a></sup>

A third way of initializing a structure is to copy the value of an existing object of the same type

```
/* Define a variable q of type point, and set members to the same values as those of p */
struct point q = p;

```

## Assignment\[[edit](https://en.wikipedia.org/w/index.php?title=Struct_(C_programming_language)&action=edit&section=4 "Edit section: Assignment")\]

A struct may be assigned to another struct. A compiler might use `memcpy()` to perform such an assignment.

```
struct point {
    int x;
    int y;
};

int main(void)
{
    struct point p = { 1, 3 };        /* initialized variable */
    struct point q;                   /* uninitialized */
    q = p;                     /* copy member values from p into q */
    return 0;
}

```

## Pointers to struct\[[edit](https://en.wikipedia.org/w/index.php?title=Struct_(C_programming_language)&action=edit&section=5 "Edit section: Pointers to struct")\]

Pointers can be used to refer to a `struct` by its address. This is useful for passing structs to a function. The pointer can be [dereferenced](https://en.wikipedia.org/wiki/Dereference_operator "Dereference operator") using the `*` operator. The `->` operator dereferences the pointer to struct (left operand) and then accesses the value of a member of the struct (right operand).

```
struct point {
   int x;
   int y;
};
struct point my_point = { 3, 7 };
struct point *p = &my_point;  /* p is a pointer to my_point */
(*p).x = 8;                   /* set the first member of the struct */
p->x = 8; 
```
