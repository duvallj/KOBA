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
AOR     | ALU Output        |               R               |   2 / 0b0010
ABRA    | Addr Bus Reg A-LSB|               W               |   3 / 0b0011
ABRB    | Addr Bus Reg B-MSB|               W               |   4 / 0b0100
CRA     | Cache Register A  |               B               |   5 / 0b0101
CRB     | Cache Register B  |               B               |   6 / 0b0110
CRC     | Cache Register C  |               B               |   7 / 0b0111
CRD     | Cache Register D  |               B               |   8 / 0b1000
NULA    | Null Register A   |              N/A              |   9 / 0b1001
NULB    | Null Register B   |              N/A              |  10 / 0b1010
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
    bit_mask = 0b11000000,
    bit_id   = 0b11000000,
    bit_mapping = {
        'g.0.0':    0b000000,
        'g.0.1':    0b000001,
        'g.1.0':    0b000010,
        'g.1.1':    0b000011,
        'g.2.0':    0b000100,
        'g.2.1':    0b000101,
        'g.3.0':    0b000110,
        'g.3.1':    0b000111,
        'g.4.0':    0b001000,
        'g.4.1':    0b001001,
        'g.5.0':    0b001010,
        'g.5.1':    0b001011,
        'g.6.0':    0b001100,
        'g.6.1':    0b001101,
        'g.7.0':    0b001110,
        'g.7.1':    0b001111,
        'g.8.0':    0b010000,
        'g.8.1':    0b010001,
        'g.9.0':    0b010010,
        'g.9.1':    0b010011,
        'g.10.0':   0b010100,
        'g.10.1':   0b010101,
        'g.11.0':   0b010110,
        'g.11.1':   0b010111,
        'g.12.0':   0b011000,
        'g.12.1':   0b011001,
        'g.13.0':   0b011010,
        'g.13.1':   0b011011,
        'g.14.0':   0b011100,
        'g.14.1':   0b011101,
        'g.15.0':   0b011110,
        'g.15.1':   0b011111,
        'r.0.0':    0b100000,
        'r.0.1':    0b100001,
        'r.1.0':    0b100010,
        'r.1.1':    0b100011,
        'r.2.0':    0b100100,
        'r.2.1':    0b100101,
        'r.3.0':    0b100110,
        'r.3.1':    0b100111,
        'r.4.0':    0b101000,
        'r.4.1':    0b101001,
        'r.5.0':    0b101010,
        'r.5.1':    0b101011,
        'r.6.0':    0b101100,
        'r.6.1':    0b101101,
        'r.7.0':    0b101110,
        'r.7.1':    0b101111,
        'r.8.0':    0b110000,
        'r.8.1':    0b110001,
        'r.9.0':    0b110010,
        'r.9.1':    0b110011,
        'r.10.0':   0b110100,
        'r.10.1':   0b110101,
        'r.11.0':   0b110110,
        'r.11.1':   0b110111,
        'r.12.0':   0b111000,
        'r.12.1':   0b111001,
        'r.13.0':   0b111010,
        'r.13.1':   0b111011,
        'r.14.0':   0b111100,
        'r.14.1':   0b111101,
        'r.15.0':   0b111110,
        'r.15.1':   0b111111,
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
    opcode   = "jil",
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
