import json

import requests
from hdfs import InsecureClient

from main.config.constants import *

from main.config.properties import *

requests.urllib3.disable_warnings(requests.urllib3.exceptions.InsecureRequestWarning)




class RawAssetGetter(object):
    """Asset getter is used to get assets from lumada.

    Attributes:
        assets: all assets in core.
    """

    def __init__(self, assets=None):
        if assets is None:
            assets = []
        self.assets = assets

    def get_assets(self, continuation_token=None):
        """Return the assets in core"""
        headers['X-Lumada-Continuation-Token'] = continuation_token
        resp = self.get_lumada_response(url + ams + "assets", headers, proxyDict)
        data = json.loads(resp.text)
        return data["contents"]

    def get_all_assets(self, continuation_token=None):
        """Return all the assets in core"""
        while True:
            headers['X-Lumada-Continuation-Token'] = continuation_token
            resp = self.get_lumada_response(url + ams + "assets", headers, proxyDict)
            data = json.loads(resp.text)
            continuation_token = data["continuationToken"]
            self.assets = self.assets + data["contents"]
            if continuation_token is None:
                break
        return self.assets

    def get_asset(self, asset_id):
        resp = self.get_lumada_response(url + ams + "assets/" + asset_id, headers, proxyDict)
        data = json.loads(resp.text)
        return data

    def get_asset_snapshot(self, asset_id):
        resp = self.get_lumada_response(url + ams + "assets/" + asset_id, headers, proxyDict)
        data = json.loads(resp.text)
        return data

    @staticmethod
    def get_lumada_response(url, headers, proxyDict):
        resp = requests.get(url=url, headers=headers, proxies=proxyDict, verify=False)
        if resp.status_code == requests.codes.ok:
            return resp
        else:
            raise Exception('Status code not okay..')

#
# print("In raw asset getter...")
# ag = RawAssetGetter()
# assets = ag.get_assets()
#
# # Connecting to Webhdfs by providing hdfs host ip and webhdfs port (50070 by default)
# client = InsecureClient('http://127.0.0.1:50070')
#
# with client.write('/user/kagopalakrishnan/output/assets', encoding='utf-8') as writer:
#     for asset in assets:
#         writer.write(str(asset) + "\n")
