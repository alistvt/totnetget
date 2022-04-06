import subprocess

proc = subprocess.run(f"cat /proc/net/dev", shell=True, capture_output=True)

data = proc.stdout

args = data.splitlines()[2:]
args = [arg.decode("utf-8") for arg in args]

recieved = [int(arg.split()[1]) for arg in args]
transfered = [int(arg.split()[9]) for arg in args]
total = recieved + transfered
print(f"recieved: {sum(recieved)}")
print(f"transfered: {sum(transfered)}")
print(f"total: {sum(total)}")

# print(args)
# text = '\n'.join(args)

# with open("x.txt", 'w') as f:
#     f.write(text)
#     print(text)
