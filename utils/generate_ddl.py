from sqlalchemy.schema import CreateTable

from ..models.entity import User

print(CreateTable(User.__table__))
