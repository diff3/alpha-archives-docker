import MySQLdb

def insert_user():
    try:
        connection = MySQLdb.connect(
            host="db",  
            user="root", 
            passwd="pwd", 
            db="alpha_archives" 
        )
        cursor = connection.cursor()

        insert_query = """
        INSERT INTO `user_customuser` (`id`, `password`, `last_login`, `is_superuser`, `first_name`, `last_name`, `is_staff`, `is_active`, `date_joined`, `username`, `birthdate`, `street_number`, `street_type`, `street_name`, `city_zipcode`, `city`, `address_complement`, `country`, `email`, `email_validated`, `phone_number`, `phone_validated`)
        VALUES
        (1, 'pbkdf2_sha256$390000$ww7DXzNup4BhUhycRv40nv$rsJCWwwyiJLTkG1HzRbbBSn0g6MnKVOxvi5ayf9mShU=', NULL, 1, '', '', 1, 1, '2024-05-22 06:35:06.011881', 'admin', NULL, '', '', '', '', '', '', 'Earth', 'none@nothere.com', 1, '', 0);
        """
        cursor.execute(insert_query)
        connection.commit()

        print("User inserted successfully.")

    except MySQLdb.Error as e:
        print(f"Error inserting user: {e}")
        connection.rollback()

    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    insert_user()