#!/usr/bin/env python

import json

from lib.icinga2action import Icinga2Action


class Icinga2GetStatus(Icinga2Action):

    def run(self):
        client = self.get_client()
        return client.status.list()
