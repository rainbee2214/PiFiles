import sys
import coder

def main(argv):
    script, flag, filename = sys.argv


    if flag == '-e':
        coder.encode(filename, filename+"_Encoded.pi", coder.getPiWithTwoHex(), 2)
    elif flag == '-d':
        coder.decode(filename, "_Decoded.pi", coder.getPiWithTwoHex(), 2)

if __name__ == "__main__":
   main(sys.argv[1:])