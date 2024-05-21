from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from datetime import datetime


class Base(DeclarativeBase):
    """
    Anything that subclasses this Base class will be established as a new ORM mapped class which refers to a Table object
    """
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    password: Mapped[str]
    dob: Mapped[datetime]
    weight: Mapped[float]
    gender: Mapped[str]
    goal: Mapped[str]
    training_style: Mapped[str]

    def __repr__(self):
        return (f"<Hero(id={self.id}, email={self.email}, password={self.password}, dob={self.dob}, weight={self.weight},"
                f"gender={self.gender}, goal={self.goal}, training_style={self.training_style})>")


# if __name__ == "__main__":
#     Base.metadata.create_all(engine)

    # session.add(Hero(name="Super Man", secret_name="Clark Kent", age=40, password="Louis Lane"))
    # session.commit()

    # print(session.query(Hero).all())

    # obj = session.query(Hero).get(1)
    # obj.secret_name = "Bruce Wayne"
    # session.commit()
    # print(session.query(Hero).all())

    # hero = Hero(name="Super Man", secret_name="Clark Kent", age=40)
    # add_hero(hero)
    # delete_hero(2)
