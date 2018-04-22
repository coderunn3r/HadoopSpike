#!/usr/bin/env python

import json

import sys


class RawAssetProcessor(object):
    def __init__(self, asset_headers=None):
        if asset_headers is None:
            asset_headers = []
        self.asset_headers = asset_headers

    def generate_asset_header(self, asset_objects):
        for asset_object in asset_objects:
            asset_obj_in_json = json.loads(asset_object)
            if "ServiceNow" == asset_obj_in_json["dataSource"] and asset_obj_in_json["assetType"] == "cmdb_ci_server":
                config_mapping = self.load_config_mapping(asset_obj_in_json["dataSource"].lower())
                config_definition = self.load_config_definition(asset_obj_in_json["dataSource"].lower())
                json_object = self.construct_asset_header(config_mapping,
                                                          config_definition,
                                                          asset_obj_in_json["data"])
                self.asset_headers.append(json_object)

    @staticmethod
    def load_config_mapping(datasource):
        filename = datasource + "_mapping.json"
        with open("main/config/" + filename) as json_data_file:
            data = json.load(json_data_file)
        return data

    @staticmethod
    def load_config_definition(datasource):
        filename = datasource + "_datatype_definition.json"
        with open("main/config/" + filename) as json_data_file:
            data = json.load(json_data_file)
        return data

    @staticmethod
    def construct_asset_header(mapping, config, data):
        return data


temp = []
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    temp.append(line)

rap = RawAssetProcessor()

rap.generate_asset_header(temp)

for asset_header in rap.asset_headers:
    print(str(asset_header))
