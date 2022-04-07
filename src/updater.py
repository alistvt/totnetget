"""
Idle loop to save the real network usage
"""
from time import sleep
from helpers import get_net_usage, write_to_file, OFFSET

while True:
    try:
        rc, tr, ttl = get_net_usage("GB")
        data = {
            "recieved": rc + OFFSET["recieved"],
            "transferred": tr + OFFSET["transferred"],
            "total": ttl + OFFSET["total"]
        }
        write_to_file(data)
        sleep(10)
    except:
        pass

