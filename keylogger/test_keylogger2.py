import pytest
import keylogger2

"""
To run all tests:
py.test

To run a subset of tests
py.test -k method1 -v
-k <expression> is used to represent the substring to match
-v increases the verbosity

can also label them w/ decorator @pytest.mark.<name>.
We can run the marked test by:

py.test -m <name>
-m <name> mentions the marker name

"""

def test_callback():
    key = Keylogger()
    key.callback("space")
    assert
