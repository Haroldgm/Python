# https://www.hackerrank.com/challenges/string-validators/problem
if __name__ == '__main__':
    string = input()

    if len(string)> 0 and len(string)<= 1000:
        print(any(c.isalnum() for c in string))
        print(any(c.isalpha() for c in string))
        print(any(c.isdigit() for c in string))
        print(any(c.islower() for c in string))
        print(any(c.isupper() for c in string))