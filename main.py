import base
import sqlalchemy

User_table =  base.User()
User_table.name = "Пользователь 1"
User_table.about = "биография пользователя 1"
User_table.email = "email@email.ru"
db_sess = .create_session()
db_sess.add(User_table)
db_sess.commit()