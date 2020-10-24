# Digital HHZ 2.0

Das Herman-Hollerith-Zentrum (HHZ) soll als Forschungszentrum für Digitale Transformation auch infrastrukturell ein positives Beispiel für Digitalisierung sein. 
Deshalb sollen smarte Umgebungen geschaffen werden, in dem digitale Dienste, mittels durch Sensoren und Aktoren erzeugter Daten, die Interaktion der Nutzer mit dem Gebäude bzw. der Lern- und Arbeitsumgebung fördern und die Nutzer im Alltag unterstützen.  

Das Ziel des Digital HHZ 2.0 ist die Bereitstellung einer robusten IoT-Umgebung/Infrastruktur als Enabler für IoT-Projekte, Hackathons und Thesen. 
Dieses Repository dient als Startpunkt für die Teilprojekte und nachfolgende Projekte. 
Es ist als eine Übersicht über alle Tätigkeiten im Projekt konzipiert.
Implementiert wurde ein auf der Low-Code-Platform Node-RED und MQTT basiertes Smart-Lab, mit Beispiel-Appliances und Funktionalitäten wie 
auf M5Stick-C und Raspberry Pi basierende Sensor-Aktor-Infrastruktur,
die Publikation von Daten über MQTT und Darstellung in Form eines externen und internen Dashboards, 
das Plug’n’Play Device und Appliance Management, 
das Konzept und die Implementierung einer nachhaltigen Datenhaltung, 
die teilautomatisierte Fehlererkennung und 
das Testen von Appliances. 

In der Dokumentation werden die einzelnen Bestandteile (Software- und Hardwarekomponenten), sowie weitere Technologien und ihre Installation und Konfiguration beschrieben.

1 Digital HHZ 2.0
1.1 Trello Dokumentation
1.2 Architektur
1.3 Zugang zum Digital HHZ Netzwerk
2 Verwendete Softwarekomponenten
2.1 MQTT
2.2 NodeRed
2.3 Homie Konvention
2.4 InfluxDB
2.5 Chronograf
2.6 Telegraf
2.7 Einführung in Service Discovery
2.8 ThingsBoard
3 Verwendete Hardwarekomponenten
3.1 Raspberry Pi
3.2 M5Sticks
3.3 Tasmota Lampe
4 Einrichtung Mosquitto Broker
4.1 Installation
4.2 Topics
4.3 Bridging
5 HHZ Dashboard
5.1 Digital HHZ
5.2 Monitoring & Service Discovery
5.3 Service Discovery mit Avahi
5.4 Simulation
5.5 InfluxDB Chronograf
5.6 ThingsBoard
5.7 ThingsBoard Devices
5.8 ThingsBoard Appliances
6 Device Management
6.1 Unterscheidung Geräte und Objekte
6.2 Anlegen eines Gerätes
6.3 Zuordnung physisches Gerät<-->Datenobjekt
6.4 Dashboard
6.5 ThingsBoard Dokumentation
7 Datenmanagement
7.1 ER-Modell
7.2 Wie sind die Daten zu verstehen?
7.3 Wie sind die Daten zu verarbeiten?
7.4 InfluxDB
7.5 Telegraf
7.6 Chronograf
7.7 Backup und Dropbox Uploader
7.8 DigitalHHZ2MonthlyUploader Dropbox developer App
7.9 Daten-Replay
8 Fehlermanagement im Digital HHZ
9 Aufsetzen einer neuen Appliance
9.1 Aufsetzen des Raspberry Pis
9.2 Node Red Installation
9.3 Erklärung des MQTT Datenflusses
9.4 Broker Konfiguration
9.5 Erklärung der Topic Struktur
9.6 Weitere Schritte
