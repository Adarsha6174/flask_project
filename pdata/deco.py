def deco(fun):
    def inner():
        print('Before')
        fun()
        print('After')
    return inner
@deco
def ex():
    print('Outer')
ex()
