#!/usr/bin/env python

import json

from lib.icinga2action import Icinga2Action


class Icinga2AcknowledgeProblem(Icinga2Action):

    def run(self, object_type, filter_string, filter_vars, author, comment, expiry, sticky, notify):
        self.logger.info(
                'Icinga2AcknowledgeProblem initialized with:\n object_type: %s,\n filter_string: %s,\n filter_vars: %s,\n author: %s,\n comment: %s,\n expiry: %s,\n sticky: %s,\n notify: %s',
            object_type, filter_string, filter_vars, author, comment, expiry, sticky, notify)
        client = self.get_client()
        #TODO: an empty result is still ok.
        return client.actions.acknowledge_problem(
            object_type=object_type,
            filter=filter_string,
            filter_vars=filter_vars,
            author=author,
            comment=comment,
            expiry=expiry,
            sticky=sticky,
            notify=notify
            )

