#!/usr/bin/env python

import json

from lib.icinga2action import Icinga2Action


class Icinga2AddComment(Icinga2Action):

    def run(self, object_type="Host", filter_string="", filter_vars="", author="", comment=""):
        client = self.get_client()
        #TODO: an empty result is still ok.
        return client.actions.add_comment(object_type=object_type, filter=filter_string, filter_vars=filter_vars, author=author, comment=comment)
