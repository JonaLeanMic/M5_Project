import RPi.GPIO as GPIO
import time

# Variablen
Schwingungen = 10  #
Counter = 0  #
Ausloesungen = 0
StartZeit = 0
EndZeit = 0
ZwischenzeitAlt = 0
Zeit = 0

# Pinreferenz wählen
GPIO.setmode(GPIO.BCM)
# Pi 23 als Ausgang für die LED
LED_Pin = 23
GPIO.setup(LED_Pin, GPIO.OUT)
# Pin 18 als Interruptpin mit Pullup Widertand
# dies ist der EIngang der Lichtschranke
Interrupt_Pin = 18
GPIO.setup(Interrupt_Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# Callback-Funktion (Interrupt)
# In dieser Funktion wird
def Interrupt(channel):
    global Counter
    global StartZeit
    global EndZeit
    global ZwischenzeitAlt
    Zwischenzeit = time.monotonic()  # Zeit merken, wenn Interrupt ausgelöst

    print("Counter: " + str(Counter) + " - ZeitDiff: " + str(Zwischenzeit - ZwischenzeitAlt))
    if Counter == 1:
        StartZeit = Zwischenzeit
        print("Startzeit: " + str(StartZeit))
    if Counter == Ausloesungen + 1:
        EndZeit = Zwischenzeit
        print("Endzeit : " + str(EndZeit))
    Counter = Counter + 1
    ZwischenzeitAlt = Zwischenzeit


# Die Lichtschranke vom mathematischen Pendel ist immer auf High
# Bei Unterbrechunge geht sie auf Low
# Interrupt Event hinzufüben, steigende Flanke --> GPIO.RISING
# Interrupt Event hinzufüben, fallende Flanke --> GPIO.FALLING
GPIO.add_event_detect(Interrupt_Pin, GPIO.FALLING, callback=Interrupt, bouncetime=250)
Ausloesungen = (Schwingungen * 2) + 1  # ein Interrupt wird schon beim Schalten ausgelöst

# Schleife bis Counter = 10

# Dies ist quasi die Hauptprogramm Schleife
while Counter <= Ausloesungen + 1:
    GPIO.output(LED_Pin, GPIO.HIGH)
    time.sleep(0.25)
    GPIO.output(LED_Pin, GPIO.LOW)
    time.sleep(0.25)
    # print(".") # nur ein Debug Punkt ;)
    # GPIO.add_event_detect(Interrupt_Pin, GPIO.FALLING, callback = Interrupt, bouncetime = 250)

GPIO.output(LED_Pin, GPIO.LOW)  # Blink LED ausschalten

GPIO.cleanup()  # GPIO initialisierung zurücksetzten (interrupts beenden)
Zeit = EndZeit - StartZeit  # Zeitdifferenz berechnen
print("Zeitdifferenz: " + str(Zeit))  # Zeit ausgeben
print("Counter " + str(Counter))
print("Eine Schwingung: " + str(Zeit / Schwingungen))  # Zeit ausgeben
