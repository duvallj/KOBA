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
    opcode   = "alu_l",     # stands for "logic"
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
    opcode   = "alu_m",
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

read_reg = Instruction(
    opcode   = "rreg",
    bit_mask = 0b11110000,
    bit_id   = 0b10000000,
    bit_mapping = {
        '0': 0b0000,
        '1': 0b0001,
        '2': 0b0010,
        '3': 0b0011,
        '4': 0b0100,
        '5': 0b0101,
        '6': 0b0110,
        '7': 0b0111,
        '8': 0b1000,
        '9': 0b1001,
        'a': 0b1010,
        'b': 0b1011,
        'c': 0b1100,
        'd': 0b1101,
        'e': 0b1110,
        'f': 0b1111,
    }
)

write_reg = Instruction(
    opcode   = "wreg",
    bit_mask = 0b11110000,
    bit_id   = 0b01000000,
    bit_mapping = {
        '0': 0b0000,
        '1': 0b0001,
        '2': 0b0010,
        '3': 0b0011,
        '4': 0b0100,
        '5': 0b0101,
        '6': 0b0110,
        '7': 0b0111,
        '8': 0b1000,
        '9': 0b1001,
        'a': 0b1010,
        'b': 0b1011,
        'c': 0b1100,
        'd': 0b1101,
        'e': 0b1110,
        'f': 0b1111,
    }
)

write_disp = Instruction(
    opcode   = "disp",
    bit_mask = 0b11000000,
    bit_id   = 0b11000000,
    bit_mapping = {

    }
)

read_address = Instruction(
    opcode   = "radr",
    bit_mask = 0b11111111,
    bit_id   = 0b01111111,
    bit_mapping = {}
)

write_address = Instruction(
    opcode   = "wadr",
    bit_mask = 0b11111111,
    bit_id   = 0b01111110,
    bit_mapping = {}
)

jump_unconditional = Instruction(
    opcode   = "jmp",
    bit_mask = 0b11111111,
    bit_id   = 0b10101001,
    bit_mapping = {}
)

jump_if_equal = Instruction(
    opcode   = "jie",
    bit_mask = 0b11111111,
    bit_id   = 0b10101010,
    bit_mapping = {}
)

jump_if_less = Instruction(
    opcode   = "jie",
    bit_mask = 0b11111111,
    bit_id   = 0b10101100,
    bit_mapping = {}
)
