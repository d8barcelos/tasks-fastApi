from datetime import datetime, timedelta
from typing import Dict
import jwt

JWT_SECRET = "your_secret_key"  # Em produção use variável de ambiente
JWT_ALGORITHM = "HS256"

def signJWT(user_id: int) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": (datetime.utcnow() + timedelta(hours=24)).isoformat()
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {"access_token": token}

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        expire = datetime.fromisoformat(decoded_token['expires'])
        if expire >= datetime.utcnow():
            return decoded_token
    except:
        return {}
    return {}
