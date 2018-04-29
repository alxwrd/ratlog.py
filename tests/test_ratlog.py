# -*- coding: utf-8 -*-
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


def generic_test_data():
    with open("tests/ratlog.testsuite.json") as testsuite:
        test_json = json.load(testsuite)
    return [(test["log"], test["data"]) for test in test_json["generic"]]


class TestRatlog:

    def test_creating_logger(self):
        log = ratlog.Log()

        assert isinstance(log, ratlog.Log)

    def test_integer_as_message(self):
        log = ratlog.Log()

        log(1)

        assert "1\n" == output.value

    def test_unicode_as_message(self):
        log = ratlog.Log()

        log(u"\U0001F984")

        assert "🦄\n" == output.value

    def test_string_as_fields_makes_tags(self):
        log = ratlog.Log()

        log("message", "tag1", "tag2")

        assert "[tag1|tag2] message\n" == output.value

    def test_multiple_tags_on_instance_create(self):
        log = ratlog.Log("test1", "test2", "test3")

        log("message")

        assert "[test1|test2|test3] message\n" == output.value

    def test_allow_more_tags_on_exisiting_instance(self):
        log = ratlog.Log("test1", "test2")

        log("message", {}, "test3")

        assert "[test1|test2|test3] message\n" == output.value 

    def test_allow_permanent_addition_of_more_tags(self):
        log = ratlog.Log("test1")

        log.tags.append("test2")

        log("message")

        assert "[test1|test2] message\n" == output.value

    @pytest.mark.parametrize("expected,data", generic_test_data())
    def test_generic_spec_cases(self, expected, data):
        log = ratlog.Log(*data.get("tags", []))

        log(data.get("message", ""), data.get("fields"))

        assert expected == output.value
