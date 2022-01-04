class Stack:

    def __init__(self):
        self.my_list = []

    def isEmpty(self):
        if len(self.my_list) == 0:
            return True
        else:
            return False

    def push(self, new_element):
        self.my_list.append(new_element)
        # return self.my_list

    def pop(self):
        return self.my_list.pop()

    def peek(self):
        if not self.isEmpty():
            return self.my_list[len(self.my_list) - 1]

    def size(self):
        len_list = len(self.my_list)
        return len_list


def checker(brackets):
    brackets_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    st = Stack()
    print_list = []
    for x in brackets:
        if x in brackets_dict.values() and len(brackets) % 2 == 0:
            st.push(x)
        elif x in brackets_dict.keys() and st.size() != 0:
            a = st.pop()
            if brackets_dict[x] == a:
                print_list.append("Cбалансированно")
            else:
                print_list.append('Несбалансировано')
        else:
            print_list.append('Несбалансировано')

    if 'Несбалансировано' in print_list:
        return 'Несбалансировано'
    else:
        return 'Сбалансировано'


print(checker('(()'))
