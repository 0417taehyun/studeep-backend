from typing import Any
from datetime import datetime
from sqlalchemy import Column, DateTime, func
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative
class Base:
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'
    
    id: Any
    created_at: datetime = Column(DateTime(timezone=True), default=func.now())
    updated_at: datetime
    deleted_at: datetime
    
    