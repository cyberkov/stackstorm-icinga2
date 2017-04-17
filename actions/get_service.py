#!/usr/bin/env python

import json

from lib.icinga2action import Icinga2Action


class Icinga2GetService(Icinga2Action):

    def run(self, services):
        client = self.get_client()

        filters = list()
        for service in services:
            if "!" in service:
                (host, service) = service.split("!", 1)
                filters.append('host.name == "%s" && service.name == "%s"' % (host, service))
            else:
                filters.append('service.name == "%s"' % service)

        print(" || ".join(["(%s)" % f for f in filters]))
        return json.dumps(client.objects.list(
            "Service",
            filter=" || ".join(["(%s)" % f for f in filters])
        ))
