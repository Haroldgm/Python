import textwrap
  
def wrap(string, max_width):
    if (len(string) > 0 and len(string) <= 1000) and (max_width > 0 and max_width <= len(string)):
        result = textwrap.fill(string,max_width) 
        return result

if __name__ == '__main__':
    string, max_width = input().strip(), int(input().strip())
    result = wrap(string, max_width)
    print(textwrap.wrap(string,max_width))
    print(result)