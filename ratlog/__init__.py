
from __future__ import print_function

import sys


class Log:
    writer = sys.stdout.write

    def __init__(self, *args, **kwargs):
        writer = kwargs.get("writer")

        if writer and callable(writer):
            self.writer = writer

        self.tags = list(args)

    def __call__(self, message, fields=None, *tag_args):
        if not fields:
            fields = {}

        tags = self._format_tags(self.tags + list(tag_args))
        message = self._format_message(message)
        fields = self._format_fields(fields)

        output = tags + message + fields + "\n"

        self.writer(output)

    @staticmethod
    def _format_message(message):
        if not message:
            return ""
        return message

    @staticmethod
    def _format_tags(tags):
        if not tags:
            return ""
        joined_tags = "|".join(tag for tag in tags)
        return "[{}] ".format(joined_tags)

    @staticmethod
    def _format_fields(fields):
        if not fields:
            return ""

        def create_field(entry):
            key = entry[0] if entry[0] else ""
            value = ": {}".format(entry[1]) if entry[1] else ""
            return " | {}{}".format(key, value)

        return "".join(map(create_field, fields.items()))
