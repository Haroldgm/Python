# https://www.hackerrank.com/challenges/list-comprehensions/tutorial

if __name__ == '__main__':
    x,y,z,n = map(int,input('Enter values separated by a space:').split(" "))

    results = []
    for x in [i for i in range(x+1)]:
    	for y in [j for j in range(y+1)]:
    		for z in [j for j in range(z+1)]:
    			if (x+y+z != n):
    				results.append([x,y,z])

    print('The permutations are:\n',results)