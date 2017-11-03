#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""exceptions.py
Copyright 2017 Martin Storgaard Dieu under The MIT License

Written by Martin Storgaard Dieu <martin@storgaarddieu.com>, november 2017
"""


class DawaException(Exception):
    """The base exception

    The exception that all other exceptions inherit from.
    Follows the specification in https://dawa.aws.dk/generelt#fejlhaandtering
    """
    title = ''
    details = dict()
