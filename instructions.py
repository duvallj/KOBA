from collections import namedtuple

Instruction = namedtuple(
    "Instruction",
    [
        "opcode",           # What this instruction will be written as in assembly
        "bit_mask",         # Controls how much of the id is taken
        "bit_id",           # How the code should be represented in binary. Should defintely be unique
        "bit_mapping",      # Maps code words to bit endings
    ]
)

"""
alu logic based off of 74LS181 chip
all logic opcodes are expressed in prefix notation to denote their function
code(arguments) = description

a(0) = register a
b(0) = register b
i(1) = invert argument
o(2) = or arguments
x(2) = xor arguments
n(2) = and arguments
p(2) = add arguments
m(2) = subtract 2nd argument from the 1st
"""

alu_l = Instruction(
    opcode   = "logic",
    bit_mask = 0b11110000,
    bit_id   = 0b00010000,
    bit_mapping = {
        'ia':       0b0000,
        'oiaib':    0b0001,
        'niab':     0b0010,
        '0':        0b0011,
        'niaib':    0b0100,
        'ib':       0b0101,
        'xab':      0b0110,
        'naib':     0b0111,
        'oiab':     0b1000,
        'xiaib':    0b1001,
        'b':        0b1010,
        'nab':      0b1011,
        '1':        0b1100,
        'oaib':     0b1101,
        'oab':      0b1110,
        'a':        0b1111,
    }
)

alu_math = Instruction(
    opcode   = "math",
    bit_mask = 0b11110000,
    bit_id   = 0b00000000,
    bit_mapping = {
        'UNUSED_1': 0b0000,
        'UNUSED_2': 0b0001,
        'UNUSED_3': 0b0010,
        'UNUSED_4': 0b0011,
        'panaib':   0b0100,
        'poabnabi': 0b0101,
        'mamb1':    0b0110,
        'mnab1':    0b0111,
        'panab':    0b1000,
        'pab':      0b1001,
        'poabinab': 0b1010,
        'UNUSED_5': 0b1011,
        'paa':      0b1100,
        'poaba':    0b1101,
        'poaiba':   0b1110,
        'ma1':      0b1111,
    }
)
"""                  Registers!
Code    |   Name            |   (R)ead/(W)rite/(B)oth       |   Number
--------|-------------------|-------------------------------|--------------
AIA     | ALU Input A       |               W               |   0 / 0b0000
AIB     | ALU Input B       |               W               |   1 / 0b0001
AOC     | ALU Output        |               R               |   2 / 0b0010
ABRA    | Addr Bus Reg A-LSB|               W               |   3 / 0b0011
ABRB    | Addr Bus Reg B-MSB|               W               |   4 / 0b0100
CRA     | Cache Register A  |               B               |   5 / 0b0101
CRB     | Cache Register B  |               B               |   6 / 0b0110
CRC     | Cache Register C  |               B               |   7 / 0b0111
CRD     | Cache Register D  |               B               |   8 / 0b1000
PINA    | Player Input A    |               R               |   9 / 0b1001
PINB    | Player Input B    |               R               |  10 / 0b1010
NULC    | Null Register C   |              N/A              |  11 / 0b1011
NULD    | Null Register D   |              N/A              |  12 / 0b1100
NULE    | Null Register E   |              N/A              |  13 / 0b1101
NULF    | Null Register F   |              N/A              |  14 / 0b1110
BLCK    | Blockchain Reg    |               B               |  15 / 0b1111
"""

read_reg = Instruction(
    opcode   = "rreg",
    bit_mask = 0b11110000,
    bit_id   = 0b01000000,
    bit_mapping = {
        'AIA':  0b0000,
        'AIB':  0b0001,
        'AOC':  0b0010,
        'ABRA': 0b0011,
        'ABRB': 0b0100,
        'CRA':  0b0101,
        'CRB':  0b0110,
        'CRC':  0b0111,
        'CRD':  0b1000,
        'NULA': 0b1001,
        'NULB': 0b1010,
        'NULC': 0b1011,
        'NULD': 0b1100,
        'NULE': 0b1101,
        'NULF': 0b1110,
        'BLCK': 0b1111,
    }
)

write_reg = Instruction(
    opcode   = "wreg",
    bit_mask = 0b11110000,
    bit_id   = 0b10000000,
    bit_mapping = {
        'AIA':  0b0000,
        'AIB':  0b0001,
        'AOR':  0b0010,
        'ABRA': 0b0011,
        'ABRB': 0b0100,
        'CRA':  0b0101,
        'CRB':  0b0110,
        'CRC':  0b0111,
        'CRD':  0b1000,
        'NULA': 0b1001,
        'NULB': 0b1010,
        'NULC': 0b1011,
        'NULD': 0b1100,
        'NULE': 0b1101,
        'NULF': 0b1110,
        'BLCK': 0b1111,
    }
)

# color     row     column
# g / r     0 - 15  0 - 1
write_disp = Instruction(
    opcode   = "disp",
    bit_mask = 0b11100000,
    bit_id   = 0b11000000,
    bit_mapping = {
        'g0':    0b00000,
        'g1':    0b00001,
        'g2':    0b00010,
        'g3':    0b00011,
        'g4':    0b00100,
        'g5':    0b00101,
        'g6':    0b00110,
        'g7':    0b00111,
        'g8':    0b01000,
        'g9':    0b01001,
        'gA':    0b01010,
        'gB':    0b01011,
        'gC':    0b01100,
        'gD':    0b01101,
        'gE':    0b01110,
        'gF':    0b01111,
        'r0':    0b10000,
        'r1':    0b10001,
        'r2':    0b10010,
        'r3':    0b10011,
        'r4':    0b10100,
        'r5':    0b10101,
        'r6':    0b10110,
        'r7':    0b10111,
        'r8':    0b11000,
        'r9':    0b11001,
        'rA':    0b11010,
        'rB':    0b11011,
        'rC':    0b11100,
        'rD':    0b11101,
        'rE':    0b11110,
        'rF':    0b11111,
    }
)

read_address = Instruction(
    opcode   = "radr",
    bit_mask = 0b11111111,
    bit_id   = 0b00111111,
    bit_mapping = {}
)

write_address = Instruction(
    opcode   = "wadr",
    bit_mask = 0b11111111,
    bit_id   = 0b10111111,
    bit_mapping = {}
)

jump_unconditional = Instruction(
    opcode   = "jmp",
    bit_mask = 0b11111111,
    bit_id   = 0b00101001,
    bit_mapping = {}
)

jump_if_equal = Instruction(
    opcode   = "jie",
    bit_mask = 0b11111111,
    bit_id   = 0b00101010,
    bit_mapping = {}
)

jump_if_less = Instruction(
    opcode   = "jin",
    bit_mask = 0b11111111,
    bit_id   = 0b00101100,
    bit_mapping = {}
)

instructions = {
    alu_l.opcode : alu_l,
    alu_math.opcode : alu_math,
    read_reg.opcode : read_reg,
    write_reg.opcode : write_reg,
    write_disp.opcode : write_disp,
    read_address.opcode : read_address,
    write_address.opcode : write_address,
    jump_unconditional.opcode : jump_unconditional,
    jump_if_equal.opcode : jump_if_equal,
    jump_if_less.opcode : jump_if_less,
}
