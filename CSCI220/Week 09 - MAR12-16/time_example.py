from datetime import datetime

##current = datetime.now()
##fixed = current.strftime("%d-%H-%M-%S")
##part = fixed.split('-')
##
##for i in range(len(part)):
##    part[i] = int(part[i])
    


##current  = datetime.now()
##broken = current.strftime("%y-%m-%d-%H-%M-%S")
##arrayed = broken.split('-')
##
##for i in range(len(arrayed)):
##    arrayed[i] = int(arrayed[i])
##
##whole = (arrayed[0] * 10000 + arrayed[1] * 100 + arrayed[2]) + ((arrayed[3] * 3600 + arrayed[4] * 60 + arrayed[5]) / 100000)


stamp = '03/17/2012 13:00:00'
arrayed = []
arrayed.append(int(stamp[8:10]))
arrayed.append(int(stamp[0:2]))
arrayed.append(int(stamp[3:5]))
arrayed.append(int(stamp[11:13]))
arrayed.append(int(stamp[14:16]))
arrayed.append(int(stamp[17:19]))
whole = (arrayed[0] * 10000 + arrayed[1] * 100 + arrayed[2]) + ((arrayed[3] * 3600 + arrayed[4] * 60 + arrayed[5]) / 100000)


print(whole)
