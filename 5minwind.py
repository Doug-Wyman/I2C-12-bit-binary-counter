import mcp_i2c
from time import sleep
import time
import datetime
import sys
import mysql.connector

if len(sys.argv) > 1:
    deviceaddr = sys.argv[1]
else:
    deviceaddr = 0x27
print (deviceaddr)
WindCount = mcp_i2c.counter(1,int(deviceaddr))
WindCount.resetcount() 
LastCount= int(0)
Last24 = [int(0)] * 24



for num in range(1,25):
    RegisterLong = WindCount.getcount()
    if LastCount <= RegisterLong:
        Last24.append(RegisterLong-LastCount)
        print(RegisterLong-LastCount)
    elif LastCount > RegisterLong:
        Last24.append((int(4096) -LastCount) + RegisterLong)
        print((int(4096) -LastCount) + RegisterLong)
    LastCount = RegisterLong
    Last24.pop(0)
    sleep(1.9)
    
#print("INSERT INTO `WindSpeed`(`datetime`, `twosec`) VALUES ( NOW() , '" + str(Last24).strip('[]') + "')")
try:
	cnx = mysql.connector.connect(user='Weather', password='iamweather',
							  host='192.168.0.11',
							  database='Weather')
	#query = "INSERT INTO WindSpeed (`datetime`, `twosec`) VALUES ( NOW() , '" + str(Last24).strip('[]') + "')"
	query = "INSERT INTO anemometer (`datetime`, `01`, `02`, `03`, `04`, `05`, `06`, `07`, `08`, `09`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24` ) VALUES ( NOW() , " + str(Last24).strip('[]') + ")"
	print(query)
	cursor = cnx.cursor()
	cursor.execute(query)
	cnx.commit()
	cursor.close()
	cnx.close()
	print ("updated db WX")
except Exception as e: 
	print(e)
	print ("Error Updating WxDB")
	pass
try:
	cnx = mysql.connector.connect(user='Weather', password='iamweather',
							  host='192.168.0.158',
							  database='weather')
	#query = "INSERT INTO WindSpeed (`datetime`, `twosec`) VALUES ( NOW() , '" + str(Last24).strip('[]') + "')"
	query = "INSERT INTO anemometer (`datetime`, `01`, `02`, `03`, `04`, `05`, `06`, `07`, `08`, `09`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24` ) VALUES ( NOW() , " + str(Last24).strip('[]') + ")"
	print(query)
	cursor = cnx.cursor()
	cursor.execute(query)
	cnx.commit()
	cursor.close()
	cnx.close()
	print ("updated db 158")
except Exception as e: 
	print(e)
	print ("Error Updating 158")
	pass



