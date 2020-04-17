class Sequence():
    legal = True
    normalization = True
    illegalWords = {'GAATTC': None, 'TCTAGA':None, 'ACTAGT':None, 'CTGCAG': None, 'GCGGCCGC': None}

    def __init__(self, seq):
        for sites in ['GAATTC', 'TCTAGA', 'ACTAGT', 'CTGCAG', 'GCGGCCGC']:
            position = seq.find(sites)
            if position != -1:
                self.legal = False
                self.illegalWords[sites] = position
        if self.legal:
            print('This is a legal sequence')
        else:
            print('This is an illegal sequence contains ' + str(self.illegalWords))

        if seq.startswith('GG') | seq.endswith('CC'):
            self.normalization = False
            print('Normalization is needed')
        else:
            print('Well normalization')






