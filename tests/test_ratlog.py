import ratlog


class TestRatlog:

    def test_creating_logger(self):
        log = ratlog.Log()

        assert isinstance(log, ratlog.Log)
