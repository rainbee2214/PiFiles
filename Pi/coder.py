import pi

chunkSize = 4

def encode(inputFilename, outputFilename):
    with open(inputFilename, 'rb') as f:
        data = f.read().encode('hex').upper()
        chunks = [data[i:i+chunkSize] for i in range(0, len(data), chunkSize)]
        print chunks

    # TODO:
    #   - Encode filename/type, save to outputFilename
    #   - Get indices corresponding each chunk
    #   - Save indices to outputFilename 

def decode(inputFilename, outputDirectory):
    with open(inputFilename, 'rb') as f:
        data = f.read()

    # TODO:
    #   - Decode filename/type
    #   - Get indices, compute to hex
    #   - Decode hex, save to outputDirectory

encode('README.md', '..')