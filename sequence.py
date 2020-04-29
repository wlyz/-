class Sequence():
    legal = True
    normalization = True
    illegalWords = {'GAATTC': None, 'TCTAGA': None, 'ACTAGT': None, 'CTGCAG': None, 'GCGGCCGC': None}

    def __init__(self, seq):

        self.isLegal(seq)

        # 判断标准化
        if self.legal:
            print('legal seq')

    def isLegal(self, seq):  # 判断有无非法酶切位点
        for sites in ['GAATTC', 'TCTAGA', 'ACTAGT', 'CTGCAG', 'GCGGCCGC']:
            position = seq.find(sites)
            if position != -1:
                self.legal = False
                self.illegalWords[sites] = position
        pass

    def delete(self, seq):  # 酶切位点删除
        pass

    def add_prefix_suffix(self):  # 序列前后缀标准化
        pass

