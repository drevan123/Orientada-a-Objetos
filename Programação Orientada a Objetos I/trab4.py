class A:
     def fun(self):
      print("")

class B:
   def fun(self):
       print("")

class C:
   def fun(self):
      print("")

class D:
   def fun(self):
       print("")

class E:
   def fun(self):
      print("")

class F(B,A):
   def __init__(self):
      print("")

class G(D,C):
   def __init__(self):
      print("")

class H(F,E):
   def __init__(self):
      print("")

class I(H,G):
   def __init__(self):
       print("")



#print ordenação
X = C()

print("ordenações 9")
print(I.__mro__)

print("ordenações 5")
print(I.__mro__[:5])
