import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class MyClass:
    def function1():
        print("function1 called!!")

    def function2(self):
        print(id(self))
        print("function2 called!!")

f = MyClass()
f.function2()
#f.function1()  <-- 에러남

print(id(f))
print(MyClass.__dict__)
print(MyClass.function1()) ## 인스턴스화 시키지 않고 class의 namespace 직접 호출
