from datetime import timedelta

current_time = input().split(":")
explosion_time = input().split(":")
currentTime = list(map(int,current_time))
explosionTime = list(map(int,explosion_time))     



t1 = timedelta(hours=currentTime[0], minutes=currentTime[1],seconds=currentTime[2])
t2 = timedelta(hours=explosionTime[0], minutes=explosionTime[1],seconds=explosionTime[2])


t3 =   t2-t1
s  = abs(t3.seconds)
if s == 0:
    s = 86400
hours, remainder = divmod(s, 3600)
minutes, seconds = divmod(remainder, 60)
print ('{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds)))
