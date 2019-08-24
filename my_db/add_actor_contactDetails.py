from my_db.model.base import engine, Session, Base
from my_db.model.actor import Actor
from my_db.model.ContactDetails import ContactDetails
from sqlalchemy import create_engine, select, MetaData, Table


def addContactDetails():
    Base.metadata.create_all(engine)
    session = Session()
    # SELECT * FROM my_movie_db.actors where name = 'Adivi Shesu';
    # customerData = session.query(Customer).filter(Customer.name==customerName)
    # movies = session.query(Movie).all()
    # actor = session.query(actorObj).filter(actorObj.name == 'Adivi Shesu')
    actorId = 0
    # User.query.filter(User.email.endswith('@example.com')).all()
    # actor = Actor.query.filter(Actor.name=='Adivi Shesu').all()
    """with engine.connect() as con:
        rs = con.execute('SELECT * FROM my_movie_db.actors where name = ' +'Adivi Shesu')"""

    metadata = MetaData(bind=None)
    table = Table('actors', metadata, autoload=True, autoload_with=engine)
    stmt = select([table]).where(table.columns.name == 'Adivi Shesu')

    connection = engine.connect()
    results = connection.execute(stmt).fetchall()

    print(str(results[0][1], 'utf-8'))
    print(results[0][2])

    actor = Actor(str(results[0][1], 'utf-8'), results[0][2])
    actor.id = results[0][0]

    contactDetails = ContactDetails("123 123 1234", "Hitech city,Hyderabad", actor)
    session.add(contactDetails)

    session.commit()
    session.close()


if __name__ == '__main__':
    addContactDetails()