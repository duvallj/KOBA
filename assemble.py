import sys, time

print("\033c")

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

def terminal_size():
    import fcntl, termios, struct
    h, w, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return w, h

time.sleep(0.5)

if terminal_size()[0] < 60:
	print("Welcom to the: \n KIND OF BAD ASSEMBLER")
else:
	print((((terminal_size()[0] - 8) // 2) * " ") + "Welcome to the: \n" + 
		(((terminal_size()[0] - 58) // 2) * " ") + "╦╔═┬┌┐┌┌┬┐  ╔═╗┌─┐  ╔╗ ┌─┐┌┬┐  ╔═╗┌─┐┌─┐┌─┐┌┬┐┌┐ ┬  ┌─┐┬─┐\n" + 
		(((terminal_size()[0] - 58) // 2) * " ") + "╠╩╗││││ ││  ║ ║├┤   ╠╩╗├─┤ ││  ╠═╣└─┐└─┐├┤ │││├┴┐│  ├┤ ├┬┘\n" + 
		(((terminal_size()[0] - 58) // 2) * " ") + "╩ ╩┴┘└┘─┴┘  ╚═╝└    ╚═╝┴ ┴─┴┘  ╩ ╩└─┘└─┘└─┘┴ ┴└─┘┴─┘└─┘┴└─\n\n")
time.sleep(0.5)

print("You've selected the following options")
time.sleep(0.2)
print("     Verbose Mode: ", end="", flush=True)
time.sleep(0.5)
print("◉  ON" if verbose else "◎  OFF")
time.sleep(0.2)
print("   Overwrite Mode: ", end="", flush=True)
time.sleep(0.5)
print("◉  ON" if force else "◎  OFF")
time.sleep(0.2)
print("     Quantum Mode: ", end="", flush=True)
time.sleep(0.5)
print("◉  ON" if quantum else "◎  OFF")
time.sleep(0.2)


print("Reading file " + infile, end=" ", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.8)
print(".")

try:
	with open(infile) as file:
		lines = file.readlines()

except FileNotFoundError:
	error(text = "No file " + infile + " found")

if len(lines) == 0:
	error(text = "File " + infile + " is empty")

time.sleep(0.5)

print("Done.\n")

print("Assembling file...")

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
	if quantum:
		time.sleep(0.5)


# cleanup
next(bar)  #for that sweet, sweet 100%
print()