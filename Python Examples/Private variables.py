class P:
    __alias = 'Tadi'   # private
    _a = 1000
    def _foo(self):     # public method
        print('This is Non-public method')
      
class Q(P):
    _name = "Nitish" # Non-public
    def who(self):
        print('a :',self._a)
        print('name  : ', self._name)
        print('alias : ', self._P__alias)
    def __foo(self): # private method
        super()._foo()
        print('This is private method')
   
p1 = Q()
p1._Q__foo()
p1.who()
print(p1._a)
print(p1._name)
print(p1._P__alias)
