# Context Free Grammar

This section defines the syntax of CodeGo language. To easily define and understood the syntax, we used a mix of Backus-Naur Form (BNF) and Extended Backus-Naur Form (EBNF) rules, BNF for simple expressions and EBNF for more complex expressions.


## Basic Components

For basic types:

```

<basic_type>    →   "Numero" | "Desimal" | "Teksto" | "Tsek" | "Lista" | "Bagay"

```


For identifiers:

```

<identifier>    →   <letter> { <letter> | <digit> }

<letter>	      →   [a-zA-Z_]

<digit> 	      →   [0-9]

```

For literals, which cover numeric, string and Boolean literals:

```

<literal>         →   <number_literal> | <string_literal> | <boolean_literal>

<number_literal>  →   <digit> { <digit> } [ "." { digit } ]

<string_literal>  →   '"' { <characters> } '"'

<boolean_literal> →   "Tama" | "Mali"

<characters>      →   <letter> | <digit> | <whitespace> | <punctuation> | <special_character>

<punctuation>     →   "." | "," | "!" | "?" | ":" | ";" | "'" | "\"" | "(" | ")" | "[" | "]" | "{" | "}"

<whitespace>      →   " " | "\t" | "\n" | "\r"

<special_character> → "@" | "#" | "$" | "%" | "^" | "&" | "*" | "-" | "+" | "="

```


For writing expressions:

```
<statements>    → { <statement> }
 
<statement>     → <var_declaration> | <conditional_statement> | <loop_statement> | <comment> | <whitespace> | <function_statement> | <class_statement> | <error_handling>

<expression>    → <term> { <operator> <term> } | <lambda_function>

<operator>      → "+" | "-" | "*" | "/" | ">" | "<" | ">=" | "<="

<term>          → <identifier> | <literal> | "(" <expression> ")"

```


## Variable Declarations

For variable declarations, we declared thru key-pair assignment using the following rule:

Rules:

```

<var_declaration>	→ [<basic_type>] <identifier> [ "=" <expression> ]

```

Examples:

```

Numero a = 20

Teksto pangalan = "CodeGo"

Bagay customer = {
	id: 1000,
	pangalan: "Juan Tamad",
	...
}

x = 5

```

## Conditional Statements

To define the basic structure for writing decision-making logic, we used the following syntax rules:

Rules:

```

<conditional statement>   → <kung_statement> | <kapag_statement>

<kung_statement>          → "Kung" "(" <expression> ")" "{" <statements> "}"

<kapag_statement>         → "Kapag" "(" <expression> ")" "{" ("Kaso" <expression> ":" <statements> "Hinto")+ "}"

```

Examples:

```

Kung (bayad > total) {
	Desimal sukli = bayad – total
	# print is a built-in function to print all given arguments.
	print("May sukli na ", sukli)  
}

Kapag (mahalKa) {
	Kaso "Oo":
		print("Edi Wow!")
		Hinto
	Kaso "Hindi":
		print("Hanap iba.")
		Hinto
}

```

## Loop Statements

To support block of codes to be executed repeatedly, we define the looping structure as follows:

Rules:

```

<loop_statement> → <habang_statement> | <bawat_statement>

<habang_statement> → "Habang" "(" <expression> ")" "{" <statements> "}"

<bawat_statement> → "Bawat" "(" (<identifier> | <identifier> "," <identifier>) "Sa" <identifier> ")" "{" <statements> "}"

```

Examples:


```

Habang (mayOrderPa) {
	print("Huwag ilimbag ang resibo")
}

Bagay luto = { ulam: "Pritong Itlog", presyo: 50.00 }
Bawat (key, value Sa luto) {
	print(key, ": ", value, "\n")
}

Lista menu = [{
	ulam: "Pritong Itlog",
	presyo: 50.00,
}, {
	ulam: "Adobo",
	presyo: 100.50,
}]

Bawat (luto Sa menu) {
	print("Ang ulam na ", luto.ulam, " ay may presyong ", luto.presyo)
}

```

## Function Statements

To design the syntax for reusable blocks of codes that perform specific tasks, we included the following components: 

Rules:

```

<function_statement>  → "Gawa" <identifier> "(" {[<basic_type>] <identifier>} ")" "{" <statements> "}"

<lambda_function>     → "(" [{<identifier>}] ")" "=" ">" "{" <statements> "}"

```

Examples:

```

Gawa bayaran (Desimal bayad, Desimal presyo) {
	return bayad - presyo
}

```


## Class Statements

We defined below syntax to support creating blueprints for objects:

Rules:

```

<class_statement> → "Klase" <identifier> "{" <class_props> <class_methods> "}"

<class_props>     → { <var_declaration> }

<class_methods>   → { <function_statement> }

```

Example:

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

For the process of detecting and responding to errors that may occur in the program, use below syntax:

Rules:

```

<error_handling> → "Subukan" "{" <statements> "}" "Salo" "{" <statements> "}"

```

Example:

```

Subukan {
	Kung (diMahal) {
		Bagong Kamalian("Di ka pogi")
	}
} Salo (Kamalian e) {
	print("Eto mali sayo: ", e.mensahe)
}

```

# Comments

Comments should start with the hashtag symbol #.

Rules:

```

<comment> → "#" <characters>

```

Example:

```

# Eto ay isang simpleng komento
print("Hello, World!")

```