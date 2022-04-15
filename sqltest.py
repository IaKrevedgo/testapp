import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class sql():
    def dbcreate():
        try:
            # Подключение к существующей базе данных
            connection = psycopg2.connect(user="postgres",
                                        # пароль, который указали при установке PostgreSQL
                                        password="1",
                                        host="127.0.0.1",
                                        port="5432")
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            # Курсор для выполнения операций с базой данных
            cursor = connection.cursor()
            sql_create_database = 'create database postgres_dbtest'
            cursor.execute(sql_create_database)
        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")
    def dbconnect():
        import psycopg2
    from psycopg2 import Error

    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                    
                                    password="1",                                               # пароль, который указали при установке PostgreSQL
                                    host="127.0.0.1",
                                    port="5432",
                                    database="test")

        
        cursor = connection.cursor()                                                            # Курсор для выполнения операций с базой данных
        
        print("Информация о сервере PostgreSQL")                                                # Распечатать сведения о PostgreSQL
        print(connection.get_dsn_parameters(), "\n")
        # Выполнение SQL-запроса
        cursor.execute("SELECT version();")
        # Получить результат
        record = cursor.fetchone()
        print("Вы подключены к - ", record, "\n")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
            
            
    def dbtablecreate(self, ctxt=''):
        import psycopg2
        from psycopg2 import Error

        try:
            # Подключиться к существующей базе данных
            connection = psycopg2.connect(user="postgres",
                                        # пароль, который указали при установке PostgreSQL
                                        password="1",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="postgres_db")

            # Создайте курсор для выполнения операций с базой данных
            cursor = connection.cursor()
            # SQL-запрос для создания новой таблицы
            create_table_query = ctxt 
            # Выполнение команды: это создает новую таблицу
            cursor.execute(create_table_query)
            connection.commit()
            print("Таблица успешно создана в PostgreSQL")

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("Соединение с PostgreSQL закрыто")    
                

                            
                            
    def dbreadtable():
        import psycopg2

        con = psycopg2.connect(
                                database="test", 
                                user="postgres", 
                                password="1", 
                                host="127.0.0.1", 
                                port="5432"
                                ) 
        
        print("Database opened successfully")
        cur = con.cursor()  
        cur.execute('''SELECT id, "fistName", "lastName", "midName", "birthDate", "companyName", work, "workAt", certificate, email1,
                    email2, tel1, tel2, citizenship, "adrCountry", "adrCity", "adrStreet", "adrHNum", "adrRNum", "addData1", "addData2",
                    "addData3", pas1, pas2, pas3, "pasLastDate", access, pay FROM public.users order by id''')
        
        rows = cur.fetchall()
        for row in rows:  
            print("ID =", row[0])
            print("Имя =", row[1])
            print("Фамилия =", row[2])
            print("Отчество =", row[3])
            print("Дата рождения =", row[4])
            print('\n')

        print("Operation done successfully")  
        con.close()   
        
ctxt =  '''CREATE TABLE mobile
                                (ID INT PRIMARY KEY     NOT NULL,
                                MODEL           TEXT    NOT NULL,
                                PRICE         REAL); '''                        
sql.dbconnect()
sql.dbreadtable()