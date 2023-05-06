def aba():
    ab='45'
    return ab+'69'
print(aba())

'''
import datetime
nowi=datetime.datetime.now()
time_file=open('times','r')
for line in time_file:
    line=line.rstrip('\n')
    verif_time=line.split(':')
    flagtime=False
    if int(verif_time[0])>nowi.hour:
        flagtime = True
    elif int(verif_time[0])==nowi.hour:
        if int(verif_time[1])>nowi.minute:
            flagtime = True
        elif int(verif_time[1])==nowi.minute:
            if int(verif_time[2]) > nowi.second:
                flagtime=True

    if flagtime:
        print(datetime.datetime.strptime(line,'%X'))
        print(nowi)
        remain_time=datetime.datetime.strptime(line,'%X')-nowi
        print('до конца раунда осталось', remain_time.seconds//60,':', str(remain_time.seconds % 60).zfill(2))
        #return f"до конца раунда осталось {remain_time.seconds//60}:{str(remain_time.seconds % 60).zfill(2)}"
        time_file.close()
        break
'''