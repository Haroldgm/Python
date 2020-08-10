if __name__ == '__main__':
    n = int(input("How many scores?\n"))
    scores = map(int, input("Write the scores separated by spaces\n").split())

    maximum_score = max(scores)
    for score in scores:
        if (score == maximum_score):
            scores.remove(maximum_score)
    maximum_score = max(scores)
    print(maximum_score)