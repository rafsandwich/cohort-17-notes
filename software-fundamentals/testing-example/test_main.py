import pytest

from main import get_prefix, get_length_of_user_input, display_ascii_gift

@pytest.mark.parametrize("word,prefix", [("co-equal", "co"),
                                         ("ex-army", "ex"),
                                         ("dys-topic", "dys"),
                                         ("co-operative", "co")])
def test_get_prefix_simple_valid_data(word, prefix):

    assert get_prefix(word) == prefix

def test_get_prefix_empty_string():

    with pytest.raises(ValueError):
        get_prefix("")


def test_get_length_of_user_input_empty_input(monkeypatch):


    choices = [""]

    # A way to fake the user input so we do control it.
    def fake_input():
        return next(iter(choices))

    monkeypatch.setattr("builtins.input", fake_input)  # Go into a separate piece of code and swap something out

    assert get_length_of_user_input() == 0


def test_display_ascii_gift_prints_to_terminal(capsys):

    display_ascii_gift("love")

    stuff_printed = capsys.readouterr()

    assert stuff_printed.out == 'love ノ( º _ ºノ)\n'
