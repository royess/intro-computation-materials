def print_with_indent(name, num_indent):
    print('|     '*num_indent + name)

def get_file_or_dir(num_indent, is_root):
    if is_root:
        name = 'ROOT'
    else:
        name = input()

    if name[0]=='d' or name=='ROOT':
        if name[0]=='d':
            num_indent += 1

        print_with_indent(name, num_indent)

        included_files = []
        subname = ''
        while subname!=']' and subname!='*':
            subname = get_file_or_dir(num_indent, False)
            if subname[0]=='f':
                included_files.append(subname)
        included_files.sort()

        for file in included_files:
            print_with_indent(file, num_indent)

        if name=='ROOT':
            print()

    return name

num_cases = int(input())

for i in range(1, num_cases+1):
    print('DATA SET {}:'.format(i))
    get_file_or_dir(0, True)
