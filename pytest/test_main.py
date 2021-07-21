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
import pytest
import main

@pytest.mark.parametrize('a, b, result',
[
    (2,3,5),
    ('hello', 'world', 'helloworld'),
    (1.5, 3.2, 4.7)
])
def test_add(a, b, result):
    assert main.add(a,b) == result



# @pytest.mark.set1
# def test_file1_method1():
# 	x=5
# 	y=6
# 	assert x+1 == y,"test failed"
# 	assert x == y,"test failed"
# @pytest.mark.set2
# def test_file1_method2():
# 	x=5
# 	y=6
# 	assert x+1 == y,"test failed"
#
#
# @pytest.mark.set1
# def test_file2_method1():
# 	x=5
# 	y=6
# 	assert x+1 == y,"test failed"
# 	assert x == y,"test failed because x=" + str(x) + " y=" + str(y)
# @pytest.mark.set2
# def test_file2_method2():
# 	x=5
# 	y=6
# 	assert x+1 == y,"test failed"
