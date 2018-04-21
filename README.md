# KOBA
Kind Of Bad Assembler. A homemade assembler for a homemade processor


# Kind Of Bad Assembly
How to write code for the assembler
## Numbers
Numbers can be represented many different ways.  
The ALU processes them as 2's complement signed ints.

| Base       | Representation                       | Example     | Equals (Binary/Decimal) |
|------------|--------------------------------------|-------------|-------------------------|
| Binary     | `b` followed by 8 bits               | `b00000011` | `00000011`/`3`          |
| Octal      | `@` followed by 3 octal digits       | `@037`      | `00011111`/`-1`         |
| Hexadecimal| `0x` followed by 2 hexi digits       | `0xFA`      | `11111010`/`-6`         |
| Decimal    | decimal number with +/- (any length) | `-2`        | `11111110`/`-2`         |
| Wildcard   | `*`, for when value doesn't matter   | `*`         | **UNDEFINED**           |

Note: the `*` wildcard number is technically undefined in value, but this specific assembler will always resolve it to 0.  However, this behaviour should not be depended on, and simply writing `0` will also produce a 0 with only one character.

###### Examples
| IN | BINARY OUT | DECIMAL OUT|
|----|------------|------------|
| `0xFF` | `11111111` | `-1` |
| `0x1F` | `00011111` | `31` |
| `@131` | `01011001` | `89` |
| `+8` | `00001000` | `8` |
| `+1` | `00000001` | `1` |
| `+0` | `00000000` | `0` |
| `0` | `00000000` | `0` |
| `-0` | `00000000` | `0` |
| `-1` | `11111111` | `-1` |
| `-6` | `11111010` | `-6` |
| `-128` | `10000000` | `-128` |
| `+126` | `01111110` | `126` |
| `+128` | `10000000` | `128` |
| `b01` | `00000001` | `1` |
| `b01111111` | `01111111` | `127` |