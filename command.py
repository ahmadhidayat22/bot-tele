import subprocess



def ping():
    s1 =subprocess.run("ping 34.101.144.49", shell=True, capture_output=True)
    # print(s1)
    # print(s1.stdout.decode())
    return s1.stdout.decode()

t = ping()
print(t)