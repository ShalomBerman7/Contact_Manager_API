import mysql.connector

conn = mysql.connector.connect(
    host="db",
    port=3306,
    user="user",
    password="mypassword",
    database="contacts_db")

cursor = conn.cursor()


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
        return contacts

    @staticmethod
    def get_new_id():
        cursor.execute("SELECT MAX(id) FROM contacts")
        new_id = cursor.fetchall()
        return new_id

    @staticmethod
    def create_contact(first_name, last_name, phone_number):
        cursor.execute(f"INSERT INTO contacts (first_name, last_name, phone_number) \
                        VALUES('{first_name}', '{last_name}', '{phone_number}')")
        conn.commit()
        new_id = Contact.get_new_id()
        return new_id

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
            cursor.execute(f"DELETE FROM contacts WHERE id = '{id}'")
            conn.commit()
            return True
        except:
            return False

# cursor.close()
# conn.close()
