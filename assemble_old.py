#!/usr/bin/env python3
import sys, time


def terminal_size():
    import fcntl, termios, struct
    h, w, hp, wp = struct.unpack('HHHH',
        fcntl.ioctl(0, termios.TIOCGWINSZ,
        struct.pack('HHHH', 0, 0, 0, 0)))
    return w, h

verbose = False
force  = False
simple = False
quantum = False

if "-v" in sys.argv:
    verbose = True
    sys.argv.remove("-v")
if "-f" in sys.argv:
    force = True
    sys.argv.remove("-f")
if "-s" in sys.argv:
    simple = True
    sys.argv.remove("-s")
if "-q" in sys.argv:
    quantum = True
    sys.argv.remove("-q")

if not simple:
    print("\033c")

def error(text=None):
    print("\n")
    if verbose:
        if simple:
            if text:
                print("!!ERROR: " + text)
            print("Usage: python assemble.py <input file> <output file> [options,]")
            print("Help:  python assemble.py --help")
        else:
            print("╔" + ("═" * (terminal_size()[0] - 2)) + "╗")
            if text:
                text = "╟╼━ Error: " + text
                print(text + (" " * (terminal_size()[0] - len(text) - 1)) + "║")
            text = "╟╼━ Usage: python assemble.py <input file> <output file> [options,]"
            print(text + (" " * (terminal_size()[0] - len(text) - 1)) + "║")
            text = "╟╼━ Help:  python assemble.py --help"
            print(text + (" " * (terminal_size()[0] - len(text) - 1)) + "║")
            print("╚" + ("═" * (terminal_size()[0] - 2)) + "╝")
    else:
        print("An error was encountered. Run with -v for verbose output")
    exit()

if len(sys.argv) > 1:
    if sys.argv[1] == "--help":
        print("Usage: python assemble.py <input file> <output file> [options,]")
        print("Options: ")
        print("         -v : verbose")
        print("         -f : overwrite output if it already exists")
        print("         -s : simple mode")
        print("         -q : quantum mode")
        exit()

if len(sys.argv) < 3:
    error()

infile = sys.argv[1]


time.sleep(0.5)

if simple or terminal_size()[0] < 60:
    print("Welcome to the: \n KIND OF BAD ASSEMBLER")
else:
    print(
        (((terminal_size()[0] - 8) // 2) * " ") + "Welcome to the: \n" + 
        (((terminal_size()[0] - 58) // 2) * " ") + "╦╔═┬┌┐┌┌┬┐  ╔═╗┌─┐  ╔╗ ┌─┐┌┬┐  ╔═╗┌─┐┌─┐┌─┐┌┬┐┌┐ ┬  ┌─┐┬─┐\n" + 
        (((terminal_size()[0] - 58) // 2) * " ") + "╠╩╗││││ ││  ║ ║├┤   ╠╩╗├─┤ ││  ╠═╣└─┐└─┐├┤ │││├┴┐│  ├┤ ├┬┘\n" + 
        (((terminal_size()[0] - 58) // 2) * " ") + "╩ ╩┴┘└┘─┴┘  ╚═╝└    ╚═╝┴ ┴─┴┘  ╩ ╩└─┘└─┘└─┘┴ ┴└─┘┴─┘└─┘┴└─\n\n")

time.sleep(0.5)

print("You've selected the following options")
if simple:
    print("Verbose: " + str(verbose))
    print("  Force: " + str(force))
    print(" Simple: " + str(simple))
    print("Quantum: " + str(quantum))
else:   
    time.sleep(0.2)
    print("     Verbose Mode: ", end="", flush=True)
    time.sleep(0.5)
    print("◉  ON" if verbose else "◎  OFF")
    time.sleep(0.2)
    print("   Overwrite Mode: ", end="", flush=True)
    time.sleep(0.5)
    print("◉  ON" if force else "◎  OFF")
    time.sleep(0.2)
    print("      Simple Mode: ", end="", flush=True)
    time.sleep(0.5)
    print("◉  ON" if simple else "◎  OFF")
    print("     Quantum Mode: ", end="", flush=True)
    time.sleep(0.5)
    print("◉  ON" if quantum else "◎  OFF")
    time.sleep(0.2)

if verbose:
    if simple:
        print("\nReading file " + infile)
    else:
        print("\nReading file " + infile, end=" ", flush=True)
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

if verbose:
    print("Done.\n")
    print("Assembling file...")

def progress_bar(lines):
    line = 0
    width = 0
    if not simple:
        width = terminal_size()[0] / lines      #width of characters per each line
    print()
    while line <= lines:
        if simple:
            print("\r" + str(int((line / lines) * 100)) + "%", end = "")
        else:
            print("\033[F" + (int(line * width) * "█") + ('░' if (int(line * width) < (line * width)) else ''))
            print(str(int((line / lines) * 100)) + "%", end = "")
        line += 1
        yield line


bar = progress_bar(len(lines))
out = []

def process(line):
    return line.encode() #TODO: actual stuff

for line in lines:
    next(bar)  #progress bar, prettty
    out.append(process(line))
    if quantum:
        time.sleep(0.5)

outfile = sys.argv[2]

next(bar)  #for that sweet, sweet 100%
time.sleep(0.5)

if verbose:
    if simple:
        print("\n\nSaving output to " + outfile)
    else:
        print("\n\nSaving output to " + outfile, end=" ", flush=True)
        time.sleep(0.3)
        print(".", end="", flush=True)
        time.sleep(0.3)
        print(".", end="", flush=True)
        time.sleep(0.5)
        print(".")

if force:
    with open(outfile, "wb") as output:
        output.write(b"".join(out))
else:
    try:
        with open(outfile, "xb") as output:
            output.write(b"".join(out))
    except FileExistsError:
        error(text="Ouput file " + outfile + " already exists. If you want to overwrite it, use -f")

print()
