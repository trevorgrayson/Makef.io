from reader import read, replace_opts


class TestReader:
    def test_read_one(self):
        words = ["python"]
        assert read(*words)[0:6] == 'PYTHON'

    def test_read_two(self):
        words = ["python", "flask"]
        result = read(*words)[0:6]
        print(result)

    def test_replace_opts(self):
        make = """
PYTHON?=python

dothing:
	echo "done"
"""
        result = replace_opts(make, PYTHON='python3')

        assert result.startswith("\nPYTHON?=python3")
