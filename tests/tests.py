import unittest.mock as um

import pytest

from app.main import search_str


@pytest.mark.parametrize(
    "file_name,text,words,result,answer",
    [
        (
                "test1.txt",
                (
                        "Having a friend is a divine gift, it is probably the most powerful relationship we can have,\n"
                        "because it is a choice, not an obligation, as it often happens with family.\n"
                        "True friends should not let a momentary brawl ruin a lifetime of memories, memories and friendship.\n"
                        "Come back anytime for many more phrases, messages, tips and ideas for better living.\n"
                        "Hope to see you soon, that you do great, good luck.\n"
                ),
                "lifetime",
                True,
                "String exist in a file",
        ),
        (
                "test2.txt",
                (
                        "Football or soccer, which is considered to be the most popular sport in the world.\n"
                        "Is a team sport played between two teams of eleven players using a spherical ball.\n"
                ),
                "championship",
                False,
                "String does not exist in a file",
        ),
        (
                "test3.txt",
                (
                        "It has a living room, a dining room, two bedrooms, a bathroom, a kitchen, and a garage.\n"
                        "There are six chairs and a dining table in the dining room.\n"
                        "The dining room is between the living room and the kitchen.\n"
                ),
                "a bathroom",
                True,
                "String exist in a file",
        ),
        (
                "test4.txt",
                (
                        "There are four armchairs, a table, a room divider, a sofa and a TV set in the living room.\n"
                        "In each bedroom you can find a wardrobe and a bed. There is a bucket in the bathroom.\n"
                        "In the kitchen there are many kitchen utensils."
                ),
                "house",
                False,
                "String does not exist in a file",
        ),
    ],
)
def test_read_from_file(file_name, text, words, result, answer):
    with um.patch("builtins.open", um.mock_open(read_data=text)) as mock_file:
        assert search_str(file_name, words) == result
    mock_file.assert_called_with(file_name, "r")
