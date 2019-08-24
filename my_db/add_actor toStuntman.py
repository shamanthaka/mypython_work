from my_db.model.base import engine, Session, Base
from my_db.model.actor import Actor
from my_db.model.Stuntman import Stuntman

def addStuntmanToActor():
    Base.metadata.create_all(engine)
    session = Session()

    actor = session.query(Actor).filter(Actor.name == 'Adivi Shesu').first()

    stuntman = Stuntman("Bheem",True, actor)

    session.add(stuntman)
    session.commit()
    session.close()

if __name__ == '__main__':
    addStuntmanToActor()