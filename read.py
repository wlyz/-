from csv import DictReader
from sequence import Sequence


def readCSV(input_file, sep=","):
    list_seq = []

    reader = DictReader(open(input_file), delimiter=sep, quotechar='"')

    for l in reader:
        list_seq.append(l)

    return list_seq


if __name__ == '__main__':
    seqs = readCSV('partial_ecoli_genome.csv')
    for seq in seqs:
        print(seq['name'])
        Sequence(seq['sequence'])
        print(' ')
