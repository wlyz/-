from csv import DictReader
import numpy as np


def readFile(input_file, input_type):
    if input_type == 'CSV':
        return readCSV(input_file)
    elif input_type == 'Fasta':
        return readFasta(input_file)
    elif input_type == 'GenBank':
        return readGenbank(input_file)
    elif input_type == 'txt':
        return readTxt(input_file)


def readCSV(input_file, sep=","):
    list_seq = []

    reader = DictReader(open(input_file), delimiter=sep, quotechar='"')

    for l in reader:
        list_seq.append(l)

    return list_seq


def readTxt(input_file):
    with open(input_file, 'r') as f:
        seq = f.read()
    return seq


def readFasta():
    pass


def readGenbank():
    pass


def separateSeq(seq):  # separate a sequence into 3-words groups
    pass


def mutationRule():  # 突变规则

    pass

