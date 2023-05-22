
# hallo
# laufzeit  von  dem  openvpn-daemon  pruefen
# die Datei openvpn.log lesbar oeffnen und
# zeilenweise ausgeben
# teste ob erfolgmsg gefunden -> Alarm connection found
# teste ob du ein Fehlermdg hast,wenn ja gib ihn aus
# teste ob x eingeben worden ist, fall nicht springe an den anfang der Schleife
# gibt nur eine Zusammenfassung aus

import os

scanline = ""
connect = 0
disconnect = 0
make = 0
			
def detect_failed():
	global saneline
	global connect
	global disconnect
	global make

	if ( "SIGUSR1" in scanline):
		print("Disconnect")
		disconnect += 1
		
	if ("MULTI: multi_create_instance called"  in scanline):
		print("  <new instance> ")
		make += 1

	if("VERIFY OK: depth=0" in scanline):
		print("  <<CONNECT>>")
		connect += 1


print("Hallo Word")

file = open("/var/log/openvpn.log")

for line in file:
	scanline = line.rstrip()
	detect_failed()
# print(scanline:1:3)
	print(line.rstrip())

file.close()
print(os.system("date"))

print("Connect : %d   Make : %d  disconnect = %d" % (connect,make,disconnect));
