hex = {
	"0" : 0b0000,
	"1" : 0b0001,
	"2" : 0b0010,
	"3" : 0b0011,
	"4" : 0b0100,
	"5" : 0b0101,
	"6" : 0b0110,
	"7" : 0b0111,
	"8" : 0b1000,
	"9" : 0b1001,
   	"A" : 0b1010,
	"B" : 0b1011,
	"C" : 0b1100,
	"D" : 0b1101,
	"E" : 0b1110,
	"F" : 0b1111,
}

def parse_literal(lit):
	if lit[:2] == "0x":
		return (hex[lit[2]] << 4 | hex[lit[3]]) & 0xFF
	if lit[0] == "@":
		return ((hex[lit[1]] & 0b111) << 6 | (hex[lit[2]] & 0b111) << 3 | hex[lit[3]]) & 0xFF
	if lit[0] == "+":
		return int(lit[1:]) & 0xFF
	if lit[0] == "-":
		return ((1 << 8) - int(lit[1:])) & 0xFF
	if lit[0] == "0":
		return 0
	if lit[0] == "b":
		return int(lit[1:], 2) & 0xFF
	if lit == "*":
		return 0b00000000


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