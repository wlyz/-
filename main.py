from functions import readFile
from sequence import Sequence
import numpy as np

if __name__ == '__main__':
    S = Sequence(readFile('testfile.txt', 'txt'))
    print(S.seq)
    print(S.legal)
    print(S.illegalWords)

    # print(readFile('testfile.txt', 'txt'))
    # seqs = readCSV('partial_ecoli_genome.csv')
    # for seq in seqs:
    #     print(seq['name'])
    #     Sequence(seq['sequence'])
    #     print(' ')

