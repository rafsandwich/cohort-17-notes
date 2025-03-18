# Modelling the problem

## Data type

### Primitives
string - immutable
char - a single string item
integer - a number
float - floating point number
bool - True or False

### Complex 
Set - unordered unique list of values
Dictionary - sets of key pairs
List - ordered thing of things
Tuple - (this, thing) 

### Structures
Trees - Parent-child relationships
Queues - FIFO first in first out
Stacks - FILO First in last out

Example: Advent of code

```txt
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
```

`[sum([elf 1]) [elf 2]]`

### Example 2

I have a `list` of colours, I want to know how many of each colour


Example: `["red", "blue", "red", "green", "blue", "blue"]` would give us as a string `{"red: 2, blue: 3, green: 1}`"

Example: ["red", "blue", "red", "green", "blue", "blue", "green", "green", "green"] would give us as a string "red: 2, blue: 3, green: 4"

### The problem

Write a function which receives 4 digits and returns the latest time of day that can be built with those digits.

The time should be in HH:MM format.

Examples:

1, 9, 8, 3 => "19:38"

9, 1, 2, 5 => "21:59" ("19:25" is also a valid time, but 21:59 is later)`

Notes

Result should be a valid 24-hour time, between 00:00 and 23:59.
Only inputs which have valid answers are tested.

### Algorithm

Set of instructions

A procedure used to solve a problem or a description of a process to arrive at an outcome/solution.



Hour - 2 digits

0, 1, 2

0-9
IF first digit is 0 or 1

ELSE 0-3

Minutes - 2 digits

0-5

0-9


## Refactoring

Code Smells: things that make your code bad

- Duplicate code
- Magic numbers (global variables)
- Commented out code
- Type hints (or lack of)
- Function names
- Variable names

## Time and Space complexity

O(n) - Big O notation

![alt text](image.png)