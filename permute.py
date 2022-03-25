def permute1(seq):
    if not seq:                                                                         # тестирование любой последовательности
        return [seq]                                                                    # пустая последовательность
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i]+seq[i+1:]                                                      # удаление текущего узла
            for x in permute1(rest):                                                    # перестановка остальных
                res.append(seq[i:i+1] + x)                                              # добавление узла спереди
            return res

def permute2(seq):                                                                      # то же самое только с генератором
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i]+seq[i+1:]
            for x in permute2(rest):
                yield seq[i:i+1] + x
                