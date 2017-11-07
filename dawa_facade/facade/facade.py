#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""facade.py
Copyright 2017 Martin Storgaard Dieu under The MIT License

Written by Martin Storgaard Dieu <martin@storgaarddieu.com>, november 2017
"""
from dawa_facade.facade.replication import Replication
from dawa_facade.util.dawa_session import DawaSession
import requests.adapters


class DawaFacade(object):
    base_url = 'https://dawa.aws.dk'
    adapter = requests.adapters.HTTPAdapter()

    def __init__(self, base_url: str=None, timeout=305):
        self.timeout = timeout

        if isinstance(base_url, str):
            self.base_url = base_url

        self.session = self._create_session()
        self.replication = Replication(self.session)

    def _create_session(self):
        from dawa_facade import __version__
        ua = 'Mozilla/5.0 (compatible; Dawa-Facade/{version:s}; +https://github.com/YnkDK/Dawa-Facade)'.format(
            version=__version__
        )
        session = DawaSession(self.base_url)
        session.headers.update({
            'User-Agent': ua,
            'Accept': 'application/json'
        })
        session.mount(self.base_url, self.adapter)
        return session
