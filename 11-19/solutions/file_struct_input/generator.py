import random 

char_in_name = [
    '_', '.',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def random_string():
    return ''.join([ random.choice(char_in_name ) for _ in range(random.randint(2, 15)) ])

def generate_one_case():
    num_indent = 0
    max_num_dir = 10
    max_num_file = 100
    num_dir = 0
    num_file = 0

    while num_indent>=0:
        r = random.random()
        if r>0.9: #end
            if num_indent!=0:
                print(']')
            num_indent -= 1
        elif r>0.7 and num_dir<=max_num_dir: #create dir
            print('d'+random_string())
            num_dir += 1
            num_indent += 1
        elif num_file<max_num_file:
            print('f'+random_string())
            num_file += 1

    print('*')

n = random.randint(3,5)
print(n)
for _ in range(n):
    generate_one_case()
