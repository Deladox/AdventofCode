import re
import sys
import time
from matplotlib import pyplot as plt
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


def test_4torrsim():
        x=str(-163)
        ssh_nbDCPM = SshNbUtils(ip="10.10.50.174", user="smartroot", pw="314740193099")
        result = ssh_nbDCPM.cmd(sudo=True, cmd_list=["tiny_dh_client -d /tmp/device_handlers/tdcm -a config/dispersion -c set -v " +x+ " -t float \n"])
        result = str(result)
        print(result)

        #break_list = "\r\n\r\nThis command can be service interrupting.\r\nAre you sure you want to continue? (Yes/NO):"
        #ssh_nbDCPM = SshNbUtils(ip="10.10.50.174", user="admin", pw="admin")
        #dcpresult = ssh_nbDCPM.cmd(break_list = break_list, cmd_list=["config interface if-1/line tdcm manual 100 \n"])
        #print(dcpresult)


def test_3():

    ssh_nbDCPM = SshNbUtils(ip="10.10.50.174", user="smartroot", pw="314740193099")
    dcpresult = ssh_nbDCPM.cmd(sudo=True, cmd_list=["tiny_dh_client -d /tmp/device_handlers/tdcm -a config/dispersion -c set -v -173 -t float \n"])
    ssh_nb = SshNbUtils(ip="10.10.50.133", user="smartroot", pw="314740193099") 
    ssh_nb.cmd(slot2=True, sudo=True, cmd_list=["tiny_dh_client -d /tmp/device_handlers/qsfp/0 -a config/debug/reset -c set -t bool -v true\n", 
    "tiny_dh_client -d /tmp/device_handlers/qsfp/2 -a config/debug/reset -c set -t bool -v true\n", 
    "tiny_dh_client -d /tmp/device_handlers/qsfp/4 -a config/debug/reset -c set -t bool -v true\n", 
    "tiny_dh_client -d /tmp/device_handlers/qsfp/6 -a config/debug/reset -c set -t bool -v true\n"])
    ssh_nb.cmd(slot2=True, sudo=True, cmd_list=["killall qsfp_device_handler\n"])
    time.sleep(10)

    endresult1 = []
    endresult2 = []
    endresult3 = []
    endresult4 = []
    for i in range(0,81, 1):
        j = i-173
        k = str(j)
        ssh_nbDCPM = SshNbUtils(ip="10.10.50.174", user="smartroot", pw="314740193099")
        dcpresult = ssh_nbDCPM.cmd(sudo=True, cmd_list=["tiny_dh_client -d /tmp/device_handlers/tdcm -a config/dispersion -c set -v " +k+ " -t float \n"])
        time.sleep(7)
        ssh_nb = SshNbUtils(ip="10.10.50.133", user="smartroot", pw="314740193099")
        result1 = ssh_nb.cmd(slot2=True, sudo=True, cmd_list=["tiny_dh_client -d /tmp/device_handlers/qsfp/0 -c get -a data/fec/berCounters\n",])
        result2 = ssh_nb.cmd(slot2=True, sudo=True, cmd_list=["tiny_dh_client -d /tmp/device_handlers/qsfp/2 -c get -a data/fec/berCounters\n",])
        result3 = ssh_nb.cmd(slot2=True, sudo=True, cmd_list=["tiny_dh_client -d /tmp/device_handlers/qsfp/4 -c get -a data/fec/berCounters\n",])
        result4 = ssh_nb.cmd(slot2=True, sudo=True, cmd_list=["tiny_dh_client -d /tmp/device_handlers/qsfp/6 -c get -a data/fec/berCounters\n",])
        result1 = str(result1)
        result2 = str(result2)
        result3 = str(result3)
        result4 = str(result4)
        result1 = result1.split(",")
        result2 = result2.split(",")
        result3 = result3.split(",")
        result4 = result4.split(",")
        result1 = result1[2].split(":") # re.findall(pattern=r'/d[.]/d+', string=result) #,
        result2 = result2[2].split(":")
        result3 = result3[2].split(":")
        result4 = result4[2].split(":")
        endresult1.append(float(result1[2]))
        endresult2.append(float(result2[2]))
        endresult3.append(float(result3[2]))
        endresult4.append(float(result4[2]))
        print(endresult1)
        print(endresult2)
        print(endresult3)
        print(endresult4)

    ssh_nbDCPM = SshNbUtils(ip="10.10.50.174", user="smartroot", pw="314740193099")
    dcpresult = ssh_nbDCPM.cmd(sudo=True, cmd_list=["tiny_dh_client -d /tmp/device_handlers/tdcm -a config/dispersion -c set -v -173 -t float \n"])
    ssh_nb = SshNbUtils(ip="10.10.50.133", user="smartroot", pw="314740193099") 
    ssh_nb.cmd(slot2=True, sudo=True, cmd_list=["tiny_dh_client -d /tmp/device_handlers/qsfp/0 -a config/debug/reset -c set -t bool -v true\n", 
    "tiny_dh_client -d /tmp/device_handlers/qsfp/2 -a config/debug/reset -c set -t bool -v true\n", 
    "tiny_dh_client -d /tmp/device_handlers/qsfp/4 -a config/debug/reset -c set -t bool -v true\n", 
    "tiny_dh_client -d /tmp/device_handlers/qsfp/6 -a config/debug/reset -c set -t bool -v true\n"])
    ssh_nb.cmd(slot2=True, sudo=True, cmd_list=["killall qsfp_device_handler\n"])
    time.sleep(10)

    for i in range(-1,-81, -1):
        j = i-173
        k = str(j)
        ssh_nbDCPM = SshNbUtils(ip="10.10.50.174", user="smartroot", pw="314740193099")
        dcpresult = ssh_nbDCPM.cmd(sudo=True, cmd_list=["tiny_dh_client -d /tmp/device_handlers/tdcm -a config/dispersion -c set -v " +k+ " -t float \n"])
        time.sleep(7)
        ssh_nb = SshNbUtils(ip="10.10.50.133", user="smartroot", pw="314740193099")
        result1 = ssh_nb.cmd(slot2=True, sudo=True, cmd_list=["tiny_dh_client -d /tmp/device_handlers/qsfp/0 -c get -a data/fec/berCounters\n",])
        result2 = ssh_nb.cmd(slot2=True, sudo=True, cmd_list=["tiny_dh_client -d /tmp/device_handlers/qsfp/2 -c get -a data/fec/berCounters\n",])
        result3 = ssh_nb.cmd(slot2=True, sudo=True, cmd_list=["tiny_dh_client -d /tmp/device_handlers/qsfp/4 -c get -a data/fec/berCounters\n",])
        result4 = ssh_nb.cmd(slot2=True, sudo=True, cmd_list=["tiny_dh_client -d /tmp/device_handlers/qsfp/6 -c get -a data/fec/berCounters\n",])
        result1 = str(result1)
        result2 = str(result2)
        result3 = str(result3)
        result4 = str(result4)
        result1 = result1.split(",")
        result2 = result2.split(",")
        result3 = result3.split(",")
        result4 = result4.split(",")
        result1 = result1[2].split(":") # re.findall(pattern=r'/d[.]/d+', string=result) #,
        result2 = result2[2].split(":")
        result3 = result3[2].split(":")
        result4 = result4[2].split(":")
        endresult1.insert(0,float(result1[2]))
        endresult2.insert(0,float(result2[2]))
        endresult3.insert(0,float(result3[2]))
        endresult4.insert(0,float(result4[2]))
        print(endresult1)
        print(endresult2)
        print(endresult3)
        print(endresult4)


    x = range(-253,-92, 1)

    plot1 = plt.figure(1)
    plt.plot(x, endresult1)
    plt.title("Transceiver 1")
    plt.xlabel("Dispersion in ps/nm")
    plt.ylabel("pre-Fec Ber of Transceiver in 108")
    plt.yscale('log')
    plt.savefig("Transceiver1")

    plot2 = plt.figure(2)
    plt.plot(x, endresult2)
    plt.title("Transceiver 2")
    plt.xlabel("Dispersion in ps/nm")
    plt.ylabel("pre-Fec Ber of Transceiver in 108")
    plt.yscale('log')
    plt.savefig("Transceiver2")

    plot3 = plt.figure(3)
    plt.plot(x, endresult3)
    plt.title("Transceiver 3")
    plt.xlabel("Dispersion in ps/nm")
    plt.ylabel("pre-Fec Ber of Transceiver in 108")
    plt.yscale('log')
    plt.savefig("Transceiver3")

    plot4 = plt.figure(4)
    plt.plot(x, endresult4)
    plt.title("Transceiver 4")
    plt.xlabel("Dispersion in ps/nm")
    plt.ylabel("pre-Fec Ber of Transceiver in 108")
    plt.yscale('log')
    plt.savefig("Transceiver4")

    plt.show()

#def test_torrsim():
 #   result = ["{"preFecBer":0.00000615,"preFecBerAverage":0.00000646,"uncorrBer":0.0,"uncorrBerAverage":0.0}"]
  #  result = re.findall(pattern=r'/d[.]/d+', string=result[0])
   # print(result)