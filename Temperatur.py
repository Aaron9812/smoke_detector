# smarter Feuermelder IOX CODING IOT

# Temperaturabfrage
import os, sys, time, datetime
import api

def aktuelleTemperatur():
      
    # 1-wire Slave Datei lesen
    file = open('/sys/bus/w1/devices/28-3c01d607c29f/w1_slave')
    filecontent = file.read()
    file.close()

    # Temperaturwerte auslesen und konvertieren
    stringvalue = filecontent.split("\n")[1].split(" ")[9] #Abfrage des Wertes in Zeile [1] an der Stelle [9]. Hier befindet sich die Temp
    temperature = float(stringvalue[2:]) / 1000 # gibt Wert ab 3. Stelle an, da Wert als "t=23765" angegeben wird

    # Temperatur ausgeben
    rueckgabewert = '%6.2f' % temperature # %6 -->Dezimalzahl wird auf 6 Stellen mit Nullen aufgefüllt, um Kommafehler bei 1-stelligen Celsiuswerten zu vermeiden. 2:--> Komma nach zwei Stellen
    return(rueckgabewert)

schleifenZaehler = 0
Datum = datetime.datetime.now()
schleifenPause = 1

# Ausgabe zu Messbeginn
print ("Temperaturabfrage für ", Datum,
      " Messungen alle ", schleifenPause ," Sekunden gestartet")

# Ausgabe während der Messung
while True:
    messdaten = aktuelleTemperatur()
    Datum = datetime.datetime.now() #aktueller Zeitstempel
    print ("Aktuelle Temperatur : ", messdaten, "°C",
    "in der ", schleifenZaehler, ". Messabfrage", "Zeitstempel: ", Datum)
    adding_data(device_id=1,temp=messdaten)
    time.sleep(schleifenPause)
    schleifenZaehler = schleifenZaehler + 1
    

