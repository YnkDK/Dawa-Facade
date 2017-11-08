#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""replication.py
Copyright 2017 Martin Storgaard Dieu under The MIT License

Written by Martin Storgaard Dieu <martin@storgaarddieu.com>, november 2017
"""
import json.decoder

import dawa_facade.util.dawa_session
from dawa_facade.responses.replication.postal_code import PostalCode
from dawa_facade.responses.replication.sequence_number import SequenceNumber
from dawa_facade.util.exceptions import JSONDecodeError
from dawa_facade.util.response_yielder import yield_response


class Replication(object):
    """Handles everything about replication.

    DAWA does not guarantee referential integrity, e.g. it is possible that an address have been created with a street
    code or municipality code, that does not yet reference a section of a street. Your system should handle this.

    Events happens in near real time. The source is the data source for BBR (Bygnings- og Boligregisteret).

    NB: The postal code of an address and supplementary city names are only updated once per day.
    """
    def __init__(self, session: dawa_facade.util.dawa_session.DawaSession):
        self._session = session

    def get_sequence_number(self) -> SequenceNumber:
        """Polls the latest sequence number from DAWA

        All events (insert, update or delete) gets a unique sequence number in DAWA.

        :return: The latest sequence number
        """
        # Get the sequence number from DAWA
        response = self._session.get('/replikering/senestesekvensnummer?noformat')
        # Parse the data
        try:
            data = response.json()
        except json.decoder.JSONDecodeError as e:
            raise JSONDecodeError(status_code=response.status_code, details={
                'msg': e.msg,
                'colno': e.colno,
                'lineno': e.lineno,
                'pos': e.pos,
                'doc': e.doc
            })
        # Marshal the response
        return SequenceNumber(**data)

    def get_postal_codes(self, from_sequence_number=None, to_sequence_number=None):
        """

        :param SequenceNumber | int | None from_sequence_number:
        :param SequenceNumber | int | None to_sequence_number:
        :return:
        """
        if isinstance(from_sequence_number, SequenceNumber):
            from_sequence_number = from_sequence_number.sequence_number
        elif from_sequence_number is None:
            from_sequence_number = 0
        assert isinstance(from_sequence_number, int), 'Invalid from_sequence_number provided'
        if isinstance(to_sequence_number, SequenceNumber):
            to_sequence_number = to_sequence_number.sequence_number
        elif to_sequence_number is None:
            to_sequence_number = self.get_sequence_number().sequence_number
        assert isinstance(to_sequence_number, int), 'Invalid to_sequence_number provided'

        response = self._session.get(
            url='/replikering/postnumre/haendelser',
            params={
                'sekvensnummerfra': from_sequence_number,
                'sekvensnummertil': to_sequence_number,
                'noformat': ''
            }
        )

        for data in yield_response(response=response, response_class=PostalCode):
            yield data

