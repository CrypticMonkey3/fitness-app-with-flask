from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from typing import Optional


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
    dob: Mapped[Optional[str]]
    weight: Mapped[Optional[float]]
    gender: Mapped[Optional[str]]
    goal: Mapped[Optional[str]]
    training_style: Mapped[Optional[str]]

    def __repr__(self):
        return (f"<User(id={self.id}, email={self.email}, password={self.password}, dob={self.dob}, weight={self.weight},"
                f"gender={self.gender}, goal={self.goal}, training_style={self.training_style})>")
