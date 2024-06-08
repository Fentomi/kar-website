import sqlite3


class Database():
    def create_connect(self):
        try:
            self.database = sqlite3.connect('./data/database.db')
            self.cursor = self.database.cursor()
        except:
            print('[DATABASE] Connection lost!')

    def send_sql_request(self, sql_request: str):
        res = self.cursor.execute(sql_request)
        self.database.commit()
        return res.fetchall()

    def close(self):
        self.database.close()

    @staticmethod
    def add_equipment(data: dict):
        db = Database()
        db.create_connect()
        db.send_sql_request(f"INSERT INTO sos_oborudovanie(kod_oborud, invent_nomer, sostoyanie, kod_tipa_ucheta) VALUES({data['kod_oborud']}, {data['invent_nomer']}, '{data['sostoyanie']}', {data['kod_tipa_ucheta']});")
        print(f"[COMMAND] INSERT INTO sos_oborudovanie(kod_oborud, invent_nomer, sostoyanie, kod_tipa_ucheta) VALUES({data['kod_oborud']}, {data['invent_nomer']}, '{data['sostoyanie']}', {data['kod_tipa_ucheta']});")
        db.close()

    @staticmethod
    def delete_equipment(data: dict):
        db = Database()
        db.create_connect()
        print(data)
        db.send_sql_request(f"DELETE FROM sos_oborudovanie WHERE kod_oborud = {data['kod_oborud']};")
        print(f"[COMMAND] DELETE FROM sos_oborudovanie WHERE kod_oborud = {data['kod_oborud']};")
        db.close()

    @staticmethod
    def edit_equipment(data: dict):
        db = Database()
        db.create_connect()
        db.send_sql_request(f"UPDATE sos_oborudovanie SET sostoyanie = '{data['sostoyanie']}', invent_nomer = {data['invent_nomer']} WHERE kod_oborud = {data['kod_oborud']};")
        print(f"[COMMAND] UPDATE sos_oborudovanie SET sostoyanie = '{data['sostoyanie']}', invent_nomer = {data['invent_nomer']} WHERE kod_oborud = {data['kod_oborud']};")
        db.close()

    @staticmethod
    def get_equipment_list():
        db = Database()
        db.create_connect()
        data = db.send_sql_request(f"SELECT * FROM sos_oborudovanie")
        print(f"[COMMAND] SELECT * FROM sos_oborudovanie")
        db.close()
        json_data = []
        for item in data:
            json_data.append({
                'kod_oborud': item[0],
                'invent_nomer': item[1],
                'sostoyanie': item[2],
                'kod_tipa_ucheta': item[3]
            })
        return json_data

    @staticmethod
    def add_mol(data: dict):
        db = Database()
        db.create_connect()
        db.send_sql_request(f"INSERT INTO sos_MOL(kod_MOL, nach_otvetst, kod_sotr) VALUES({data['kod_MOL']}, '{data['nach_otvetst']}', {data['kod_sotr']});")
        print(f"[COMMAND] INSERT INTO sos_MOL(kod_MOL, nach_otvetst, kod_sotr) VALUES({data['kod_MOL']}, '{data['nach_otvetst']}', {data['kod_sotr']});")
        db.close()

    @staticmethod
    def edit_mol(data: dict):
        db = Database()
        db.create_connect()
        db.send_sql_request(f"UPDATE sos_MOL SET kod_sotr = '{data['kod_sotr']}', nach_otvetst = '{data['nach_otvetst']}' WHERE kod_MOL = {data['kod_MOL']};")
        print(f"[COMMAND] UPDATE sos_MOL SET kod_sotr = '{data['kod_sotr']}', nach_otvetst = '{data['nach_otvetst']}' WHERE kod_MOL = {data['kod_MOL']};")
        db.close()

    @staticmethod
    def delete_mol(data: dict):
        db = Database()
        db.create_connect()
        db.send_sql_request(f"DELETE FROM sos_MOL WHERE kod_MOL = {data['kod_MOL']};")
        print(f"[COMMAND] DELETE FROM sos_MOL WHERE kod_MOL = {data['kod_MOL']};")
        db.close()

    @staticmethod
    def get_mol_list():
        db = Database()
        db.create_connect()
        data = db.send_sql_request(f"SELECT kod_MOL, nach_otvetst, kod_sotr FROM sos_MOL;")
        print(f"[COMMAND] SELECT kod_MOL, nach_otvetst, kod_sotr FROM sos_MOL;")
        db.close()
        json_data = []
        for item in data:
            json_data.append({
                'kod_MOL': item[0],
                'nach_otvetst': item[1],
                'kod_sotr': item[2]
            })
        return json_data