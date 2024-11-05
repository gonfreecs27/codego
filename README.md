# CodeGo

## Introduction
Designing a new programming language using Filipino terms for data types, control structures, and syntax makes coding more accessible to Filipinos, especially aspiring developers. In this paper, we present CodeGO, named for "code" and "GO," symbolizing speed and efficiency in development. The name also connects to the Filipino term "kodigo," emphasizing its target audience and local relevance.
 
A key challenge for Filipino developers is the language barrier in existing programming languages, which are often based on English. This adds complexity for those unfamiliar with English terms, leading to a steep learning curve. CodeGO addresses this by using Filipino terminology, making programming more relatable and reducing cognitive load for both beginners and experienced developers. Its cultural relevance fosters pride and confidence in local developers.
 
CodeGO also tackles inefficiencies in web development, particularly in small to medium-sized projects where rapid prototyping is crucial. By simplifying syntax and providing built-in functions, CodeGO reduces redundant coding, enabling developers to focus on functionality and user experience.
 
Compared to languages like Python and JavaScript, known for their simplicity and speed, CodeGO offers similar functionality but in a more familiar context for Filipinos. Designed for rapid web development, it supports front-end and back-end technologies like HTML, CSS, and JavaScript equivalents, while streamlining the development process.
 
By minimizing redundant coding and offering intuitive Filipino-based syntax, CodeGO meets the demand for efficient web development tools. It empowers developers to focus on innovation, bridging the gap between programming and local culture to boost productivity in the Philippine tech landscape.


## Basic Data Types

**Numero (Integer)** – data type for positive and negative integers.

```
Numero a = 20
```

**Desimal (Float)** – used for decimal numbers

```
Desimal presyo = 100.50
```

**Teksto (String)** – used for text-type data.

```
Teksto pangalan = "CodeGo"
```

**Tsek (Boolean)** – used to represent true or false values (Tama, Mali).

```
Tsek mahalKaBa = Mali
```

**Lista (Array or List)** – used for arrays or lists of data. 

```
Lista mgaPangalan = ["Faderon", "Mendillo", "Olage"]
```

**Bagay (Object)** – equivalent to an object or a dictionary

```
Bagay customer = {
	id: 1000,
	pangalan: "Juan Tamad",
	...
}
```

## Control Structures

**Kung** – conditional statement equivalent to if statement in common languages.

```
Kung (bayad > total) {
    Desimal sukli = bayad – total
    # print is a built-in function to print all given arguments.
    print("May sukli na ", sukli)  
}
```

**Habang** – equivalent to while loop. Loops until a condition is met.

```
Habang (mayOrderPa) {
    print("Huwag ilimbag ang resibo")
}
```

**Bawat** – loops through an array of data equivalent to for loop or foreach statements.

```
# sample code to traverse in a Bagay data type 
Bagay luto = { ulam: "Pritong Itlog", presyo: 50.00 }
Bawat (key, value Sa luto) {
    print(key, ": ", value, "\n")
}
```

```
# sample code to traverse a list of objects
Lista menu = [{
    ulam: "Pritong Itlog",
    presyo: 50.00,
}, {
    ulam: "Adobo",
    presyo: 100.50,
}]

Bawat (luto Sa menu) {
    print("Ang ulam na ", luto.ulam, " ay may presyong ", luto.presyo, ".\n")
}
```

**Kapag** – equivalent to switch statement and an alternative to if-else statements.

```
Kapag (mahalKa) {
    Kaso "Oo":
        print("Edi Wow!")
        Hinto
    Kaso "Hindi":
      print("Hanap iba.")
      Hinto
}
```

## Functions and Classes

To define functions and methods:

```
# explicitly defining data types of function parameters is optional
# if explicitly defined, and argument’s type mismatched with the defined
# type, an exception will be thrown 
Gawa bayaran (Desimal bayad, Desimal presyo) {
    return bayad - presyo
}
```

To define a class:

```
Klase Customer {
    Teksto pangalan
    Numero edad
    Desimal dalangPera

    Gawa init() {}

    Gawa bumili (Lista order) {
        # ako is a reserved keyword to refer to the instance of this class
        print("Eto ang mga binili ni ", ako.pangalan)
    }
}
```

## Error Handling
•	Subukan (Try): block of codes to attempt for execution
•	Salo (Catch): to handle the thrown exception

```
Subukan {
    Kung (diMahal) {
        Bagong Kamalian("Di ka pogi")
    }
} Salo (Kamalian e) {
    print("Eto mali sayo: ", e.mensahe)
}
```


## Comments
Comments should start with the hashtag symbol #.

```
# Eto ay isang simpleng komento
print("Hello, World!")
```
