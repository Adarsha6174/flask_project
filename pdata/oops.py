class A:
    def one(self):
        print('Class A')
class B(A):
    def one(self):
        print('Class B')
class C(B):
    def one(self):
        print('Class C')



obj=C()
obj.one()
print(__name__)
if __name__=='__main__':
    print('yes')