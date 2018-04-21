import sys, time

def error(text = ""):
	if text != "":
		print("Error: " + text)
	print("Usage: python assemble.py <input file> <output file> [options,]")
	print("Help:  python assemble.py --help")
	exit()

if len(sys.argv) > 1:
	if sys.argv[1] == "--help":
		print("Usage: python assemble.py <input file> <output file> [options,]")
		print("Options: ")
		print("			-v : verbose")
		print("			-f : overwrite output if it already exists")
		print("			-q : quantum mode")
		exit()

if len(sys.argv) < 3:
	error()

verbose = False
force  = False
quantum = False

if len(sys.argv) > 3:
	if "-v" in sys.argv:
		verbose = True
	if "-f" in sys.argv:
		force = True
	if "-q" in sys.argv:
		quantum = True

infile = sys.argv[1]

print("Welcome to the Kind Of Bad Assembler")
print("You've selected the following options")
print("     Verbose Mode: " + ("◉  ON" if verbose else "◎  OFF"))
print("   Overwrite Mode: " + ("◉  ON" if force else "◎  OFF"))
print("     Quantum Mode: " + ("◉  ON" if quantum else "◎  OFF"))
print("Reading file " + infile + "...")

try:
	with open(infile) as file:
		lines = file.readlines()

except FileNotFoundError:
	error(text = "No file " + infile + " found")

print("Done.\n")

print("Assembling file...")

def terminal_size():
    import fcntl, termios, struct
    h, w, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return w, h

def progress_bar(lines):
	line = 0
	width = terminal_size()[0] / lines  	#width of characters per each line
	print()
	while line <= lines:
		print("\033[F" + (int(line * width) * "█") + ('░' if (int(line * width) < (line * width)) else ''))
		print(str(int((line / lines) * 100)) + "%", end = "")
		line += 1
		yield line


bar = progress_bar(len(lines))
for line in lines:
	next(bar)  #progress bar, prettty


# cleanup
next(bar)  #for that sweet, sweet 100%
print()