# class Details:
#     name = 'vamsi'
#     age = 22
#
#     def __init__(selfa):
#         print('In a class A')
#
#     def change_details(self, nam, age):
#         self.name = nam
#         self.age = age
#
#
# # class B(Details):
# #     def __init__(self):
# #         super().__init__()
# #         print('In class B')
# #
#
# det = Details()
# det.change_details('KRishna', 23)
# print(det.name, det.age)
# p1 = Details()
#
# # b = B()


class A():
    def dummy(self):
        print('In class A')


class X():
    def dummy(self):
        print('In class X')


class B(A, X):
    pass
    # def dummy(self):
    #     print('In class B')


class C(A):
    def dummy(self):
        print('In class C')


class D(B, C):
    pass


d = D()
d.dummy()

# class X():
#     def who_am_i(self):
#         print("I am a X")
#
#
# class Y():
#     def who_am_i(self):
#         print("I am a Y")
#
#
# class A(X, Y):
#     def who_am_i(self):
#         print("I am a A")
#
#
# class B(X, Y):
#     def who_am_i(self):
#         print("I am a B")
#
#
# class F(A, B):
#     pass
#
#
# f = F()
# f.who_am_i()
