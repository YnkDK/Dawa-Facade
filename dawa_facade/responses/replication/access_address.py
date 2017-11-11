#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""access_address.py
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Martin Storgaard Dieu <ms@intramanager.com>, november 2017
"""
import datetime
import uuid

from dawa_facade.responses import BaseResponse, parse_datetime


class AccessAddressData(BaseResponse):
    """

    """

    def __init__(self, **kwargs) -> None:
        kwargs['id'] = uuid.UUID(kwargs['id'])
        kwargs['status'] = int(kwargs['status'])
        kwargs['accuracy'] = int(kwargs['nøjagtighed'])

        # Optionals
        kwargs['created_datetime'] = parse_datetime(kwargs.get('oprettet', None))
        kwargs['updated_datetime'] = parse_datetime(kwargs.get('ændret', None))
        kwargs['commencement_datetime'] = parse_datetime(kwargs.get('ikrafttrædelsesdato', None))
        kwargs['municipality_code'] = kwargs.get('kommunekode', None)
        kwargs['street_code'] = kwargs.get('vejkode', None)
        kwargs['house_number'] = kwargs.get('husnr', None)
        kwargs['local_city_name'] = kwargs.get('supplerendebynavn', None)
        kwargs['postal_code'] = kwargs.get('postnr', None)
        kwargs['postal_code'] = kwargs.get('postnr', None)
        kwargs['etrs89_east'] = kwargs.get('etrs89koordinat_øst', None)
        kwargs['etrs89_north'] = kwargs.get('etrs89koordinat_nord', None)
        kwargs['source'] = kwargs.get('kilde', None)
        kwargs['house_number_source'] = kwargs.get('husnummerkilde', None)
        kwargs['technical_standard'] = kwargs.get('tekniskstandard', None)
        kwargs['text_orientation'] = kwargs.get('tekstretning', None)
        kwargs['address_point_updated_datetime'] = parse_datetime(kwargs.get('adressepunktændringsdato', None))
        kwargs['esdh_reference'] = kwargs.get('esdhreference', None)
        kwargs['journal_number'] = kwargs.get('journalnummer', None)
        kwargs['height'] = kwargs.get('højde', None)
        kwargs['access_point_identifier'] = kwargs.get('adgangspunktid', None)
        if kwargs['access_point_identifier'] is not None:
            kwargs['access_point_identifier'] = uuid.UUID(kwargs['access_point_identifier'])

        # The following fields are deprecated and are no longer updated
        kwargs.pop('ejerlavkode', None)
        kwargs.pop('matrikelnr', None)
        kwargs.pop('esrejendomsnr', None)
        super().__init__(**kwargs)



class AccessAddressEvent(BaseResponse):
    """A sequence number

    A unique sequence number for an event in DAWA

    """
    def __init__(self, **kwargs) -> None:
        kwargs['sequence_number'] = int(kwargs['sekvensnummer'])
        kwargs['timestamp'] = parse_datetime(kwargs['tidspunkt'])
        kwargs['data'] = AccessAddressData(**kwargs['data'])
        kwargs['operation'] = kwargs['operation'].lower()
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
    def operation(self) -> str:
        """The type of event: insert, update, delete

        :return: The type of the event (operation)
        """
        return super().get('operation')

    @property
    def data(self) -> AccessAddressData:
        """The data

        :return: The data (data)
        """
        return super().get('data')
