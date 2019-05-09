import json
annotations = json.load(open( "via_region_data.json"))
annotations = list(annotations.values())  # don't need the dict keys
annotations1 = annotations[1]
annotations2 = list(annotations1.values())
annotations2 = [a for a in annotations2 if a['regions']]
# Add images
i=0
for a in annotations2:
    # Get the x, y coordinaets of points of the polygons that make up
    # the outline of each object instance. These are stores in the
    # shape_attributes (see json format above)
    # The if condition is needed to support VIA versions 1.x and 2.x.
    if type(a['regions']) is dict:
        polygons = [r['shape_attributes'] for r in a['regions'].values()]
    else:
        polygons = [r['shape_attributes'] for r in a['regions']]

    objects = [s['region_attributes'] for s in a['regions']]

    i=i+1
    for n in objects:
        print(n,i)

    class_ids = [n['code'] for n in objects]
