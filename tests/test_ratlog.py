import json
import pytest
import ratlog


class MockWriter(object):

    def __init__(self):
        self.value = ""

    def __call__(self, message):
        self.value = message


output = MockWriter()
ratlog.Log.writer = output


def get_generic_test_data():
    with open("tests/ratlog.testsuite.json") as testsuite:
        test_json = json.load(testsuite)
    return [(test["log"], test["data"]) for test in test_json["generic"]]


class TestRatlog:

    def test_creating_logger(self):
        log = ratlog.Log()

        assert isinstance(log, ratlog.Log)

    @pytest.mark.parametrize("expected,data", get_generic_test_data())
    def test_generic_spec_cases(self, expected, data):
        log = ratlog.Log(*data.get("tags", []))

        log(data.get("message", ""), data.get("fields"))

        assert expected == output.value
