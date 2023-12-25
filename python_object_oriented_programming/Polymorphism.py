# -------------------------------------------------
# -- Object Oriented Programming => Ploymorphism --
# -------------------------------------------------
# The Same Method Doing Different Things On The Different Data Type.
# -------------------------------------------------------


# print(len('ahmed'))
# print(len([1, 3, 4, 5, 6, 7, 8]))
# print(len({'ahmed':19, 'maram':15, 'ibrahim': 17}))

print("_" * 40)

class A:
    def say_hello(slef):
        print('Hello From class A.')
        raise NotImplementedError('Derived Class Must Implement The Same Function That Exist In The Parent Class. ')

class B(A):
    def say_hello(slef):
        print('Hello From class B.')

class C(A):
    pass

instance_one = B()
instance_two = C()
instance_one.say_hello()
instance_two.say_hello()   # give error because the func say_hello not implement on it.