import subprocess
import sys

command = ["ls"] + sys.argv[1:]
ls = subprocess.run(command, capture_output=True, text=True)
output = ls.stdout.replace("liran", "***")
print(output)


import subprocess
import time

# # f = open("countries.txt")
# # process = subprocess.Popen("ls", stdout=f)
# # process = subprocess.Popen("ls", stderr=f)
# # process = subprocess.Popen("ls", stdin=f)
# process = subprocess.Popen("ls", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # f.close()
# print(process)

# for i in range(3):
#     print(i)
#     time.sleep(1)

# out, err = process.communicate()
# print(out)

# # process.kill()
# # process.terminate()
# process.wait()
# print("FINISHED")


# ls = subprocess.Popen("ls", stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# grep = subprocess.Popen(["grep", "txt"], stdin=ls.stdout, stdout=subprocess.PIPE, text=True)

# out, err = grep.communicate()
# print(out)







ls = subprocess.Popen("ls", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = ls.communicate()

ls = subprocess.run("ls", capture_output=True, text=True, timeout=10)
print(ls.stdout)
print(ls.stderr)

# command = "ls -la"
command = "ls -la".split()
# command = ["ls", "-la"]
ls = subprocess.run(command, capture_output=True, text=True, timeout=10)
print(ls.stdout)

python3 a.py
python3 a.py -la
python3 a.py -l
python3 a.py -a
python3 a.py -R -l



s = "wow.txt"
s = s.replace("txt", "***")
