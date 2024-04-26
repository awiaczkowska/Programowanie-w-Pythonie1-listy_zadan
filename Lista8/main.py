# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
d={1:'a',2:'b', 'c':'C'}
d2={1:'C'}
print('c' in d)
print(d['c'] in d2 )
lst=list(d.values())
print(lst)

def dict_index (d,val):
    for key in d:
        if d[key]==val : return key

print (dict_index(d,'a'))
