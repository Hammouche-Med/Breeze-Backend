from datetime import datetime


def readMsg(filePath):
    with open(filePath) as f:
        lines = f.readlines()
        return lines

def msgDcd (filePath):
    msg = readMsg(filePath)
    msgElements = msg[0].split(" ")
    
    decodedMsg = {
        "type" : msgElements[0],
        "OACI" : msgElements[1],
        "content" : msg,
        "date_reception" : datetime.now().strftime('%Y-%m-%d %H:%M:00'),

        # TODO::fix wrong year and month
        "date_message" : datetime.now().combine(datetime.strptime(msgElements[2][0:2], "%d"), datetime.strptime(msgElements[2][2:6],"%H%M").time()).strftime('%Y-%m-%d %H:%M:00'),
    }
    print(decodedMsg)

msgDcd("METAR.txt")
