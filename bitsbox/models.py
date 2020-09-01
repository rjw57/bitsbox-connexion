import uuid

from sqlalchemy.dialects.postgresql import UUID

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))


class Bit(db.Model):
    id = db.Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False, default=str)
