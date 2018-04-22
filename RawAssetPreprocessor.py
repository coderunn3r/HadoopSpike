import sys

from main.config.constants import *
from main.raw_asset_getter.RawAssetGetter import *


class RawAssetPreProcessor(object):
    """Raw Asset Pre Processor is used to pre process the asset snapshots.

    Attributes:
        asset_objects: all assets in core.
    """

    def __init__(self, asset_objects=None):
        if asset_objects is None:
            asset_objects = []
        self.asset_objects = asset_objects



    def raw_assets_preprocessor(self, assets):
        for asset in assets:
            resp = RawAssetGetter.get_lumada_response(url + ads + "assets/" + asset["id"] + "/snapshot", headers,
                                                      proxyDict)
            res_data = json.loads(resp.text)
            json_object = {'data': res_data["latestSnapshot"]["data"]["data"]}
            asset_metadata = json.loads(res_data["latestSnapshot"]["data"]["metadata"])
            json_object.update(asset_metadata)
            self.asset_objects.append(json.dumps(json_object))



temp = []
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    temp.append(line)

print("In raw asset getter...")
ag = RawAssetGetter(temp)
assets = ag.get_assets()
