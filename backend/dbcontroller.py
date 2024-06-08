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
    def add_client(data: dict):
        db = Database()
        db.create_connect()
        db.send_sql_request(f"INSERT INTO zhevzh_Klient(Fam_klienta, Name_klienta, Otch_klienta, Nomer_tel) VALUES({data['Fam_klienta']}, {data['Name_klienta']}, {data['Otch_klienta']}, {data['Nomer_tel']});")
        print(f"[COMMAND] INSERT INTO zhevzh_Klient(Fam_klienta, Name_klienta, Otch_klienta, Nomer_tel) VALUES({data['Fam_klienta']}, {data['Name_klienta']}, {data['Otch_klienta']}, {data['Nomer_tel']});")
        db.close()
        return True

    @staticmethod
    def edit_client(data: dict):
        db = Database()
        db.create_connect()
        db.send_sql_request(f"UPDATE zhevzh_Klient SET Fam_klienta = '{data['Fam_klienta']}', Name_klienta = '{data['Name_klienta']}', Otch_klienta = '{data['Otch_klienta']}', Nomer_tel = '{data['Nomer_tel']}' WHERE Kod_klienta = {data['Kod_klienta']};")
        print(f"[COMMAND] UPDATE zhevzh_Klient SET Fam_klienta = '{data['Fam_klienta']}', Name_klienta = '{data['Name_klienta']}', Otch_klienta = '{data['Otch_klienta']}', Nomer_tel = '{data['Nomer_tel']}' WHERE Kod_klienta = {data['Kod_klienta']};")
        db.close()
        return True

    @staticmethod
    def delete_client(data: dict):
        db = Database()
        db.create_connect()
        db.send_sql_request(f"DELETE FROM zhevzh_Klient WHERE Kod_klienta = {data['Kod_klienta']}")
        print(f"[COMMAND] DELETE FROM zhevzh_Klient WHERE Kod_klienta = {data['Kod_klienta']}")
        db.close()
        return True

    @staticmethod
    def get_client_list():
        db = Database()
        db.create_connect()
        data = db.send_sql_request(f"SELECT * FROM ZHEVZH_KLIENT;")
        print(f"[COMMAND] SELECT * FROM ZHEVZH_KLIENT;")
        db.close()
        return data

    @staticmethod
    def get_employee_list():
        db = Database()
        db.create_connect()
        data = db.send_sql_request("SELECT * FROM ZHEVZH_SOTR;")
        print(f"[COMMAND] SELECT * FROM ZHEVZH_SOTR;")
        db.close()
        return data

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
        # ДОПИСАТЬ функцию
        db = Database()
        db.create_connect()
        data = db.send_sql_request("SELECT FROM ZHEVZH_TOVAR")
        print(f"[COMMAND] SELECT * FROM ZHEVZH_TOVAR")
        db.close()
        return data

    @staticmethod
    def add_order(data: dict):
        # ПРОТЕСТИРОВАТЬ функцию
        db = Database()
        db.create_connect()
        db.send_sql_request(f"INSERT INTO zhevzh_Zakaz(Kod_klienta, Kod_sotr, Stoimost_zakaza, Data_zakaza, Data_vypolnenya) VALUES({data['Kod_klienta']}, {data['Kod_sotr']}, {data['Stoimost_zakaza']}, '{data['Data_zakaza']}', '{data['Data_vypolnenya']}');")
        print(f"[COMMAND] INSERT INTO zhevzh_Zakaz(Kod_klienta, Kod_sotr, Stoimost_zakaza, Data_zakaza, Data_vypolnenya) VALUES({data['Kod_klienta']}, {data['Kod_sotr']}, {data['Stoimost_zakaza']}, '{data['Data_zakaza']}', '{data['Data_vypolnenya']}');")
        db.close()
        return True

    @staticmethod
    def edit_order(data: dict):
        # ПРОТЕСТИРОВАТЬ функцию
        db = Database()
        db.create_connect()
        db.send_sql_request(f"UPDATE zhevzh_Zakaz SET Fam_klienta = '{data['Fam_klienta']}', Name_klienta = '{data['Name_klienta']}', Otch_klienta = '{data['Otch_klienta']}', Nomer_tel = '{data['Nomer_tel']}' WHERE Kod_klienta = {data['Kod_klienta']};")
        print(f"[COMMAND] ")
        db.close()
        return True

    @staticmethod
    def delete_order(data: dict):
        # ПРОТЕСТИРОВАТЬ функцию
        db = Database()
        db.create_connect()
        db.send_sql_request(f"DELETE FROM zhevzh_Zakaz WHERE Kod_zakaza = {data['Kod_zakaza']}")
        print(f"[COMMAND] DELETE FROM zhevzh_Zakaz WHERE Kod_zakaza = {data['Kod_zakaza']}")
        db.close()
        return True


if __name__ == '__main__':
    # print(Database.get_client_list())
    # print(Database.get_employee_list())
    # print(Database.get_product_list())
    # Database.add_client({
    #     'Fam_klienta': '1',
    #     'Name_klienta': '2',
    #     'Otch_klienta': '3',
    #     'Nomer_tel': '4'
    # })
    # Database.delete_client({
    #     'Kod_klienta': 4,
    #     'Fam_klienta': '1',
    #     'Name_klienta': '2',
    #     'Otch_klienta': '3',
    #     'Nomer_tel': '4'
    # })
    # Database.edit_client({
    #     'Kod_klienta': 5,
    #     'Fam_klienta': '12',
    #     'Name_klienta': '23',
    #     'Otch_klienta': '34',
    #     'Nomer_tel': '45'
    # })
    pass