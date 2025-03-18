# Planning code

1. Read the problem
   - Really understand what it means
   - What goes into the problem (input: integer, list)
   - **What the answer looks like (output: integer, string)**

2. Write a plan
   - function signatures (`def function_name(input: int) -> int:`)
   - Figure out what the function does (does not mean code)
     - Uses a for loop to add numbers together
    - Excalidraw can help with flowcharts
    - Pen and paper helps

3. Write tests
   - Given a example, what should my function return
   - Most briefs give examples of inputs and outputs
     - If I give you `5`, the function should return `6`
   - Try to think yourself as a hacker trying to break the system
     - Try to "trick" your code into making a mistake
   - This is how you know your code works (running `pytest`)

4. Write the code
