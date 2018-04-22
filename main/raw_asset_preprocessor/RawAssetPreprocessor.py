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



print("In raw asset getter...")
ag = RawAssetGetter()
assets = ag.get_assets()


print("In raw asset preprocessor...")
raf = RawAssetPreProcessor()
raf.raw_assets_preprocessor(assets)

# Connecting to Webhdfs by providing hdfs host ip and webhdfs port (50070 by default)
client = InsecureClient('http://127.0.0.1:50070')

with client.write('/user/kagopalakrishnan/output/asset_objects', encoding='utf-8') as writer:
    for asset_object in raf.asset_objects:
        writer.write(str(asset_object) + "\n")
