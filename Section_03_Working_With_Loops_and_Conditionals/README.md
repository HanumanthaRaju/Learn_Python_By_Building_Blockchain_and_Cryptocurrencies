# Loops and Conditionals: Repeat and Check

## Module Overview

![outcome](./01.JPG)

## Blockchain Overview

![outcome](./02.JPG)

## Working with loops

![outcome](./03.JPG)

### Creating for loop
Refer to the loops-if-01-created-for-loop folder for the code

![outcome](./04.JPG)

### Creating While loop
Refer to the loops-if-02-created-while-loop folder for the code

![outcome](./05.JPG)

## Understanding Conditionals

![outcome](./06.JPG)

![outcome](./07.JPG)

### applying if else

![outcome](./08.JPG)

### Booleans

![outcome](./09.JPG)

### adding elif

![outcome](./10.JPG)

### Understanding break and continue

Refer to the loops-if-03-understanding-break-continue folder for the code

![outcome](./11.JPG)

![outcome](./10.JPG)

## Understanding is in 

![outcome](./12.JPG)

## the not keyword

![outcome](./13.JPG)

## Working with and/or

![outcome](./14.JPG)

## Grouping conditionals

![outcome](./15.JPG)

## Switch statements

There is no switch-case statement in python

## Blockchain Theory: Understanding Blockchain Verification

A core concept of the Blockchain technology is that individual Blocks should be connected. Each Block knows the Block coming prior to itself. So Block C knows Block B which in turn is aware of Block A.

What does "Know" mean though?

To ensure data integrity, a hash is calculated for each Block. We're not doing this yet but we'll add this functionality throughout the course.

For now, we simply store the complete value of Block B in Block C which then is stored in Block D - and so on.

This allows us to check whether a certain Block in the Blockchain still looks the way it looked like when the Block after it was added. So if we change Block B after we added Block C, Block C will recognize that because it saved a snapshot of Block B when it (=> Block C) was created.

This ensures that the Blockchain can't be manipulated by other users. If you change a value, the other Blocks coming after it will recognize that.

Of course, you could theoretically edit the entire Blockchain. We'll add more security mechanisms throughout the course to ensure that this also doesn't work. The relation between Blocks is a first important building block though.


## Verifying our blockchain

Refer to the loops-if-04-verifying-the-blockchain folder for the code

### Manipulating Blockchain

![outcome](./16.JPG)

### Checking our Blockchain

![outcome](./17.JPG)

![outcome](./18.JPG)

## Adding range function

Refer to the loops-if-05-adding-range folder for the code

![outcome](./19.JPG)

## Module Summary

![outcome](./20.JPG)

![outcome](./21.JPG)

# Useful Resources and Links

•	More on Loops: https://docs.python.org/3/tutorial/controlflow.html#for-statements

•	More on if Statements: https://docs.python.org/3/tutorial/controlflow.html#if-statements
















