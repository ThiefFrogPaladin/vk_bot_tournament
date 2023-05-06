import datetime
nowi=datetime.datetime.now().replace(microsecond=0)
spis=[]
spis.append(str(nowi))
print(nowi)
nowi+=datetime.timedelta(minutes=10)
spis.append(nowi)
print(nowi)

nowi+=datetime.timedelta(minutes=10)
spis.append(nowi)
print(nowi)
nowi+=datetime.timedelta(minutes=10)
spis.append(nowi)
print(nowi)
nowi+=datetime.timedelta(minutes=10)
spis.append(nowi)
print(nowi)
nowi+=datetime.timedelta(minutes=10)
spis.append(nowi)
print(nowi)
print(spis)
print(567)

print(spis[0])
stro=str('2023-05-06 05:38:49')
print(datetime.datetime.strptime(spis[0],"%Y-%m-%d %H:%M:%S"))


print('-----------')
loc=datetime.datetime.now().replace(microsecond=0)
loc=loc.replace(second=0)
print(loc)
