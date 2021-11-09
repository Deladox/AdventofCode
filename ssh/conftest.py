import pytest
import sys
sys.path.append('/home/kalle/Python/ssh/')
sys.path.append('/home/kalle/Python/ssh/ssh_so')
sys.path.append('/home/kalle/Python/ssh/ssh_so/helper')
print(sys.path)
from ssh_karl_helper import SshNbUtils

@pytest.fixture(scope="session")
def ssh_admin():
    ssh_admin = SshNbUtils(ip="10.10.20.12", user="admin", pw="admin")
    return ssh_admin


@pytest.fixture(scope="session")
def ssh_root():
    ssh_root = SshNbUtils(ip="10.10.50.133", user="smartroot", pw="314740193099")
    return ssh_root
