# Python Standard Library

## Module Overview

![outcome](./01.JPG)

## What about Blockchain

![outcome](./02.JPG)

## Python standard library

Google for python standard library and find out the rich set of library functions available in python

**import** statement is used in the code, to include the feature of the package in your implementation.

## importing packages

![outcome](./03.JPG)

## importing hashlib to create a unique hash

In the function hash_block(), we are generating the pseudo hash, we write the code for generating real hash

We will **import hashlib** to create hashes, instead of returning custom hash we give a call to SHA256 algorithm in hashlib, The value we pass is a block which is a dictionary which needs to be converted to string, so to convert string we **import json** package.

Refer to the **blockchain1.py file**, run it and check the hash generated

## Using other import syntax

Use aliases instead of the package name: **import hashlib as hl**

Restrict import to specif functions of a package: **from functools import reduce**

## The Proof of Work

### Adding Proof of Work

![outcome](./04.JPG)

### Proof of Work

![outcome](./05.JPG)

### Cheating the Blockchain

![outcome](./06.JPG)

## Adding Proof of work to our blockchain

Refer to **blockchain2.py code**

Define a **valid_proof()** function, it requires transactions, last_hash and proof number as arguments, function body is used to guess the new hash. We check the new hash generated whether ot is precceding with **two zero's**, this is our check to determine whether proof is valid.

Include a another function **Proof_of_work()** uses last_block and last_hash which calls last_block(), initialize proof to 0, have a loop to increment proof, until valid_proof() returns true, then return a proof

## Include proof of work in our mining function

Use prrof_of_work when we mine a block. In the **mine_block()** give a call to proof_of_work() which returns proof, in the block add the proof field and append to our blockchain. also add proof to our genesis block fir instance we initialize to 100.

Also we should ensure the **verify_chain()** to have an additional check to check if our new hash begins with two zero's, add a if block in it.

Mine a new block that gives the output as below: refer to the hashes generated till we find a valid hash

![outcome](./07.JPG)

![outcome](./08.JPG)

![outcome](./09.JPG)

![outcome](./10.JPG)

## Fixing a hash order fault

Our current mechanism foe generating a hash one flaw, Our block is defined as dictionary which is unordered. In **hash_block() function use the sort_keys=True**. **import another package collections by importing OrderDict which is to be used in add_tansaction()**. comment out the old transaction and create with OrderedDict().

Refer to **blockchain3.py** file

Test the blockchain with all the options.

## Spltting up our code

Refer to **Final_implementation folder** for the blockchain implemented in this module








