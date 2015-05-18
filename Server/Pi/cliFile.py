import sys
import coder

def main(argv):
    script, flag, filename = sys.argv

    if flag == '-e':
        coder.encode(filename, "_Encoded4.pi", coder.getPiWithFourHex(), 4)
    elif flag == '-d':
        coder.decode(filename, "_Decoded4.pi", coder.getPiWithFourHex(), 4)

if __name__ == "__main__":
   main(sys.argv[1:])