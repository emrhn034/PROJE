import bcrypt

def hashle(parola: str) -> bytes:
    return bcrypt.hashpw(parola.encode(), bcrypt.gensalt())

def dogrula(parola: str, hashli: bytes) -> bool:
    return bcrypt.checkpw(parola.encode(), hashli)
