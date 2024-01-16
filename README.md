Versuch M5 - Mathematisches Pendel (Medieningenieur:in, 3. Semester)
Projekt von Jonathan Michel, Miriam Bernhardt, Hannah Neppert

Das Programm dient dazu, die Messungen des Laborversuchs "Mathematisches Pendel" durchzuführen und die Messwerte anzuzeigen und als XLS Datei zu exportieren.

Vorbereitung:
Beim Start des Raspberry Pis öffnet sich das Programm automatisch. (Zugangsdaten Raspberry Pi: Username: "ming" Passwort: "laborm5")
Außerdem lässt sich das Programm auch über eine Desktop-Verknüpfung "PendelM5" öffnen.
Der Raspberry Pi ist im Netzwerk von einem ESP.
Es kann auch von anderen Endgeräten auf das Programm zugegriffen werden. Dafür sind folgende Schritte notwendig:
1. Verbindung mit dem Wlan-Netzwerk "VersuchM5", Passwort: "passwort"
2. Öffnen eines Browsers
3. Eingeben der IP-Adresse des Raspberry Pis in die Suchzeile: "......." (Falls zukünftig ein anderes Netzwerk verwendet wird, muss die IP-Adresse angepasst werden.)


Bedienung des Programms:
Der Magnet ist zu Beginn des Versuchs eingeschaltet und hält das Pendel dadurch fest.
Wenn sich das Programm im Browser geöffnet hat, kann der Versuch über den Button "Messung starten" gestartet werden.
Der Magnet wird dadurch ausgeschaltet und das Pendel fängt an, sich zu bewegen. 
Die Zeit misst das Programm für 10 Pendelschwingungen einzeln und zeigt die Werte direkt an.
Nach 10 Messungen wird der Magnet wieder eingeschaltet und stoppt somit die Schwinungen.
Wenn die Messung abgeschlossen ist, können die Ergebnisse über den Button "Messdaten herunterladen" auf dem jeweiligen Gerät gespeichert werden.
Als Datei erhält man eine .xls-Datei, die direkt mit Excel geöffnet werden kann.

Abbruch des Messung:
Falls die Messung neugestartet werden muss, kann dies über den Button "Messung abbrechen" erfolgen. Die Messwerte werden dann zurückgesetzt und die Messung kann neu gestartet werden.

Starten des Programms über die Konsole:
1. Start der Konsole
2. Starten des Programms: Versuch-M5/python app.py

Beenden des Programms über die Konsole:
1. Starten der Konsole (neuer Tab)
2. folgenden Befehl eingeben: pkill -9 python






Zum Programm-Code:
Das Programm verwendet einen Flask-Server, um auf einer Webseite zu laufen.
Es wurden folgende Bibliotheken heruntergeladen:
Flask
Flask_Classful
pyautogui
xlsxwriter




