from passlib.context import CryptContext

# posswd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def generate_passwd_hash(passwd: str) -> str:
    return pwd_context.hash(passwd)


def verify_password(passwd: str, hash: str) -> bool:
    return pwd_context.verify(passwd, hash)

