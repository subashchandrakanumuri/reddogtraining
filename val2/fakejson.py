import json
with open('via_region_data.json', 'r') as outfile:
    fakejson =json.load(outfile)
layer1=list(fakejson.keys())[1]
layer2=list(fakejson[layer1].keys())[0]
layer3=list(fakejson[layer1][layer2].keys())[0]
layer3a=list(fakejson[layer1][layer2].keys())[1]
layer4 = fakejson[layer1][layer2][layer3]
layer4a = fakejson[layer1][layer2][layer3a]
imgkey = 'Bonnet_31.jpg'+str(layer4a)
fakejson[layer1][imgkey]=fakejson[layer1].pop(layer2)
fakejson[layer1][list(fakejson[layer1].keys())[0]][layer3]='Bonnet_31.jpg'
with open('via_region_data.json', 'w') as outfile:
    json.dump(fakejson, outfile)
