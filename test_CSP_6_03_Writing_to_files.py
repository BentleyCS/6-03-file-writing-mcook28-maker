import os
import pytest
from CSP_6_03_Writing_to_files import writeFile, sortNames, highScore
# Replace "your_file_name" with the name of your python file (without .py)


def test_writeFile():
    test_list = ["Zoe", "Anna", "Mike"]
    test_filename = "test_names.txt"

    writeFile(test_list, test_filename)

    with open(test_filename, "r") as file:
        contents = file.read().splitlines()

    assert contents == test_list

    os.remove(test_filename)


def test_sortNames():
    source_file = "test_source.txt"
    target_file = "test_sorted.txt"

    names = ["Zoe", "Anna", "Mike"]

    # Create source file
    with open(source_file, "w") as file:
        for name in names:
            file.write(name + "\n")

    sortNames(source_file, target_file)

    with open(target_file, "r") as file:
        sorted_names = file.read().splitlines()

    assert sorted_names == sorted(names)

    os.remove(source_file)
    os.remove(target_file)


def test_highScore():
    test_scores = [10, 20, 30]
    filename = "scores.txt"

    # Reset scores file
    with open(filename, "w") as file:
        for score in test_scores:
            file.write(str(score) + "\n")

    new_score = 40
    avg = highScore(new_score)

    expected_average = (10 + 20 + 30 + 40) / 4

    assert avg == expected_average

    os.remove(filename)