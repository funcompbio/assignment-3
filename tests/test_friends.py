import sys
import pytest
import src.friends

class color:
    ERROR = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def test_friends1() :
    input_values = [6, 28]
    output = []

    def mock_input(s) :
        return input_values.pop(0)

    src.friends.input = mock_input
    src.friends.print = lambda s : output.append(s)

    src.friends.main()

    if output[0] != "friends" :
        errmsg = "ERROR: Your program wrongly outputs '%s' for 6 and 28 while it should output 'friends'!!" %(output[0])
        print(color.ERROR+color.BOLD+errmsg+color.END, file=sys.stderr)

    assert output == ['friends']

def test_friends2() :
    input_values = [12, 28]
    output = []

    def mock_input(s) :
        return input_values.pop(0)

    src.friends.input = mock_input
    src.friends.print = lambda s : output.append(s)

    src.friends.main()

    if output[0] != "not friends" :
        errmsg = "ERROR: Your program wrongly outputs '%s' for 12 and 28 while it should output 'not friends'!!" %(output[0])
        print(color.ERROR+color.BOLD+errmsg+color.END %(output), file=sys.stderr)

    assert output == ['not friends']

def test_friends3() :
    input_values = [30, 140]
    output = []

    def mock_input(s) :
        return input_values.pop(0)

    src.friends.input = mock_input
    src.friends.print = lambda s : output.append(s)

    src.friends.main()

    if output[0] != "friends" :
        errmsg = "ERROR: Your program wrongly outputs '%s' for 30 and 140 while it should output 'friends'!!" %(output[0])
        print(color.ERROR+color.BOLD+errmsg+color.END, file=sys.stderr)

    assert output == ['friends']

def test_friends4() :
    input_values = [30, 150]
    output = []

    def mock_input(s) :
        return input_values.pop(0)

    src.friends.input = mock_input
    src.friends.print = lambda s : output.append(s)

    src.friends.main()

    if output[0] != "not friends" :
        errmsg = "ERROR: Your program wrongly outputs '%s' for 30 and 150 while it should output 'not friends'!!" %(output[0])
        print(color.ERROR+color.BOLD+errmsg+color.END %(output), file=sys.stderr)

    assert output == ['not friends']

