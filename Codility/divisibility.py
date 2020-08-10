#Exam
def solution(N):
    if (N > 0) and (N < 1000): #Assume that N is an integer within 1 to 1000
        list_of_coded_numbers = [] #List will contain the coded numbers in descending order
        while N > 0:
            if (N % 2 == 0) and (N % 3 == 0) and (N % 5 == 0):
                list_of_coded_numbers.append("CodilityTestCoders")
    
            elif (N % 3 == 0) and (N % 5 == 0):
                list_of_coded_numbers.append("TestCoders")
    
            elif (N % 2 == 0) and (N % 5 == 0):
                list_of_coded_numbers.append("CodilityCoders")
    
            elif (N % 2 == 0) and (N % 3 == 0):
                list_of_coded_numbers.append("CodilityTest")
    
            elif (N % 5 == 0):
                list_of_coded_numbers.append("Coders")
    
            elif (N % 3 == 0):
                list_of_coded_numbers.append("Test")
    
            elif (N % 2 == 0):
                list_of_coded_numbers.append("Codility")
    
            else:
                list_of_coded_numbers.append(N)
    
            N -= 1

        list_of_coded_numbers.reverse() #Arrange the coded numbers in ascending order
        for coded_number in list_of_coded_numbers:# Print the coded numbers in each line
            print(coded_number)


if __name__ == '__main__':
    solution(110)