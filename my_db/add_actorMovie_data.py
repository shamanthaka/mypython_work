from datetime import date
from my_db.model.base import engine, Session, Base
from my_db.model.Movie import Movie
from my_db.model.actor import Actor


def addRecods():
    # Generate database schema
    Base.metadata.create_all(engine)

    session = Session()

    evaru = Movie("Bala", date(1978,8,19))
    #persist data
    session.add(evaru)

    adiviShesu = Actor("Suresh", date(2000,8,19))
    #persist data
    session.add(adiviShesu)

    #movies and actors relationship establishments
    evaru.actors = [adiviShesu]


    #commit and close session
    session.commit()
    session.close()

def showRecords():
    session = Session()
    movies = session.query(Movie).all()

    for m in movies:
        print(f'{m.title} released on {m.release_date}')

    actors = session.query(Actor).all()

    for a in actors:
        print(f'{a.name} born on {a.birthday}')


if __name__ == '__main__':
    addRecods()
    #showRecords()

