import glob
import os
import time

from .Config import *
from .core import *

version = "v2"
group_username = "@CENSORED_POLITICSSS"
start_time = time.time()


# Sudo Users
sudos = []

# OWNER_ID ko hamesha sudos mein add karo - yahi main fix hai
if OWNER_ID and int(OWNER_ID) not in sudos:
    sudos.append(int(OWNER_ID))

if SUDO_USERS:
    try:
        sudouser = SUDO_USERS
        print(f"Sudo users from env: {sudouser}")
        for x in sudouser:
            uid = int(x)
            # Default placeholder values 123/456 skip karo
            if uid not in (123, 456) and uid not in sudos:
                sudos.append(uid)
    except Exception as e:
        print(f"Sudo parse error: {e}")

print(f"Sudo users loaded: {sudos}")
