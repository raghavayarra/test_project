class even:
    def __iter__(self):
        self.a =0+
        return self

    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=2
            return x
        else:
            raise StopIteration
x=even()
p=iter(x)
for x in p:
    print(x)