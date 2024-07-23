#convert time in 12hr format
#time='20:34:55'
#o/p=8:00

time='20:59:59'
time=time.split(':')
hrs=time[0]
min=time[1]
sec=time[2]
if int(hrs)>12:
    hrs=int(hrs)-12
if int(min)>59:
    hrs=int(hrs)+1
    min=0
if int(sec)>59:  
    min=int(min)+1
    sec=0  
print(str(hrs)+':'+str(min)+':'+str(sec))
#this is for min and sec >59
time='14:70:59'
time=time.split(':')
hrs=time[0]
min=time[1]
sec=time[2]
if int(hrs)>=12:
    hrs=int(hrs)-12
if int(min)>59:
    hrs=int(hrs)+1
    min=int(min)-60
if int(sec)>59:  
    min=int(min)+1
    sec=int(sec)-60
print(str(hrs)+':'+str(min)+':'+str(sec))
