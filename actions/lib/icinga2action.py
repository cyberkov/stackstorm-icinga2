from icinga2api.client import Client

from st2actions.runners.pythonrunner import Action


class Icinga2Action(Action):
    def get_client(self, api_url=None, api_user=None, api_password=None):
        if api_url is None:
            api_url = self.config["api_url"]
        if api_user is None:
            api_user = self.config["api_user"]
        if api_password is None:
            api_password = self.config["api_password"]

        return Client(api_url, api_user, api_password)
