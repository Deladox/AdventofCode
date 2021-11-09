import re
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


def test_3():
    ssh_nb = SshNbUtils(ip="10.10.50.133", user="smartroot", pw="314740193099")
    result = ssh_nb.cmd(slot2=True, sudo=True, cmd_list=["tiny_dh_client -d /tmp/device_handlers/qsfp/0 -c get -a data/fec/berCounters"])[0]
    result = re.findall(pattern=r'/d[.]/d+', string=result) #, re.findall(pattern=r'/d[.]/d/d/d/d'string=result)
    print(result)


def torr_sim_test_1():
    result = ["tiny_dh_client -d /tmp/device_handlers/qsfp/0 -c get -a data/fec/berCounters"]
    result = re.findall(pattern=r'/d[.]/d+', string=result)
    print(result)