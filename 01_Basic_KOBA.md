# How to write KOBA
### Reading from ROM into cache
```
// 1, 2
wreg[CRA] b00110011
```
What is going on:
1. Output from the instruction ROM gets decoded and sent to the instruction decoder, which enables the latch on CRA only
2. Output from the data ROM gets put on the data bus, CRA latches onto it

Things to keep in mind:
* Literals are stored in-line in the program

### Reading and writing to RAM
*We want to read from RAM into CRA, write to RAM from CRB*
```
// 1
wreg[ABRA] b00100000
wreg[ABRB] b00000001
// 2
wreg[CRA]
radr
wreg[ABRB] b00000010
// 3
wadr
rreg[CRB]
```
What is going on:
1. We write to caches like earlier, only this time we write to the address cache.
    i. The first two most significant bits of ABRA control which device the rest of the address goes to. In KOBA, `00` points to RAM.
2. We set CRA to write, but don't specify any data. The assembler will fill in zeros as data for us.
3. Because of the way the KOBProcessor is designed, a write instruction will persist to the next clock cycle if the next instruction is not a write instruction. We call this a "write lock". This mechanism allows us to put anything on the data bus, in this case data from the RAM, decoded by the address decoder and sent to the RAM address pins, and re-latch the cache onto the new value.
4. Writing to the RAM works in a similar way as writing to the cache. The "write lock" functions exactly the same way for RAM, only this time the cache is putting something on the data bus.

Things to keep in mind:
* You can put a read instruction right after a write instruction for data transfer between locations.
* It is possible to read and write from more locations using the register addresses.
* If you want don't want to have the next non-write instruction write to the previous write instruction, you should insert a null write operation (`wreg[NULA]` is preferred) in between.