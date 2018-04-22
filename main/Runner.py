from main.raw_asset_preprocessor.RawAssetPreprocessor import RawAssetPreProcessor
from main.raw_asset_getter.RawAssetGetter import RawAssetGetter
from main.raw_asset_processor.RawAssetProcessor import RawAssetProcessor

#print("In raw asset getter...")
ag = RawAssetGetter()
assets = ag.get_assets()


#print("In raw asset preprocessor...")
raf = RawAssetPreProcessor()
raf.raw_assets_preprocessor(assets)

#print("In raw asset processor...")
rap = RawAssetProcessor()
rap.generate_asset_header(raf.asset_objects)

for asset_header in rap.asset_headers:
    print(asset_header)
