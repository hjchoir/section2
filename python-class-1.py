import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class UserInfo:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("Name:", self.name, "Phone:", self.phone)

    def __del__(self):
        print("Deleted!")

u1 = UserInfo('최혜진', '02-710-0176')
u2 = UserInfo('구정아', '02-710-0177')

print(id(u1))
print(id(u2))
u1.print_info()
u2.print_info()
