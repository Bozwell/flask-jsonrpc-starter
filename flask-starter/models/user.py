from . import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'test_user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.String(30))
    ip_address = db.Column(db.String(30))
    bytes_received = db.Column(db.Integer)
    bytes_sent = db.Column(db.Integer)
    connected_since = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    modified_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return '<username {}>'.format(self.user_id)

    def __init__(self,user_id, ip_address, bytes_received, bytes_sent, connected_since):
        self.user_id = user_id
        self.ip_address = ip_address
        self.bytes_received = bytes_received
        self.bytes_sent = bytes_sent
        self.connected_since = connected_since
        self.created_at = datetime.now()
        self.modified_at = datetime.now()