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

Die Projektplanung und das Anforderungs- und Aufgabenmanagement wurde über Trello durchgeführt. Unser Trello-Board ist unter folgender URL erreichbar:
https://trello.com/b/O8KbgCGB/digital-hhz-20

Um einen schnellen Überblick über unsere Architektur zu geben, ist hier eine Zusammenfassung des Kapitels Architektur unsere Projektdokumentation:

![Abbildung 1 Digital HHZ Architekturbild](/Architekturbild.png)

Die Abbildung zeigt ein Gesamtbild der verwendeten Technologien sowie die Interaktion der Komponenten untereinander. Die linke Seite stellt die aktuelle Implementierung im Raum 125 dar. Hier sind die Sensoren (*M5Sticks*) und Aktoren (*Tasmota-Lampe*) installiert. Die Sensoren und Aktoren kommunizieren über MQTT mit dem lokalen *MQTT-Broker*, der auf *Mosquitto* basiert und welcher im Raum 121 auf einem physischen Server (*Raspberry Pi*) installiert wurde. Die Daten der Sensoren und Aktoren werden auf weitere Mosquitto-Broker gespiegelt (Bridging). Ein zweiter Mosquitto-Broker wird im SmartLab auf einer virtuellen Maschine (*Broker-VM*) gehosted.

Die *Digital-HHZ-Webseite* (externes Dashboard), welche von außerhalb des Digital-HHZ-Netzwerks (extern) über http://digital.hhz.de zu erreichen ist, wird auf einem Strato-Server gehosted. Auf dieser Seite werden die aktuell gemessenen Sensorwerte pro Raum aufgelistet und das Projekt kurz vorgestellt. Die Digital-HHZ-Webseite sowie das *interne Dashboard* wurden mit der Low-Code-Plattform *Node-RED* entwickelt. Das interne Dashboard wird auf der *Nodered-VM* gehosted. Das interne Dashboard kann nur aufgerufen werden, wenn man im Digital-HHZ-Netzwerk eingeloggt ist.

Auf den Sensoren und Aktoren werden QR-Codes angebracht. Mithilfe dieser können Gerätedaten, sowie deren Zugehörigkeit nachvollzogen werden, indem ein QR-Code-Scanner, bspw. Smartphone, das im Digital-HHZ-Netzwerk eingeloggt ist, diesen QR-Code scannt. Man wird daraufhin automatisch auf eine gerätespezifische Seite innerhalb des *internen Dashboards* weitergeleitet und erhält alle notwendigen Informationen über das Gerät selbst und dessen Zugehörigkeit. Die Daten hierfür stammen aus der Device-Management-Software *ThingsBoard*, die ebenfalls auf der *Nodered-VM* installiert wurde. Die Daten werden vom *internen Dashboard* über die *ThingsBoard-API* abgerufen.

Auf der *DB-VM* wird der *Backup-Service* gehosted, welcher aus dem Zeitreihen-Datenbank-Management-System *InfluxDB*, sowie den weiteren Komponenten des TICK-Stacks (*Telegraf, Kapacitor und Chronograf*) besteht. Dieser Dienst holt sich über *Telegraf* von der *Broker-VM* alle Werte und speichert sie in einer Datenbank ab. Zu jedem Monatsanfang wird ein Backup der Datenbank erstellt und automatisch an *Dropbox* hochgeladen. Backups können jedoch auch manuell erstellt werden. Über *Chronograf* wurden Dashboards für die Analyse und den csv-Export der Daten erstellt und können intuitiv über das Web-Interface von *Chronograf* erweitert werden.

Jede VM sowie jeder Raspberry Pi (ob Appliance oder Broker-Pi) muss seine angebotenen Dienste über mDNS/DNS-SD (z.B. *Avahi*) veröffentlichen. *Avahi* wird benötigt, um die Geräte/Services im Digital-HHZ zugreifbar zu machen, ohne dass die IP-Adresse bekannt ist.
