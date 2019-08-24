from my_db.model.base import engine, Session, Base
from my_db.model.actor import Actor
from my_db.model.ContactDetails import ContactDetails
from sqlalchemy import create_engine, select, MetaData, Table


def addContactDetails():
    Base.metadata.create_all(engine)
    session = Session()

    actor = session.query(Actor).filter(Actor.name == 'Adivi Shesu').all()
    a = actor[0]
    contactDetails = ContactDetails("123 123 1234", "Hitech city,Hyderabad", a)
    session.add(contactDetails)

    session.commit()
    session.close()


if __name__ == '__main__':
    addContactDetails()