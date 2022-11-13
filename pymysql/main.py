import pymysql.cursors

# create connection to database
connection = pymysql.connect(
    host='localhost',
    user='test',
    password='password',
    database='testdb',
    cursorclass=pymysql.cursors.DictCursor
    )




# create cursor
cursor = connection.cursor()

# delete table if exist
cursor.execute( "DROP TABLE IF EXISTS user;")

# create table
cursor.execute( " CREATE TABLE user( "
                " user_id int auto_increment primary key,"
                " firstname varchar(100),"
                " lastname varchar(100)"
                ");")

# insert data
cursor.execute( " INSERT INTO user (firstname, lastname) VALUES ('fname', 'lname');" )
connection.commit()

# read data
cursor.execute(" SELECT firstname, lastname FROM user WHERE user_id=1") 
print(cursor.fetchone())



# def init_db():
#     db = connection.cursor()

#     # drop tables
#     db.execute("DROP TABLE IF EXISTS user;")
#     db.execute("DROP TABLE IF EXISTS post;")

#     # create table user
#     db.execute( ' CREATE TABLE user( '
#                 ' id INTEGER PRIMARY KEY AUTO_INCREMENT,'
#                 ' username varchar(10) UNIQUE NOT NULL,'
#                 ' password varchar(10) NOT NULL'
#                 ');' )

#     # create table post
#     db.execute( ' CREATE TABLE post( '
#                 'id INTEGER PRIMARY KEY AUTO_INCREMENT,'
#                 'author_id INTEGER NOT NULL,'
#                 'created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,'
#                 'title varchar(20) NOT NULL,'
#                 'body varchar(500) NOT NULL,'
#                 'FOREIGN KEY (author_id) REFERENCES user (id)'
#                 ');' )

# init_db()

