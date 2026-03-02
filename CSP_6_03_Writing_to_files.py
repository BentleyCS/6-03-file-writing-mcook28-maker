import random

def writeFile(inputList, fileName):
    # Creates a file and writes each item from the list on a new line
    with open(fileName, "w") as file:
        for item in inputList:
            file.write(str(item) + "\n")


def sortNames(fileName, targetFile):
    # Read names from source file
    with open(fileName, "r") as file:
        names = file.readlines()

    # Remove newline characters
    names = [name.strip() for name in names]

    # Sort the names
    names.sort()

    # Write sorted names to target file
    with open(targetFile, "w") as file:
        for name in names:
            file.write(name + "\n")


def highScore(newScore: int):
    # Add new score to scores.txt
    with open("scores.txt", "a") as file:
        file.write(str(newScore) + "\n")

    # Read all scores
    with open("scores.txt", "r") as file:
        scores = file.readlines()

    # Convert scores to integers
    scores = [int(score.strip()) for score in scores]

    # Calculate average
    average = sum(scores) / len(scores)

    return average
