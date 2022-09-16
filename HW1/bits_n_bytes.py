# bits_n_bytes.py
# hw 1.4

numBytes = int(input())
numBits = numBytes*8
numSequences = 2**numBits
print("There are %s bits in %s bytes, with %s possible sequences."
      % (numBits, numBytes, numSequences))

