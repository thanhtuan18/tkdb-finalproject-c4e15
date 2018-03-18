import mlab
from models.evaluate import Evaluate

mlab.connect()

average = []

total = Evaluate.objects()

# designlist = []


# for i in total:
#     print (i['design'])
#     designlist.append(i['design'])
#
# print(len(designlist))
# tong = sum(designlist)
# print(tong)

total.delete()
