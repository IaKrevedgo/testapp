# тоже для 28 главы
# смешанные инструменыт для классов

class AttrDisplay:
    '''
    Предоставляет наследуюемый метод перегрузки отображения, который показывает экземпляры с их именами классов
    и пары имя=значение для каждого атрибута, сохраненного в самом экземпляре (но не атрибутов, унаследованных от его классов).
    Может соединятся с любым классом и будет работать на любом экземпляре.
    '''
    def gatgerAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)
    
    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatgerAttrs())
    
    
if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count+1
            TopTest.count += 2
    
    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()                                                             # создать 2 экземпляра
    print(X)
    print(Y)

