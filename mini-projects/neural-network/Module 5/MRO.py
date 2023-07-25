class Type(type):
    def __repr__(cls):
        return cls.__name__


class O(object, metaclass=Type): pass


class E(O): pass


class D(O): pass


class F(O): pass


class B(D , E): pass


class C(D, F): pass


class A(B, C): pass

print(A.mro())
