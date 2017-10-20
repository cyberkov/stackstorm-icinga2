#!/usr/bin/env python

from lib.icinga2action import Icinga2Action

class Icinga2AddComment(Icinga2Action):

    def run(self, object_type, services, force_check=True, next_check=""):
        client = self.get_client()

        filters = list()
        for service in services:
            if object_type == "Service":
                if "!" in service:
                    (host, service) = service.split("!", 1)
                    filters.append('host.name == "%s" && service.name == "%s"' % (host, service))
                else:
                    filters.append('service.name == "%s"' % service)
            else:
                filters.append('host.name == "%s"' % service)

        self.logger.info(" || ".join(["(%s)" % f for f in filters]))
        return client.actions.reschedule_check(
            object_type=object_type,
            filter=" || ".join(["(%s)" % f for f in filters]),
            next_check=next_check,
            force_check=force_check
        )

