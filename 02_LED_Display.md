# How to write KOBA
### Putting stuff on the display
```
// 1, 2
disp[r0] b11111010
disp[g0] b10101010
// 3
disp[r1]
rreg[CRA]
disp[g1]
radr
```
What is going on:
1. The specific row to be written to is encoded in the instruction, so the instruction decoder needs to reset the display counter to be the correct value.
2. The instruction decoder also tells whichever color is going to be written to to parallel load the data line.
3. The "write lock" system demonstrated in the previous tutorial also applies to the display for writing arbitrary data

Things to keep in mind:
* You cannot read the data currently on the display
* Keeping that in mind, if you just want to change one pixel, you need to have the previous value stored somewhere in memory in order to not overwrite any other currently lit pixels.
* You cannot programmatically specify what row to write to, so it's a good idea to have some sort of "display flipping" function that takes all the values in some region of memory and successively puts them on the display
* `disp` counts as a write instruction, and will interrupt any previous write instructions