#/usr/bin/python

def solution(S):
    import datetime
    x = datetime.datetime.now()
    print(S)
    todaytime = x.strftime("%Y-%m-%d %H:%M:%S")
    matched = [line for line in S.split('\n')]
    City = []
    for i in range(len(matched)):
        City.append(matched[i].split(',')[1].strip())
    City = (list(dict.fromkeys(City)))
    Result = []
    for i in sorted(City):
        LINE = []
        for line in S.split('\n'):
            if i == (line.split(',')[1].strip()):
                time = (line.split(',')[2].strip())
                todaytime1 = datetime.datetime.strptime(todaytime, "%Y-%m-%d %H:%M:%S")
                pictime = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
                TIMEDIFF = ((todaytime1 - pictime))#.seconds/60)
                D = (str(TIMEDIFF).split(' ')[0])
                H = (str(TIMEDIFF).split(' ')[2].split(':')[0])
                M = (str(TIMEDIFF).split(' ')[2].split(':')[1])
                ActualTIMEDIFF = (int(D)*24*60) + (int(H)*60) + int(M)
                NEWLINE = (str(ActualTIMEDIFF)+", "+line.split(',')[1].strip())
                LINE.append(NEWLINE)
        SORTEDLINE = (sorted(LINE, reverse=True))
        for PIC in range(1, len(SORTEDLINE)+1):
            XX = (SORTEDLINE[PIC - 1].split(' ')[1]+(format(PIC, '02d')))
            print(XX)
            Result.append(XX)
    print(Result)


String = """photo.jpg, Warsaw, 2013-09-05 14:08:15
john.png, London, 2015-06-20 15:13:22
myFriends.png, Warsaw, 2013-09-05 14:07:13
Eiffel.jpg, Paris, 2015-07-23 08:03:02
pisatower.jpg, Paris, 2015-07-22 23:59:59
BOB.jpg, London, 2015-08-05 00:02:03
notredame.png, Paris, 2015-09-01 12:00:00
me.jpg, Warsaw, 2013-09-06 15:40:22
a.png, Warsaw, 2016-02-13 13:33:50
b.jpg, Warsaw, 2016-01-02 15:12:22
c.jpg, Warsaw, 2016-01-02 14:34:30
d.jpg, Warsaw, 2016-01-02 15:15:01
e.png, Warsaw, 2016-01-02 09:49:09
f.png, Warsaw, 2016-01-02 10:55:32
g.jpg, Warsaw, 2016-02-29 22:13:11"""

solution(String)
