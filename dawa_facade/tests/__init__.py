#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""__init__.py
Copyright 2017 Martin Storgaard Dieu under The MIT License

Written by Martin Storgaard Dieu <martin@storgaarddieu.com>, november 2017
"""
from dawa_facade import DawaFacade

dawa = DawaFacade()
print(dawa.replication.get_postal_codes())