from mmap import error

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="user",
    # password= "0000",
    database="DB")

cursor = conn.cursor()
cursor.execute("SELECT * FROM contacts")
rows = cursor.fetchall()

for row in rows:  # בדיקה
    print(row)


class Contact:

    @staticmethod
    def sql_to_dict(rows):
        dict_item = {}
        list_of_dict = []
        for row in rows:
            dict_item['id'] = row[0]
            dict_item['first_name'] = row[1]
            dict_item['last_name'] = row[2]
            dict_item['phone_number'] = row[3]
            list_of_dict.append(dict_item)
        return list_of_dict

    @staticmethod
    def get_all_contacts():
        cursor.execute("SELECT * FROM contacts")
        contacts = cursor.fetchall()
        conn.commit()
        return contacts

    @staticmethod
    def create_contact(first_name, last_name, phone_number):
        cursor.execute(f"INSERT INTO contacts (first_name, last_name, phone_number) \
                         VALUES('{first_name}', '{last_name}', '{phone_number}')")
        conn.commit()
        return cursor.execute("SELECT MAX(id) FROM contacts")

    @staticmethod
    def update_contact(id, first_name, last_name, phone_number):
        try:
            cursor.execute(f"UPDATE contacts \
                           SET first_name = '{first_name}', last_name = '{last_name}', phone_number = '{phone_number}' \
                           WHERE id = '{id}'")
            return True
        except:
            return False

    @staticmethod
    def delete_contact(id):
        try:
            cursor.execute(f"DELETE * FROM contacts WHERE id = '{id}'")
            conn.commit()
            return True
        except:
            return False


cursor.close()
conn.close()
