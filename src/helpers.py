import json
import subprocess


def write_to_file(data):
    with open(OFFSET_PATH, 'w') as f:
        f.write(json.dumps(data))


def get_net_usage(format):
    proc = subprocess.run(f"cat /proc/net/dev", shell=True, capture_output=True)

    data = proc.stdout

    args = data.splitlines()[2:]
    args = [arg.decode("utf-8") for arg in args]

    recieved = sum([int(arg.split()[1]) for arg in args])
    transferred = sum([int(arg.split()[9]) for arg in args])
    total = recieved + transferred

    if format == 'B':
        return recieved, transferred, total
    elif format == 'MB':
        return round(recieved/1e6, 3), round(transferred/1e6, 3), round(total/1e6, 3)
    elif format == 'GB':
        return round(recieved/1e9, 3), round(transferred/1e9, 3), round(total/1e9, 3)


if __name__ != "__main__":
    OFFSET_PATH = "/root/totnetget/offset.json"
    OFFSET = {
        "recieved": 0,
        "transferred": 0,
        "total": 0
    }
    try:
        with open(OFFSET_PATH, 'r') as f:
            OFFSET = json.loads(f.read())
    except FileNotFoundError:
        pass
