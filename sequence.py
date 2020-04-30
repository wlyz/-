def is_seq(seq):  # 判断是否ATCG序列
    dict_seq = {}
    for s in seq:
        dict_seq[s] = seq.count(s)
    if len(dict_seq) != 4:
        return False
    else:
        return True


def is_legal(seq):  # 判断有无非法酶切位点
    legal = True
    illegal_words = {'GAATTC': None, 'TCTAGA': None, 'ACTAGT': None, 'CTGCAG': None, 'GCGGCCGC': None}
    for sites in ['GAATTC', 'TCTAGA', 'ACTAGT', 'CTGCAG', 'GCGGCCGC']:
        position = seq.find(sites)
        if position != -1:
            legal = False
            illegal_words[sites] = position
    return legal, illegal_words


def delete():  # 酶切位点删除
    pass


def add_prefix_suffix():  # 序列前后缀标准化
    pass


class Sequence:

    def __init__(self, seq):
        self.seq = seq.upper()
        self.legal, self.illegal_words = is_legal(seq)
