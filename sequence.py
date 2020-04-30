def isSeq(seq):  # 判断是否ATCG序列
    dictSeq = {}
    for s in seq:
        dictSeq[s] = seq.count(s)
    if len(dictSeq) != 4:
        return False
    else:
        return True


def isLegal(seq):  # 判断有无非法酶切位点
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
    # seq = ''
    # legal = True
    # normalization = True
    # illegalWords = {'GAATTC': None, 'TCTAGA': None, 'ACTAGT': None, 'CTGCAG': None, 'GCGGCCGC': None}

    def __init__(self, seq):
        self.seq = seq.upper()
        self.legal, self.illegalWords = isLegal(seq)

