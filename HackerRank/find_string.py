# https://www.hackerrank.com/challenges/find-a-string/problem
def count_substring(string, sub_string):
    occurrence_sub_string = 0
    no_of_times_to_compare = (len(string) - len(sub_string)) + 1

    for i in range(0,no_of_times_to_compare):
        if string[i:i+len(sub_string)] == sub_string:
            occurrence_sub_string += 1

    return occurrence_sub_string

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip() # strip removes trailing and starting spaces

    count = count_substring(string, sub_string)
    print(count)