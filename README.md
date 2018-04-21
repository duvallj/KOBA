# KOBA
Kind Of Bad Assembler. A homemade assembler for a homemade processor


# Kind Of Bad Assembly
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