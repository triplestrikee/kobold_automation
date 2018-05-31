file  = open('ee684b16-b790-4cfa-b8e4-b077455cda2.fba', 'r').read()
str  = '''AggregationReport","Payload":{"AggregationType":"FrameAnalysis","Snapshot":{"Type":1,"Name":"Slice'''
count = file.count(str)

print(count)

