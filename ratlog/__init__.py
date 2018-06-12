# -*- coding: utf8 -*-
from __future__ import print_function

import sys


try:
    str = unicode
except NameError:
    pass


class Log:
    writer = sys.stdout.write

    def __init__(self, *args, **kwargs):
        writer = kwargs.get("writer")

        if writer and callable(writer):
            self.writer = writer

        self.tags = list(args)

    def __call__(self, message, fields=None, *tag_args):
        tag_args = list(tag_args)

        if not isinstance(fields, dict):
            if fields:
                tag_args.insert(0, fields)
                fields = None

        if not fields:
            fields = {}

        if not isinstance(message, str):
            message = str(message)

        tags = self._format_tags(self.tags + tag_args)
        message = self._format_message(message)
        fields = self._format_fields(fields)

        output = escape("\n", tags + message + fields) + "\n"

        self.writer(output)

    @staticmethod
    def _format_message(message):
        if not message:
            return ""
        return escape("[|", message)

    @staticmethod
    def _format_tags(tags):
        if not tags:
            return ""
        joined_tags = "|".join(escape("|]", tag) for tag in tags)
        return "[{}] ".format(joined_tags)

    @staticmethod
    def _format_fields(fields):
        if not fields:
            return ""

        def create_field(entry):
            key = escape("|:", entry[0]) if entry[0] else ""
            value = ": " + escape("|:", entry[1]) if entry[1] else ""
            return " | {}{}".format(key, value)

        sorted_items = sorted(fields.items(), key=lambda item: item[0])
        return "".join(map(create_field, sorted_items))


def escape(chars, string):
    for char in chars:
        replacement = "\\" + repr(char).replace("'", "").replace("\\", "")
        string = string.replace(char, replacement)
    return string
