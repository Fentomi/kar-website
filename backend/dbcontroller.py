import sqlite3


class Database():
    def create_connect(self):
        try:
            self.database = sqlite3.connect('./data/database.db')
            self.cursor = self.database.cursor()
            self.kod_zakaza_statusa = 1000
            self.kod_zakaza = 1000
        except:
            print('[DATABASE] Connection lost!')

    def send_sql_request(self, sql_request: str):
        res = self.cursor.execute(sql_request)
        self.database.commit()
        return res.fetchall()

    def close(self):
        self.database.close()

    @staticmethod
    def add_client(data: dict):
        print(data)
        db = Database()
        db.create_connect()
        db.send_sql_request(f"INSERT INTO zhevzh_Klient(Fam_klienta, Name_klienta, Otch_klienta, Nomer_tel) VALUES('{data['Fam_klienta']}', '{data['Name_klienta']}', '{data['Otch_klienta']}', '{data['Nomer_tel']}');")
        print(f"[COMMAND] INSERT INTO zhevzh_Klient(Fam_klienta, Name_klienta, Otch_klienta, Nomer_tel) VALUES({data['Fam_klienta']}, {data['Name_klienta']}, {data['Otch_klienta']}, {data['Nomer_tel']});")
        db.close()
        return 'ok'

    @staticmethod
    def edit_client(data: dict):
        db = Database()
        db.create_connect()
        db.send_sql_request(f"UPDATE zhevzh_Klient SET Fam_klienta = '{data['Fam_klienta']}', Name_klienta = '{data['Name_klienta']}', Otch_klienta = '{data['Otch_klienta']}', Nomer_tel = '{data['Nomer_tel']}' WHERE Kod_klienta = {data['Kod_klienta']};")
        print(f"[COMMAND] UPDATE zhevzh_Klient SET Fam_klienta = '{data['Fam_klienta']}', Name_klienta = '{data['Name_klienta']}', Otch_klienta = '{data['Otch_klienta']}', Nomer_tel = '{data['Nomer_tel']}' WHERE Kod_klienta = {data['Kod_klienta']};")
        db.close()
        return 'ok'

    @staticmethod
    def delete_client(data: dict):
        db = Database()
        db.create_connect()
        db.send_sql_request(f"DELETE FROM zhevzh_Klient WHERE Kod_klienta = {data['Kod_klienta']}")
        print(f"[COMMAND] DELETE FROM zhevzh_Klient WHERE Kod_klienta = {data['Kod_klienta']}")
        db.close()
        return 'ok'

    @staticmethod
    def get_client_list():
        db = Database()
        db.create_connect()
        data = db.send_sql_request(f"SELECT * FROM ZHEVZH_KLIENT;")
        print(f"[COMMAND] SELECT * FROM ZHEVZH_KLIENT;")
        db.close()
        result_data = []
        for item in data:
            result_data.append({
                'Kod_klienta': item[0],
                'Fam_klienta': item[1],
                'Name_klienta': item[2],
                'Otch_klienta': item[3],
                'Nomer_tel': item[4]
            })
        return result_data

    @staticmethod
    def get_employee_list():
        db = Database()
        db.create_connect()
        data = db.send_sql_request("SELECT * FROM ZHEVZH_SOTR;")
        result_data = []
        for item in data:
            result_data.append({
                'Kod_sotr': item[0],
                'Fam_sotr': item[1],
                'Name_sotr': item[2],
                'Otch_sotr': item[3],
                'Pochta_sotr': item[4],
                'Kod_dolg': item[5],
                'Data_priema': item[6],
            })
        print(f"[COMMAND] SELECT * FROM ZHEVZH_SOTR;")
        db.close()
        return result_data

    @staticmethod
    def get_product_list():
        db = Database()
        db.create_connect()
        data = db.send_sql_request("SELECT * FROM ZHEVZH_TOVAR")
        print(f"[COMMAND] SELECT * FROM ZHEVZH_TOVAR")
        db.close()
        return data

    @staticmethod
    def get_order_list():
        db = Database()
        db.create_connect()
        data = db.send_sql_request("""SELECT zhevzh_Zakaz.Kod_zakaza,
                                      zhevzh_Klient.Fam_klienta || ' ' || zhevzh_Klient.Name_klienta || ' ' || zhevzh_Klient.Otch_klienta AS ФИО_заказчика,
                                      zhevzh_Zakaz.Data_zakaza,
                                      zhevzh_Status_Zakaza.Naimenovanye_stat
                                      FROM zhevzh_Zakaz 
                                      JOIN zhevzh_Klient ON zhevzh_Zakaz.Kod_klienta = zhevzh_Klient.Kod_klienta
                                      JOIN zhevzh_Zakaz_Status ON zhevzh_Zakaz.Kod_zakaza = zhevzh_Zakaz_Status.Kod_zakaza
                                      JOIN zhevzh_Status_Zakaza ON zhevzh_Zakaz_Status.Kod_statusa = zhevzh_Status_Zakaza.Kod_statusa;""")
        print("""SELECT zhevzh_Zakaz.Kod_zakaza,
                                      zhevzh_Klient.Fam_klienta || ' ' || zhevzh_Klient.Name_klienta || ' ' || zhevzh_Klient.Otch_klienta AS ФИО_заказчика,
                                      zhevzh_Zakaz.Data_zakaza,
                                      zhevzh_Status_Zakaza.Naimenovanye_stat
                                      FROM zhevzh_Zakaz 
                                      JOIN zhevzh_Klient ON zhevzh_Zakaz.Kod_klienta = zhevzh_Klient.Kod_klienta
                                      JOIN zhevzh_Zakaz_Status ON zhevzh_Zakaz.Kod_zakaza = zhevzh_Zakaz_Status.Kod_zakaza
                                      JOIN zhevzh_Status_Zakaza ON zhevzh_Zakaz_Status.Kod_statusa = zhevzh_Status_Zakaza.Kod_statusa;""")
        db.close()
        result_data = []
        for item in data:
            result_data.append({
                'Kod_zakaza': item[0],
                'FIO_zakaza': item[1],
                'Data_zakaza': item[2],
                'Naimenovanye_stat': item[3]
            })
        return result_data

    @staticmethod
    def add_order(data: dict):
        db = Database()
        db.create_connect()
        db.send_sql_request(f"INSERT INTO zhevzh_Zakaz (Kod_zakaza, Kod_klienta, Kod_sotr, Stoimost_zakaza, Data_zakaza) VALUES ({data['Kod_zakaza']}, {data['Kod_klienta']}, {data['Kod_sotr']}, '{data['Stoimost_zakaza']}', '{data['Data_zakaza']}');")
        print(f"[COMMAND] INSERT INTO zhevzh_Zakaz (Kod_klienta, Kod_sotr, Stoimost_zakaza, Data_zakaza) VALUES ({data['Kod_klienta']}, {data['Kod_sotr']}, '{data['Stoimost_zakaza']}', '{data['Data_zakaza']}');")
        db.send_sql_request(f"INSERT INTO zhevzh_Zakaz_Status(Kod_zakaza_statusa, Kod_sotr, Kod_zakaza, Kod_statusa, Data_statusa) VALUES({data['Kod_zakaza_statusa']}, {data['Kod_sotr']}, {data['Kod_zakaza']}, (SELECT Kod_statusa FROM zhevzh_Status_Zakaza WHERE Naimenovanye_stat = 'Оформлен'), '{data['Data_zakaza']}');")
        print(f"INSERT INTO zhevzh_Zakaz_Status(Kod_zakaza_statusa, Kod_sotr, Kod_zakaza, Kod_statusa, Data_statusa) VALUES({data['Kod_zakaza_statusa']}, {data['Kod_sotr']}, {data['Kod_zakaza']}, (SELECT Kod_statusa FROM zhevzh_Status_Zakaza WHERE Naimenovanye_stat = 'Оформлен'), '{data['Data_zakaza']}');")
        db.close()
        return 'ok'

    @staticmethod
    def edit_order(data: dict):
        db = Database()
        db.create_connect()
        db.send_sql_request(f"""UPDATE zhevzh_Zakaz_Status
                                SET Kod_statusa = (SELECT Kod_statusa FROM zhevzh_Status_Zakaza WHERE Naimenovanye_stat = '{data['Naimenovanye_stat']}'),
                                    Data_statusa = CURRENT_TIMESTAMP
                                WHERE Kod_zakaza = {data['Kod_zakaza']};""")
        print(f"""[COMMAND] UPDATE zhevzh_Zakaz_Status
                                SET Kod_statusa = (SELECT Kod_statusa FROM zhevzh_Status_Zakaza WHERE Naimenovanye_stat = '{data['Naimenovanye_stat']}'),
                                    Data_statusa = CURRENT_TIMESTAMP
                                WHERE Kod_zakaza = {data['Kod_zakaza']};""")
        db.close()
        return 'ok'

    @staticmethod
    def delete_order(data: dict):
        db = Database()
        db.create_connect()
        db.send_sql_request(f"DELETE FROM zhevzh_Zakaz WHERE Kod_zakaza = {data['Kod_zakaza']}")
        print(f"[COMMAND] DELETE FROM zhevzh_Zakaz WHERE Kod_zakaza = {data['Kod_zakaza']}")
        db.close()
        return 'ok'


if __name__ == '__main__':
    # Database.add_order({
    #     'Kod_zakaza': 900,
    #     'Kod_zakaza_statusa': 900,
    #     'Kod_klienta': 1,
    #     'Kod_sotr': 2,
    #     'Stoimost_zakaza': 0,
    #     'Data_zakaza': '2023-07-01',
    # })
    pass