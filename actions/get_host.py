#!/usr/bin/env python

import json

from lib.icinga2action import Icinga2Action


class Icinga2GetHost(Icinga2Action):

    def run(self, hosts):
        client = self.get_client()
        return json.dumps(client.objects.list("Host", filter="host.name in hosts", filter_vars={"hosts": hosts}))
