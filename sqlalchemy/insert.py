from sqlalchemy.orm import Session
from sqlalchemy import select
from main import User, engine


session = Session(engine)

# add row
# user = User( user_id = 0, firstname = 'Oleg' )
# session.add(user)

# delete row (class User, user_id=1)
# session.delete(session.get(User, 0))

session.commit()
