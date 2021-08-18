
class Squares:
    def __init__(self,start,stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return (self.value ** 2)

class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item

class SkipObject:
    def __init__(self,wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)
        

def main():
    its = Squares(1,5)
    
    for it in its:
        print(it)

    print()
    
    S = 'abc'
    for x in S:
        for y in S:
            print(x+y)

    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(I.__next__(),I.__next__(),I.__next__())
    for x in skipper:
        for y in skipper:
            print(x+y)
            

if __name__ == '__main__':
    main()
