A struct in the C programming language (and many derivatives) is a composite data type (or record) declaration that defines a physically grouped list of variables under one name in a block of memory, allowing the different variables to be accessed via a single pointer or by the struct declared name which returns the same address. The struct data type can contain other data types so is used for mixed-data-type records such as a hard-drive directory entry (file length, name, extension, physical address, etc.), or other mixed-type records (name, address, telephone, balance, etc.).

The C struct directly references a contiguous block of physical memory, usually delimited (sized) by word-length boundaries. It corresponds to the similarly named feature available in some assemblers for Intel processors. Being a block of contiguous memory, each field within a struct is located at a certain fixed offset from the start.

Because the contents of a struct are stored in contiguous memory, the sizeof operator must be used to get the number of bytes needed to store a particular type of struct, just as it can be used for primitives. The alignment of particular fields in the struct (with respect to word boundaries) is implementation-specific and may include padding, although modern compilers typically support the #pragma pack directive, which changes the size in bytes used for alignment.[1]

In the C++ language, a struct is identical to a C++ class but has a different default visibility: class members are private by default, whereas struct members are public by default.

In other languages
The struct data type in C was derived from the ALGOL 68 struct data type.[2]

Like its C counterpart, the struct data type in C# (Structure in Visual Basic .NET) is similar to a class. The biggest difference between a struct and a class in these languages is that when a struct is passed as an argument to a function, any modifications to the struct in that function will not be reflected in the original variable (unless pass-by-reference is used).[3]

This differs from C++, where classes or structs can be statically allocated or dynamically allocated either on the stack (similar to C#) or on the heap, with an explicit pointer. In C++, the only difference between a struct and a class is that the members and base classes of a struct are public by default. (A class defined with the class keyword has private members and base classes by default.)

Declaration
The general syntax for a struct declaration in C is:

struct tag_name {
   type member1;
   type member2;
   /* declare as many members as desired, but the entire structure size must be known to the compiler. */
};
Here tag_name is optional in some contexts.

Such a struct declaration may also appear in the context of a typedef declaration of a type alias or the declaration or definition of a variable:

typedef struct tag_name {
   type member1;
   type member2;
} struct_alias;
Initialization
There are three ways to initialize a structure. For the struct type

/* Declare the struct with integer members x, y */
struct point {
   int    x;
   int    y;
};
C89-style initializers are used when contiguous members may be given.[4]

/* Define a variable p of type point, and initialize its first two members in place */
struct point p = { 1, 2 };
For non contiguous or out of order members list, designated initializer style[5] may be used

/* Define a variable p of type point, and set members using designated initializers */
struct point p = { .y = 2, .x = 1 };
If an initializer is given or if the object is statically allocated, omitted elements are initialized to 0.[6]

A third way of initializing a structure is to copy the value of an existing object of the same type

/* Define a variable q of type point, and set members to the same values as those of p */
struct point q = p;
Assignment
A struct may be assigned to another struct. A compiler might use memcpy() to perform such an assignment.

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
Pointers to struct
Pointers can be used to refer to a struct by its address. This is useful for passing structs to a function. The pointer can be dereferenced using the * operator. The -> operator dereferences the pointer to struct (left operand) and then accesses the value of a member of the struct (right operand).

struct point {
   int x;
   int y;
};
struct point my_point = { 3, 7 };
struct point *p = &my_point;  /* p is a pointer to my_point */
(*p).x = 8;                   /* set the first member of the struct */
p->x = 8; 
