# Understanding Complex Data Structures

![outcome](./01.JPG)

# Module Overview

![outcome](./02.JPG)

# What about Blockchain?

![outcome](./03.JPG)

# Complex Data Structure Requirements

## A Transaction

![outcome](./04.JPG)

## A Block

![outcome](./05.JPG)

## Managing List of Paricipants

![outcome](./06.JPG)

## Iterables Overview

![outcome](./07.JPG)

## Choosing the right data structure: Refer to the Transaction, A Block and Manging List of Participants above
 
 For Transaction: We need Key value pair, we require Dictionary
 
 For List of transactions: We need List
 
 For Blockchain itself: We need List
 
 For Block: Dictionary
 
 For List of participants: Set, for storing unique values
 
## Blockchain Theory: Understanding Transactions

As mentioned earlier, a Blockchain is all about storing data in Blocks. And for a Cryptocurrency, that data are Transactions (NOT Coins!).

Transactions typically require three pieces of information:

•	Who sends the coins? [sender ]
•	Who receives the coins? [recipient ]
•	How many coins are sent? [amount ]

A transaction is treated as an "Open Transaction" until it's included in a new block. Only transactions that are part of a block have been "processed" and their attached amounts are hence available to the recipient.

One Block typically contains more than one Transaction - in this course, we'll simply add all open transactions. Once the Block has been created, the "Open Transactions" are of course cleared.

## Transactions with Dictionaries and tuples

![outcome](./08.JPG)

Tuple Unpacking

Refer to the **blockchain1.py** code 

![outcome](./09.JPG)

![outcome](./10.JPG)

## Mining blocks and hashing previous block

Refer to the **blockchain2.py** code

![outcome](./11.JPG)

![outcome](./12.JPG)

## List Comprehensions

![outcome](./13.JPG)

Refer to the **blockchain3.py** code

![outcome](./14.JPG)

## Dictionary Comprehensions

![outcome](./15.JPG)

## List Comprehensions and if

![outcome](./16.JPG)

## Improved blockchain Validation logic 

![outcome](./17.JPG)

Define new function hash_block(), mine_block() call hash_block(last_block), update the code in verify_chain()

## Manging List of Participants

![outcome](./18.JPG)

![outcome](./19.JPG)

![outcome](./20.JPG)

Refer to the **blockchain4.py** code 

## Calculating Balances

Updates a get_Balance()

## Rewarding Miners

Whenever a Miners create a new block, he needs to be rewarded i.e coins

## Verifying Transactions

Defines verify_transaction()

## Reference Vs Value Copying

![outcome](./21.JPG)

![outcome](./22.JPG)

![outcome](./23.JPG)

![outcome](./24.JPG)

Refer to the **blockchain5.py** code 

## Range Selector

![outcome](./25.JPG)

## Shallow vs Deep Copying

![outcome](./26.JPG)

![outcome](./27.JPG)

## Iterable methods

Refer to Data structures in Pyhton.org for the methods involved in various data structures used in python

## all and any

![outcome](./28.JPG)

Refer to the **blockchain6.py** code

An addidtional feature to check transaction validity, define verify_transactions()

## Iterables Overview

![outcome](./29.JPG)

Unpacking:

![outcome](./30.JPG)

![outcome](./31.JPG)

![outcome](./32.JPG)

![outcome](./Capture.JPG)

## Module Summary

![outcome](./34.JPG)

![outcome](./35.JPG)

### Refer to **blockchain_final_module.py** for the complete implementation of this module

## Useful Resources & Links

•	More on Data Structures: https://docs.python.org/3/tutorial/datastructures.html


















 
 


