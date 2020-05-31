import gzip
import sys

opener = gzip.open

if __name__ == '__main__':
    f = gzip.open(sys.argv[1],mode ='wt')
    f.write(''.join(sys.argv[2:])) # data to compress and get zipped
    f.close()