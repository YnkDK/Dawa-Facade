#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""postal_code.py
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Martin Storgaard Dieu <ms@intramanager.com>, november 2017
"""
import datetime

from dawa_facade.responses import BaseResponse, parse_datetime


class PostalCodeData(BaseResponse):
    """

    """

    def __init__(self, **kwargs) -> None:
        kwargs['postal_code'] = kwargs['nr']
        kwargs['name'] = kwargs['navn']
        kwargs['is_major_recipient'] = kwargs['stormodtager']
        del kwargs['nr']
        del kwargs['navn']
        del kwargs['stormodtager']
        super().__init__(**kwargs)


class PostalCode(BaseResponse):
    """A sequence number

    A unique sequence number for an event in DAWA

    """
    def __init__(self, **kwargs) -> None:
        kwargs['sequence_number'] = int(kwargs['sekvensnummer'])
        kwargs['timestamp'] = parse_datetime(kwargs['tidspunkt'])
        kwargs['data'] = PostalCodeData(**kwargs['data'])
        del kwargs['sekvensnummer']
        del kwargs['tidspunkt']
        super().__init__(**kwargs)

    @property
    def sequence_number(self) -> int:
        """The sequence number for the event

        :return: The sequence number (sekvensnummer)
        """
        return super().get('sequence_number')

    @property
    def timestamp(self) -> datetime.datetime:
        """The timestamp for the event

        :return: The timestamp (tidspunkt)
        """
        return super().get('timestamp')

    @property
    def data(self) -> PostalCodeData:
        """The data

        :return: The data (data)
        """
        return super().get('data')
