#!/usr/bin/env python
# coding=utf-8


import json
from flask import Flask
from flask import make_response
from request import Request
from response import Response

app = Flask(__name__)
rules = list()


def make_view_func(i):
    def func():
        resp = rules[i][1]
        req = rules[i][0]
        if request.method == '':
            pass

        response = make_response(resp.content, resp.status_code)
        if resp.fmt == 'json':
            response.headers['Content-Type'] = 'Application/json'
        return response

    return func


if __name__ == '__main__':

    # Load JSON configuration
    with open('mock.json', 'r') as f:
        configs = json.load(f)

        for config in configs:
            request = dict()
            response = dict()
            req_uri = config.get('request').get('uri')
            req_method = config.get('method', 'get')
            request = Request(uri=req_uri, method=req_method)

            resp_status_code = config.get('response').get('status_code', 200)
            resp_fmt = config.get('response').get('format')
            resp_content = config.get('response').get('content')
            response = Response(status_code=resp_status_code, content=resp_content, fmt=resp_fmt)

            # save request and response
            rules.append((request, response))

        # create url rules
        for i in range(len(configs)):
            request = rules[i][0]
            response = rules[i][1]
            app.add_url_rule(request.uri, endpoint='{0}'.format(i), view_func=make_view_func(i))

        # start application
        app.run(host='0.0.0.0', port=8080)
