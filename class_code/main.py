class F:
    p = 10
    __t = 12

    def set__t(self, x):
        self.__t = x


a = F()
a.p = 120
# a.__t = 230
a.set__t(1000)
# print(a.__t)
print(F.__)
print(a.__dict__)

