import json

annotations = json.load(open( "via_region_data.json"))
for data in annotations['_via_img_metadata']:
    print(annotations['_via_img_metadata'][data]['filename'])
    for internals in annotations['_via_img_metadata'][data]['regions']:
        print(internals['shape_attributes'])
        print(internals['region_attributes'])
