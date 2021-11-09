#from environment.extract import EnvYmlJenkins

class IpSettingsSsh:
    """
    info. based on the arg. collect data from .yml file and select 'ip', 'user' and 'pw'
    :return: self.ip_set, self.user_set, self.pw_set
    """

    def __init__(
        self,
        node1=False,
        node2=False,
        node3=False,
        admin=False,
        root=False,
        crypto=False,
        crypto_d=False,
        ip=None,
        user=None,
        pw=None,
    ):


        # create dictionary's based on the class arguments
        dict_location = {"node1": node1, "node2": node2, "node3": node3}
        dict_user = {"admin": admin, "root": root, "crypto": crypto, "crypto_d": crypto_d}
        dict_user_settings = {"ip": ip, "user": user, "pw": pw}

        # dict based on data in the .yml file
        dict_ip_settings = self.__dict_ip_settings()

        # 1. ip setting by the user
        if None not in dict_user_settings.values():  # if all ip, user and pw is not None
            self.ip_set = ip
            self.user_set = user
            self.pw_set = pw

        # 2. ip settings based on the location and user (according ti the .yml file)
        elif True in dict_location.values() and True in dict_user.values():
            location_key = ""  # e.g. node1, node3
            for key in dict_location:
                if dict_location[key] is True:
                    location_key = key  # used when get ip's form dict_ip_settings

            user_key = ""  # e.g. admin, root
            for key in dict_user:
                if dict_user[key] is True:
                    user_key = key  # used when get ip's form dict_ip_settings

            # get ip settings
            self.ip_set = dict_ip_settings.get(location_key).get("ip")
            self.user_set = dict_ip_settings.get(location_key).get(user_key).get("user")
            self.pw_set = dict_ip_settings.get(location_key).get(user_key).get("pw")
        else:
            msg1 = f"ip setting missing dict_location: {dict_location}, dict_user: {dict_user}"
            msg2 = f"dict_user_settings: {dict_user_settings}, dict_ip_settings: {dict_ip_settings}"
            self.ip_set, self.user_set, self.pw_set = None, None, None

    def __dict_ip_settings(self):
        """
        info. create an dict based on the .yml file
        e.g. {'node1': {'ip': '10.10.70.10', 'admin': {'user': 'admin', 'pw': 'admin'}, 'root': {'user': 'smartroot', 'pw': '314740193099'}, 'crypto': {'user': None, 'pw': None}, 'crypto_d': {'user': None, 'pw': None}}, 'node2': {'ip': None, 'admin': {'user': None, 'pw': None}}, 'node3': {'ip': '10.10.70.11', 'admin': {'user': 'admin', 'pw': 'admin'}}}
        :return: dict
        
        env = EnvYmlJenkins()

        # node1
        l_ip = env.node1_chassis_ip
        d_l_a = {"user": env.node1_chassis_admin_user, "pw": env.node1_chassis_admin_pw}
        d_l_r = {"user": env.node1_chassis_root_user, "pw": env.node1_chassis_root_pw}
        d_l_c = {"user": env.node1_chassis_crypto_user, "pw": env.node1_chassis_crypto_pw}
        d_l_cd = {"user": env.node1_chassis_crypto_user, "pw": env.node1_chassis_crypto_pw_default}

        # node2
        i_ip = env.node2_chassis_ip
        d_i_a = {"user": env.node2_chassis_admin_user, "pw": env.node2_chassis_admin_pw}

        # node3
        r_ip = env.node3_chassis_ip
        d_r_a = {"user": env.node3_chassis_admin_user, "pw": env.node3_chassis_admin_pw}
        # ip_settings dict
        ip_settings = {
            "node1": {"ip": l_ip, "admin": d_l_a, "root": d_l_r, "crypto": d_l_c, "crypto_d": d_l_cd},
            "node2": {"ip": i_ip, "admin": d_i_a},
            "node3": {"ip": r_ip, "admin": d_r_a},
        }
        return ip_settings
        """

