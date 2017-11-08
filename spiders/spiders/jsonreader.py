import json
path='S:/Desktop/spiders/'
with open(path+'gmooc.json', 'rb') as f:
    data = json.load(f)
    print(len(data))