#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""facade.py
Copyright 2017 Martin Storgaard Dieu under The MIT License

Written by Martin Storgaard Dieu <martin@storgaarddieu.com>, november 2017
"""
import requests


class DawaFacade(object):
    base_url = 'https://dawa.aws.dk'

    def __init__(self, base_url: str=None, timeout=305):
        self.timeout = timeout

        if isinstance(base_url, str):
            self.base_url = base_url

        self.session = self._create_session()

    @staticmethod
    def _create_session():
        from . import __version__
        ua = 'Mozilla/5.0 (compatible; Dawa-Facade/{version:s}; +https://github.com/YnkDK/Dawa-Facade)'.format(
            version=__version__
        )
        session = requests.Session()
        session.headers.update({
            'User-Agent': ua
        })
        return session
