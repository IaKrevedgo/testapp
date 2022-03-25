# тестирование генераторной функциии

def scramblef(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]

scramblef2 = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))