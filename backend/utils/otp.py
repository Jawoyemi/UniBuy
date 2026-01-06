import random
import string
from datetime import datetime, timedelta, timezone

def generate_otp(length: int = 6) -> str:
    return "".join(random.choices(string.digits, k=length))

def get_otp_expiration(minutes: int = 5) -> datetime:
    return (datetime.now(timezone.utc) + timedelta(minutes=minutes)).replace(tzinfo=None)
