
import sys
sys.path.append('/home/kalle/Python/ssh/')
sys.path.append('/home/kalle/Python/ssh/ssh_so')
sys.path.append('/home/kalle/Python/ssh/ssh_so/helper')
from ssh_karl_helper import SshNbUtils

def test_1():
    ssh_nb = SshNbUtils(ip="10.10.20.12", user="admin", pw="admin")
    result_list = ssh_nb.cmd(cmd_list=["show status\n", "show uptime\n"])
    print(result_list[0])
    print(result_list[1])


def test_2(ssh_admin):
    result_list = ssh_admin.cmd(cmd_list=["show status\n", "show uptime\n"])
    print(result_list[0])
    print(result_list[1])


def test_3(ssh_root):
    result = ssh_root.cmd(cmd_list=["cat /var/log/error.log\n"])[0]
    print(result)