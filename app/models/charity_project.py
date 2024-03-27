from sqlalchemy import Column, String, Text

from app.core.db import Base, CommonColumnsMixin


class CharityProject(CommonColumnsMixin, Base):
    name = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=False)
