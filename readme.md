# Digital HHZ 2.0

Das Herman-Hollerith-Zentrum ([HHZ](https://www.hhz.de)) soll als Forschungszentrum für Digitale Transformation auch infrastrukturell ein positives Beispiel für Digitalisierung sein. 
Deshalb sollen smarte Umgebungen geschaffen werden, in dem digitale Dienste, mittels durch Sensoren und Aktoren erzeugter Daten, die Interaktion der Nutzer mit dem Gebäude bzw. der Lern- und Arbeitsumgebung fördern und die Nutzer im Alltag unterstützen.  

Das Ziel des Digital HHZ 2.0 ist die Bereitstellung einer robusten IoT-Umgebung/Infrastruktur als Enabler für IoT-Projekte, Hackathons und Thesen. 
Dieses Repository dient als Startpunkt für die Teilprojekte und nachfolgende Projekte. 
Es ist als eine Übersicht über alle Tätigkeiten im Projekt konzipiert.
Implementiert wurde ein auf der Low-Code-Platform [Node-RED](https://nodered.org/) und [MQTT](https://mqtt.org/) basiertes Smart-Lab, mit Beispiel-Appliances und Funktionalitäten wie 
* auf [M5Stick-C](https://m5stack.com/products/stick-c) und [Raspberry Pi](https://www.raspberrypi.org/) basierende Sensor-Aktor-Infrastruktur,
* die Publikation von Daten über [MQTT](https://mqtt.org/) und Darstellung in Form eines externen (http://digital.hhz.de) und internen Dashboards, 
* das Plug’n’Play Device und Appliance Management mittels [mDNS](http://www.multicastdns.org/) bzw. [avahi](https://www.avahi.org/) und [ThingsBoard](https://thingsboard.io/), 
* das Konzept und die Implementierung einer nachhaltigen Datenhaltung mit Hilfe des TICK-Stacks bestehend aus [Telegraf, InfluxDB, Chronograf, Kapacitor](https://www.influxdata.com/products/influxdb-overview/), 
* die teilautomatisierte Fehlererkennung und 
* das Testen von Appliances. 

In der Dokumentation werden die einzelnen Bestandteile (Software- und Hardwarekomponenten), sowie weitere Technologien und ihre Installation und Konfiguration beschrieben.

1. Digital HHZ 2.0
1. Trello Dokumentation
1. Architektur
1. Zugang zum Digital HHZ Netzwerk
2. Verwendete Softwarekomponenten
2. MQTT
2. NodeRed
2. Homie Konvention
2. InfluxDB
2. Chronograf
2. Telegraf
2. Einführung in Service Discovery
2. ThingsBoard
3. Verwendete Hardwarekomponenten
3. Raspberry Pi
3. M5Sticks
3. Tasmota Lampe
4. Einrichtung Mosquitto Broker
4. Installation
4. Topics
4. Bridging
5. HHZ Dashboard
5. Digital HHZ
5. Monitoring & Service Discovery
5. Service Discovery mit Avahi
5. Simulation
5. InfluxDB Chronograf
5. ThingsBoard
5. ThingsBoard Devices
5. ThingsBoard Appliances
6. Device Management
6. Unterscheidung Geräte und Objekte
6. Anlegen eines Gerätes
6. Zuordnung physisches Gerät<-->Datenobjekt
6. Dashboard
6. ThingsBoard Dokumentation
7. Datenmanagement
7. ER-Modell
7. Wie sind die Daten zu verstehen?
7. Wie sind die Daten zu verarbeiten?
7. InfluxDB
7. Telegraf
7. Chronograf
7. Backup und Dropbox Uploader
7. DigitalHHZ2MonthlyUploader Dropbox developer App
7. Daten-Replay
8. Fehlermanagement im Digital HHZ
9. Aufsetzen einer neuen Appliance
9. Aufsetzen des Raspberry Pis
9. Node-RED Installation
9. Erklärung des MQTT Datenflusses
9. Broker Konfiguration
9. Erklärung der Topic Struktur
9. Weitere Schritte
