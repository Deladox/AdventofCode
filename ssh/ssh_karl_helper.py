import sys
sys.path.append('/home/kalle/Python/ssh/')
sys.path.append('/home/kalle/Python/ssh/ssh_so')
sys.path.append('/home/kalle/Python/ssh/ssh_so/helper')
from ssh_karl import Ssh2PythonNb
from ssh_so.helper.constants import ConstantsPromptsRegex


# get prompts_regex_list, to be used when break stdout reading in ssh non-blocking mode
prompts_regex_list = ConstantsPromptsRegex().prompts_re_no1()


class SshNbUtils:
    def __init__(self, ip, user, pw):
        self.ip = ip
        self.user = user
        self.pw = pw

    def cmd(
        self,
        cmd_list,
        break_list=None,
        break_prompt_re=True,
        clear_buffer=True,
        connect_timeout=10,
    ):
        """

        info. connect to ssh, then run all cmd's in the list and finally disconnect
        note! using IpSettingsSsh e.g.: arg ip, 'out variable': ip_set

        :param cmd_list: list of cmd's ["show status", "show alarm log"]
        :param break_list: corresponds to the cmd_list when to stop reading stdout ["dmin@oslo-1>"]
               Note! break_prompt_re_list is always used (prompts_regex_list)
        :param break_prompt_re: some cmd's has the prompt regex in the replay, e.g. dcp-de22 cat /var/log/messages -->
        Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
        :param sudo: log in as sudo
        :param slot1: log in to slot 1
        :param slot2: log in to slot 2
        :param clear_buffer: used when no clear buffer is required to speed up (e.g. changing pw for crypto user)
        :param connect_timeout: time to try to establish session connection (login to cli "...", still not up/ready)
        :return: result_list
        """

        result_list, result_time = [], []

        # connect
        ssh2 = Ssh2PythonNb(ip=self.ip, user=self.user, pw=self.pw)
        session = ssh2.connect_session(timeout=int(connect_timeout))
        ch = ssh2.connect_channel(session=session)

        if clear_buffer is True:
            ssh2.clear_buffer(ch=ch, break_prompt_re_list=prompts_regex_list)

        # run cmd's
        for pos, cmd in enumerate(cmd_list):
            break_str = break_list[pos] if break_list else None
            prompts_regex_list_ = prompts_regex_list if break_prompt_re is True else None
            data = ssh2.cmd(ch=ch, cmd=cmd, break_str=break_str, break_prompt_re_list=prompts_regex_list_)
            result_list.append(data)
        ssh2.close_session(session=session)

        return result_list


