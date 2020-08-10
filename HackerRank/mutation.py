# https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    new_list = list(string)
    new_list[position] = character
    new_string = ''.join(new_list)
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)