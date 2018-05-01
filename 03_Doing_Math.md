# How to write KOBA
### Doing Math
```
// 1
wreg[AIA] 2
wreg[AIB] 2
// 2
math[pab]
// 3
wreg[CRA]
rreg[AOC]
```
What is going on:
1. Load the literal value 2 to both ALU input registers (A and B)
2. Tell the ALU to perform the addition operation on its inputs
3. Write the result of the addition operation to Cache Register A

Things to keep in mind:
* The AIA and AIB registers can not be read from, and the AOR can not be written to.
