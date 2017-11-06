#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""replication.py
Copyright 2017 Martin Storgaard Dieu under The MIT License

Written by Martin Storgaard Dieu <martin@storgaarddieu.com>, november 2017
"""
from requests import Response
import json.decoder
import dawa_facade.util.dawa_session
from dawa_facade.responses.sequence_number import SequenceNumber
from dawa_facade.util.exceptions import UnknownContentType, JSONDecodeError


class Replication(object):
    def __init__(self, session: dawa_facade.util.dawa_session.DawaSession):
        self.session = session

    def get_sequence_number(self) -> SequenceNumber:
        """Polls the latest sequence number from DAWA

        All events (create, update or discontinuance) gets a unique sequence number in DAWA.

        :return: The latest sequence number
        """
        # Get the sequence number from DAWA
        response = self.session.get('/replikering/senestesekvensnummer?noformat')  # type: Response

        # Check that the content type is as expected
        content_type = response.headers.get('Content-Type', 'unknown')  # type: str
        if not content_type.startswith('application/json'):
            raise UnknownContentType({'expected': 'application/json', 'got': content_type})

        # Parse the data
        try:
            data = response.json()
        except json.decoder.JSONDecodeError as e:
            raise JSONDecodeError({
                'msg': e.msg,
                'colno': e.colno,
                'lineno': e.lineno,
                'pos': e.pos,
                'doc': e.doc
            })
        # Marshal the response
        return SequenceNumber(**data)
