import json
import collections


class Websocket_Data_Class:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)



class Display:
    def __init__(self):
        self.temperature=""
        self.screen="test"
        self.key1="";
        self.key2="";
        self.key3="";
        self.touchkey="";




class Slider:
    def __init__(self):
        self.content=[]




class Module_Loader(object):
    def __init__(self,name,ip,port,id,device,path,options,data_config,var_config,modul_config,sysrelevant):
        # Name des modules
        self.name = name
        # Definiert die IP Adresse
        self.ip = ip
        # Definiert den Port
        self.port = port
        # Dies definiert die Modul ID
        self.id = id
        # Geräte Adresse
        self.device=device
        # Programm Pfad
        self.path = path
        # Programm Optionen
        self.options = options
        # Datensatz Konfiguration
        self.data_config=data_config
        # SPS Variablen Konfiguration
        self.var_config = var_config
        # Interne Modul Parameter
        self.modul_config = modul_config
        # Definiere ob Modul Systemrelevantist
        self.sysrelevant=sysrelevant


class Automat_External_Controll:
    def __init__(self):
        # Deaktiviert den Automaten
        self.disable_automat=""
        # Deaktiviert das Registrieren von Usern
        self.disable_register=""
        # Gibt keine Alkoholische Getränke aus.
        self.disable_fsk=""
        # Gibt keine Alkoholfreien Getränke mehr aus
        self.disable_softdrinks=""
        # Startet den Automat neu
        self.reboot=""
        # Fährt den Automaten herunter
        self.shutdown=""
        # Externer RGB eingang für Schilder und Lampen
        self.rgb_input=""



class Automat_Temperature:
    def __init__(self):
        # Gibt Aktuelle Temperatur an
        self.temperature=0.0
        # Gibt minimale Temperatur an
        self.min_temperature=0.0
        # Gibt maximale Temperatur an
        self.max_temperature=0.0

class Automat_Cashcontroller(object):
    def __init__(self,id):
        # Gibt an, welches modul die Klasse benutzt
        self.modul_id=id
        # Zeigt an ob Gerät beschäftigt list
        self.is_ready=""
        # Gibt Betrag an gespeicherten Münzen aus
        self.change_value=0.0
        # Zeigt an ob Münzwechsler wechseln kann
        self.can_change=""
        # Maximaler Wert, den der Cashcontroller Akzeptiert
        self.max_value=0.0
        # Aktueller Kontostand
        self.cash_value=0.0
        # Resetet den Kontostand
        self.reset_cash=""
        # Gibt den Betrag an, der ausgegeben werden soll
        self.cashout_value=""
        # Startet das Ausgeben des Geldes
        self.start_cashout=""
        # Rückgabewert, ob münzen ausgegeben wurden.
        self.cashout_succes=""

class Automat_Cash_Terminal:
    def __init__(self):
        # Zeigt an ob Gerät beschäftigt list
        self.is_ready=""
        # Betrag der Auf das Konto geladen werden soll.
        self.cash_value=0.0
        # Kontonummer des users
        self.userid=""
        # IBAN des Benutzers
        self.IBAN=""
        # Starte den Bezahlvorgang
        self.start_payment=""
        # Status Bezahlvorgang
        self.payment_status=""
        # Bezahlung erfolgreich
        self.payment_success=""




class Automat_Fingerabdruck(object):
    def __init__(self,id):
        # Gibt an, welches modul die Klasse benutzt
        self.modul_id=id
        # Zeit an ob Gerät beschäftigt ist.
        self.is_ready=""
        # ID vom Gelesenen Fingerabdruck
        self.finger_id=""
        # Aktiviert das anlernen eines Fingers
        self.enroll_finger=""
        # Status des Anlernens
        self.enroll_status=""
        # Finger Hash
        self.finger_hash=""
        # Löschen eines Abdruckes
        self.delete_finger=""
        # Legt einen Abdruck mit hash an
        self.upload_hash=""
        # Status über die Aktion
        self.succes=""





class Automat_Schilder:
    def __init__(self):
    # Schilder Beleuchtung ist in RGB

        # Gibt ausgewältes Item an
        self.selected_item=""
        # Gibt ausgewältes Fach an (für automaten mit manuellen Fächern)
        self.selected_shelf=""
        # Gibt die Beleuchtung für die Items an
        self.item_lights=[]
        # Gibt die Beleuchtung für die Fächer an
        self.shelf_lights=[]
        # Ausgabe Fach Beleuchtung
        self.output_light=""
        # Automaten Beleuchtung
        self.automat_light=""




class Automat_Ausgabe(object):
    def __init__(self,id):
        # Gibt an, welches modul die Klasse benutzt
        self.modul_id=id
        # Zeigt an ob das Ausgabe Modul keine Störung hat.
        self.is_ready=""
        # Gibt das Ausgewählte Fach an.
        self.selected_shelf=""
        # Gibt an, ob Fach leer ist.
        self.empty_shelf=""
        # Ausgabe der Ware
        self.vend_request=""
        # Status ob Ware erfolgreich ausgegeben wurde 1= erfolg 2 = kein Erfolg
        self.vend_succes=""
