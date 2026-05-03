from passlib.context import CryptContext
from datetime import timedelta, datetime
import jwt, uuid, logging
from src.config import Config



ACCESS_TOKEN_EXPIRY = 36000

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def generate_passwd_hash(passwd: str) -> str:
    return pwd_context.hash(passwd)


def verify_password(passwd: str, hash: str) -> bool:
    return pwd_context.verify(passwd, hash)

def create_access_token(user_data:dict, expiry:timedelta = None, refresh:bool = False):
    payload = {}
    payload['user'] = user_data
    payload['expiry'] = (datetime.now() + (expiry if expiry is not None else timedelta(seconds=ACCESS_TOKEN_EXPIRY))).timestamp()

    payload['jti'] = str(uuid.uuid4())
    payload['refresh'] = refresh
    token = jwt.encode(
        payload=payload,
        key=Config.JWT_SECRETS,
        algorithm=Config.JWT_ALGORITHM
    )

    return token

def decode_token(token:str) -> dict:
    try:
        token_data = jwt.decode(
            jwt=token,
            key=Config.JWT_SECRETS,
            algorithms=[Config.JWT_ALGORITHM]
        )

        return token_data
    except jwt.PyJWKError as e:
        logging.exception(e)
        return None



