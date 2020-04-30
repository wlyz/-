from functions import read_file
from sequence import Sequence
import numpy as np

if __name__ == '__main__':
    S = Sequence(read_file('testfile.txt', 'txt'))
    print(S.seq)
    print(S.legal)
    print(S.illegal_words)

    # print(readFile('testfile.txt', 'txt'))
    # seqs = readCSV('partial_ecoli_genome.csv')
    # for seq in seqs:
    #     print(seq['name'])
    #     Sequence(seq['sequence'])
    #     print(' ')

