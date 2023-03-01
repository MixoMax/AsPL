Ascii Programming Language
==========================

AsPL is a totally not esoteric programming language, and is used by many many people.


# Design philosophy

The Design Philophy behind AsPL is just as simple as writing AsPL: "Why use more than one character when one will do?" or as the AsPL community calls it, "One character to rule them all."


# Syntax
Basic Syntax
------------
- "+" increments the value of the current cell
- "-" decrements the value of the current cell
- ">" moves the pointer to the right
- "<" moves the pointer to the left
- "r" resets the current cell to 0
- "p" prints the current cell value
- "c" prints the current cell as a character
- "i" takes input and stores it in the current cell
- "s" takes input and stores it in the current cell as a character
- "a" print all cells != 0 as a string of characters
- "h" holds the program until Enter is pressed

it is advised to use the "h" command at the end of the program, as it will prevent the program from closing before you can see the output.

Advanced Syntax
---------------
complex functions are made by using command blocks
- "[" starts a command block
- "]" ends a command block

Each command block consists of the command and the argumens, seperated by a comma.
the commands are:

- "[f, x]" finds the first cell with the value x and moves the pointer to it
- "[b, x]" sets the current pointer to x
- "[l, x]" sets the current cell to the roman numeral x
- "[o, x]" sets the current cell to the ordinal value of the character x


# Examples
Hello World
-----------
    [o,H]>[o,e]>[o,l]>[o,l]>[o,o]>[o, ]>[o,w]>[o,o]>[o,r]>[o,l]>[o,d]<<<<<<<<<<<ah

This program prints "Hello World" by using the ordinal value of each character to set the current cell to the ordinal value of the character, then printing all cells != 0 as a string of characters.

# How to use

to register .aspl files, run register_AsPL.py as admin

to run .aspl files, double click them or run them with python using:

    python run_Aspl.py <file_path>


# How to contribute

for minor additions / bug fixes, just make a pull request or fork the repo.

for major additions / bug fixes, make an issue first, so we can discuss it.


# Credits

developed by [@MixoMax](https://github.com/MixoMax)

# License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

# Acknowledgments

- [Esolangs](https://esolangs.org/wiki/AsPL)