# TODO - old:
#  - some issues with from dataclasses import dataclass in jenkins???
'''


from dataclasses import dataclass

from environment.extract import EnvYmlJenkins
from utils.logger import Logger


@dataclass
class IpSettingsSsh:
    local: bool = False
    interop: bool = False
    remote: bool = False

    admin: bool = False
    root: bool = False
    crypto: bool = False
    crypto_d: bool = False

    ip: str = None
    user: str = None
    pw: str = None

    def __post_init__(self):
        """

        info. based on the arg. collect data from .yml file and select 'ip', 'user' and 'pw'
        :return: self.ip_set, self.user_set, self.pw_set
        """
        logger = Logger()

        # create dictionary's based on the class arguments
        dict_location = {"local": self.local, "interop": self.interop, "remote": self.remote}

        dict_user = {"admin": self.admin, "root": self.root, "crypto": self.crypto, "crypto_d": self.crypto_d}

        dict_user_settings = {"ip": self.ip, "user": self.user, "pw": self.pw}

        # dict based on data in the .yml file
        dict_ip_settings = self.__dict_ip_settings()

        # 1. ip setting by the user
        if None not in dict_user_settings.values():  # if all ip, user and pw is not None
            self.ip_set = self.ip
            self.user_set = self.user
            self.pw_set = self.pw

        # 2. ip settings based on the location and user (according ti the .yml file)
        elif True in dict_location.values() and True in dict_user.values():
            location_key = ""  # e.g. local, remote
            for key in dict_location:
                if dict_location[key] is True:
                    location_key = key  # used when get ip's form dict_ip_settings

            user_key = ""  # e.g. admin, root
            for key in dict_user:
                if dict_user[key] is True:
                    user_key = key  # used when get ip's form dict_ip_settings

            # get ip settings
            self.ip_set = dict_ip_settings.get(location_key).get("ip")
            self.user_set = dict_ip_settings.get(location_key).get(user_key).get("user")
            self.pw_set = dict_ip_settings.get(location_key).get(user_key).get("pw")
        else:
            msg1 = f"ip setting missing dict_location: {dict_location}, dict_user: {dict_user}"
            msg2 = f"dict_user_settings: {dict_user_settings}, dict_ip_settings: {dict_ip_settings}"
            logger.log(error=True, msg=f"{msg1}, {msg2}")
            self.ip_set, self.user_set, self.pw_set = None, None, None

    def __dict_ip_settings(self):
        """
        info. create an dict based on the .yml file
        e.g. {'local': {'ip': '10.10.70.10', 'admin': {'user': 'admin', 'pw': 'admin'}, 'root': {'user': 'smartroot', 'pw': '314740193099'}, 'crypto': {'user': None, 'pw': None}, 'crypto_d': {'user': None, 'pw': None}}, 'interop': {'ip': None, 'admin': {'user': None, 'pw': None}}, 'remote': {'ip': '10.10.70.11', 'admin': {'user': 'admin', 'pw': 'admin'}}}
        :return: dict
        """
        env = EnvYmlJenkins()

        # local
        l_ip = env.local_chassis_ip
        d_l_a = {"user": env.local_chassis_admin_user, "pw": env.local_chassis_admin_pw}
        d_l_r = {"user": env.local_chassis_root_user, "pw": env.local_chassis_root_pw}
        d_l_c = {"user": env.local_chassis_crypto_user, "pw": env.local_chassis_crypto_pw}
        d_l_cd = {"user": env.local_chassis_crypto_user, "pw": env.local_chassis_crypto_pw_default}

        # interop
        i_ip = env.interop_chassis_ip
        d_i_a = {"user": env.interop_chassis_admin_user, "pw": env.interop_chassis_admin_pw}

        # remote
        r_ip = env.remote_chassis_ip
        d_r_a = {"user": env.remote_chassis_admin_user, "pw": env.remote_chassis_admin_pw}

        # ip_settings dict
        ip_settings = {
            "local": {"ip": l_ip, "admin": d_l_a, "root": d_l_r, "crypto": d_l_c, "crypto_d": d_l_cd},
            "interop": {"ip": i_ip, "admin": d_i_a},
            "remote": {"ip": r_ip, "admin": d_r_a},
        }
        return ip_settings
'''
