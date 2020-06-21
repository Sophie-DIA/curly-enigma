f = 1
w = 8
my_k_list = range(0, 8, 2)
my_list = [{'first_key': 'a', 'second_key': '1'},
           {'first_key': 'c', 'second_key': '2'}]

for item in my_list:
    print(item['first_key'])


class FirstClass:
    def __init__(self, some_argument):
        self.my_param = some_argument

    def say_hello(self):
        print('Hi there! my_param is ' + self.my_param)


class BabyClass(FirstClass):
    def say_hello(self):
        super().say_hello()
        print('Just like Papa')


my_class = FirstClass('blabla')
my_class.say_hello()

my_baby_class = BabyClass('aaaap!')
my_baby_class.say_hello()