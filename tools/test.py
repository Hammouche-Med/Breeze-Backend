from datetime import datetime

metar = [ "hjklk", "jlkn", "03", "18","30" ]

m = datetime.now().strftime('%m')
y = datetime.now().strftime('%Y')

obs = metar[2]+"-"+m+"-"+y

d = datetime.now()
dd = datetime(int(y),int(m),int(metar[2]),int(metar[3]),int(metar[4]))

print (obs ,d,dd )

difff = d - dd
diff = difff.total_seconds()/60 - 60

if diff <=  5 :
    print (diff," ph5")
elif diff <= 10 :
    print(diff," ph10")
elif diff <= 33:
    print(diff," ph33")
elif diff <= 49:
    print(diff," ph49")
else :
    print(diff,' omis') 

exp = 244
rec = 243

per = rec / exp * 100

print (per)

t1 = "06:00:00"
t2 = "18:00:00"

print(t1-t2)