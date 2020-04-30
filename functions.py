from csv import DictReader
import numpy as np


def read_file(input_file, input_type):
    if input_type == 'CSV':
        return read_CSV(input_file)
    elif input_type == 'Fasta':
        return read_Fasta(input_file)
    elif input_type == 'GenBank':
        return read_Genbank(input_file)
    elif input_type == 'txt':
        return read_txt(input_file)


def read_CSV(input_file, sep=","):
    list_seq = []

    reader = DictReader(open(input_file), delimiter=sep, quotechar='"')

    for l in reader:
        list_seq.append(l)

    return list_seq


def read_txt(input_file):
    with open(input_file, 'r') as f:
        seq = f.read()
    return seq


def read_Fasta():
    pass


def read_Genbank():
    pass


def separate_seq(seq):  # separate a sequence into 3-words groups
    pass


def mutation_rule():  # 突变规则

    pass

