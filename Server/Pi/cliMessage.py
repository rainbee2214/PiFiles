import sys
import coder

def main(argv):
    script, flag, sendToSMS, message = sys.argv

    if flag == '-e':
        coder.encodeMessage(message,  coder.getPiWithTwoHex(), 2, sendToSMS)
    elif flag == '-d':
        coder.decodeMessage(message,  coder.getPiWithTwoHex(), 2, sendToSMS)


if __name__ == "__main__":
   main(sys.argv[1:])