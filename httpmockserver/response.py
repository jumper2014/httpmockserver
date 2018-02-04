#!/usr/bin/env python
# coding=utf-8


class Response(object):
    def __init__(self, status_code, content, fmt="text"):
        self.status_code = status_code
        self.content = content
        self.fmt = fmt


if __name__ == '__main__':
    pass