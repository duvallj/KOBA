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

"""
in addition to the operation (S0 - S3), 
each ALU instruction has a logic/math select and carry hi/lo select

   l.XX = logic
 m.c.XX = math, with carry input
m.nc.XX = math, without carry input

bits:        1  0  1  0  1  0
             ^  ^  \_________\
            /    \        \
           /      \        operator bits (S0-S3)
          /        \
Logic(0=math)     Carry(carry is active low)
"""

alu = Instruction(
    opcode   = "alu",
    bit_mask = 0b01000000,
    bit_id   = 0b11000000,
    bit_mapping = {
        'l.ia':          0b100000,
        'l.oiaib':       0b100001,
        'l.niab':        0b100010,
        'l.0':           0b100011,
        'l.niaib':       0b100100,
        'l.ib':          0b100101,
        'l.xab':         0b100110,
        'l.naib':        0b100111,
        'l.oiab':        0b101000,
        'l.xiaib':       0b101001,
        'l.b':           0b101010,
        'l.nab':         0b101011,
        'l.1':           0b101100,
        'l.oaib':        0b101101,
        'l.oab':         0b101110,
        'l.a':           0b101111,
        'm.c.panaib':    0b000100,
        'm.c.poabnabi':  0b000101,
        'm.c.mamb1':     0b000110,
        'm.c.mnab1':     0b000111,
        'm.c.panab':     0b001000,
        'm.c.pab':       0b001001,
        'm.c.poabinab':  0b001010,
        'm.c.paa':       0b001100,
        'm.c.poaba':     0b001101,
        'm.c.poaiba':    0b001110,
        'm.c.ma1':       0b001111,
        'm.nc.panaib':   0b010100,
        'm.nc.poabnabi': 0b010101,
        'm.nc.mamb1':    0b010110,
        'm.nc.mnab1':    0b010111,
        'm.nc.panab':    0b011000,
        'm.nc.pab':      0b011001,
        'm.nc.poabinab': 0b011010,
        'm.nc.paa':      0b011100,
        'm.nc.poaba':    0b011101,
        'm.nc.poaiba':   0b011110,
        'm.nc.ma1':      0b011111,
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
    bit_id   = 0b00000000,
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

# color     row     
# g / r     0 - F
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
    bit_id   = 0b00011000,
    bit_mapping = {}
)

write_address = Instruction(
    opcode   = "wadr",
    bit_mask = 0b11111111,
    bit_id   = 0b10011001,
    bit_mapping = {}
)

jump_unconditional = Instruction(
    opcode   = "jmp",
    bit_mask = 0b11111111,
    bit_id   = 0b00100001,
    bit_mapping = {}
)

jump_if_equal = Instruction(
    opcode   = "jie",
    bit_mask = 0b11111111,
    bit_id   = 0b00100010,
    bit_mapping = {}
)

jump_if_not_equal = Instruction(
    opcode   = "jine",
    bit_mask = 0b11111111,
    bit_id   = 0b00100100,
    bit_mapping = {}
)

jump_if_carry = Instruction(
    opcode   = "jic",
    bit_mask = 0b11111111,
    bit_id   = 0b00101000,
    bit_mapping = {}
)

jump_if_not_carry = Instruction(
    opcode   = "jinc",
    bit_mask = 0b11111111,
    bit_id   = 0b00110000,
    bit_mapping = {}
)

instructions = {
    alu.opcode : alu,
    read_reg.opcode : read_reg,
    write_reg.opcode : write_reg,
    write_disp.opcode : write_disp,
    read_address.opcode : read_address,
    write_address.opcode : write_address,
    jump_unconditional.opcode : jump_unconditional,
    jump_if_equal.opcode : jump_if_equal,
    jump_if_not_equal.opcode : jump_if_not_equal,
    jump_if_carry.opcode : jump_if_carry,
    jump_if_not_carry.opcode : jump_if_not_carry,
}
