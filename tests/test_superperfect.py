import sys
import pytest
import src.superperfect

class color:
    ERROR = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def test_superperfect1() :
    input_values = [4]
    output = []

    def mock_input(s) :
        return input_values.pop(0)

    src.superperfect.input = mock_input
    src.superperfect.print = lambda s : output.append(s)

    src.superperfect.main()

    if output[0] != "superperfect" :
        errmsg = "ERROR: Your program wrongly outputs '%s' for 4 while it should output 'superperfect'!!" %(output[0])
        print(color.ERROR+color.BOLD+errmsg+color.END, file=sys.stderr)

    assert output == ['superperfect']

def test_superperfect2() :
    input_values = [16]
    output = []

    def mock_input(s) :
        return input_values.pop(0)

    src.superperfect.input = mock_input
    src.superperfect.print = lambda s : output.append(s)

    src.superperfect.main()

    if output[0] != "superperfect" :
        errmsg = "ERROR: Your program wrongly outputs '%s' for 16 while it should output 'superperfect'!!" %(output[0])
        print(color.ERROR+color.BOLD+errmsg+color.END %(output), file=sys.stderr)

    assert output == ['superperfect']

def test_superperfect3() :
    input_values = [5]
    output = []

    def mock_input(s) :
        return input_values.pop(0)

    src.superperfect.input = mock_input
    src.superperfect.print = lambda s : output.append(s)

    src.superperfect.main()

    if output[0] != "not superperfect" :
        errmsg = "ERROR: Your program wrongly outputs '%s' for 5 while it should output 'not superperfect'!!" %(output[0])
        print(color.ERROR+color.BOLD+errmsg+color.END, file=sys.stderr)

    assert output == ['not superperfect']

def test_superperfect4() :
    input_values = [15]
    output = []

    def mock_input(s) :
        return input_values.pop(0)

    src.superperfect.input = mock_input
    src.superperfect.print = lambda s : output.append(s)

    src.superperfect.main()

    if output[0] != "not superperfect" :
        errmsg = "ERROR: Your program wrongly outputs '%s' for 15 while it should output 'not superperfect'!!" %(output[0])
        print(color.ERROR+color.BOLD+errmsg+color.END %(output), file=sys.stderr)

    assert output == ['not superperfect']

