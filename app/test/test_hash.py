# -*- coding: UTF-8 -*-
import uuid

from werkzeug.security import generate_password_hash, check_password_hash
hash = generate_password_hash('666666')

print(hash)

print(check_password_hash(hash, '666666'))
print(uuid.uuid4())