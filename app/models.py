from .database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Note(Base):
    __tablename__ = 'notes'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False, unique=True)
    content = Column(String, nullable=False)
    category = Column(String, nullable=True)
    published = Column(Boolean, nullable=False, server_default='true')  # lowercase 'true' for PostgreSQL
    createdAt = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(TIMESTAMP(timezone=True), default=None, onupdate=func.now())

