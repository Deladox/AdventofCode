import sys
sys.path.append('/home/kalle/Python/ssh/')
sys.path.append('/home/kalle/Python/ssh/ssh_so')
sys.path.append('/home/kalle/Python/ssh/ssh_so/helper')
from ssh_so_lib import SshNbUtils

def testshowinventory():
    ss_admin = SshNbUtils(ip="10.10.20.12", user="admin", pw="admin")
    result = ss_admin.cmd(cmd_list=["show status/n"])
    print("hello world")
    print(result)
    assert True