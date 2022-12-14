import os.path

from typing import List, Optional


API_ID: int = 4954361
API_HASH: str = "43a786a8548a30f9d6887e36d53c0e64"
TOKEN: str = "5817665802:AAFilzok4BddygT4u3Uynr-ohzCtGYtOcW0"

log_chat: int = -1001532430686
sudoers: List[int] = [737737727]
super_sudoers: List[int] = [737737727]

prefix: List[str] = ["/", "!", ".", "$", "-"]

disabled_plugins: List[str] = []

WORKERS = 24

DATABASE_PATH = os.path.join("eduu", "database", "eduu.db")

TENOR_API_KEY: Optional[str] = "X9HD35B7ZGP6"

sudoers.extend(super_sudoers)
