import subprocess
from datetime import datetime

from app import app
from app import jsonrpc
from models import db, User



@jsonrpc.method('test')
def test():
    return u'Welcome to Flask JSON-RPC'


@jsonrpc.method('test2')
def test():
    return u'test2 executed'

