from instructions import instructions
import re

class MalformedDataError(Exception): pass

class MalformedLineError(MalformedDataError): pass
class MalformedLiteralError(MalformedDataError): pass
class MalformedInstructionError(MalformedDataError): pass
    

def parse_literal(lit):
    value = 0
    if lit[:2] == "0x":
        value = int(lit[2:], 16)
    elif lit[0] == "@":
        value = int(lit[1:], 8)
    elif lit[0] == "+":
        value = int(lit[1:], 10)
    elif lit[0] == "-":
        value = ((1 << 8) - int(lit[1:], 10))
    elif lit[0] == "0":
        value = 0
    elif lit[0] == "b":
        value = int(lit[1:], 2)
    elif lit == "*":
        value = 0xff
    else:
        raise MalformedLiteralError("{} is not a valid literal".format(lit))
        return None

    return value & 0xFF

line_regex = re.compile("(?P<opcode>[a-zA-Z_\.]+)(\[(?P<subcode>[a-zA-Z_\.0-9]+)\])?\s*(?P<data>[0-9a-fA-F\-\+@x]+)?")
comment_regex = re.compile("^(\s)*;")

def parse_line(line):
    # Strip all leading and trailing whitespace
    line = line.strip()
    if line is None or re.match(comment_regex, line):
        # is ok, just an empty line
        return None
    
    match = re.match(line_regex, line)

    if match is None:
        raise MalformedLineError("{} is not a valid line".format(line))
        return None
    
    instr = instructions.get(match.group("opcode"), None)
    if instr is None:
        raise MalformedInstructionError("{} is not a valid instruction".format(instr))
        return None

    # Fancy trick to return 0 if it doesn't need a subcode,
    # but None if does and the subcode isn't included/is malformed
    subcode = match.group("subcode")
    sub_bits = len(instr.bit_mapping) and subcode and instr.bit_mapping.get(subcode, None)
    if sub_bits is None:
        raise MalformedInstructionError("{} is not a valid subinstruction for {}".format(sub_bits, instr))
        return None

    instr_bits = (instr.bit_mask & instr.bit_id) | (sub_bits & (0xFF ^ instr.bit_id))

    data = match.group("data")
    
    if data:
        data_bits = parse_literal(data)
        if data_bits is None:
            raise MalformedDataError("??????")
            return None
        return (instr_bits, data_bits)
    else:
        return (instr_bits, 0xff)
    


if __name__ == "__main__":
    print("     0xFF = " + format(parse_literal("0xFF"), '08b'))
    print("     0x1F = " + format(parse_literal("0x1F"), '08b'))
    print("     @131 = " + format(parse_literal("@131"), '08b'))
    print("       +8 = " + format(parse_literal("+8"), '08b'))
    print("       +1 = " + format(parse_literal("+1"), '08b'))
    print("       +0 = " + format(parse_literal("+0"), '08b'))
    print("        0 = " + format(parse_literal("0"), '08b'))
    print("       -0 = " + format(parse_literal("-0"), '08b'))
    print("       -1 = " + format(parse_literal("-1"), '08b'))
    print("       -6 = " + format(parse_literal("-6"), '08b'))
    print("     -128 = " + format(parse_literal("-128"), '08b'))
    print("     +127 = " + format(parse_literal("+127"), '08b'))
    print("     +128 = " + format(parse_literal("+128"), '08b'))
    print("      b01 = " + format(parse_literal("b01"), '08b'))
    print("b01111111 = " + format(parse_literal("b01111111"), '08b'))
