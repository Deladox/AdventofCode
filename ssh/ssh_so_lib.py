from ssh_so.ssh2_python_so import Ssh2PythonNb
from ssh_so.helper.constants import ConstantsPromptsRegex
from ssh_so.helper.ip_settings import IpSettingsSsh

# get prompts_regex_list, to be used when break stdout reading in ssh non-blocking mode
prompts_regex_list = ConstantsPromptsRegex().prompts_re_no1()


class SshNbUtils(IpSettingsSsh):
    def cmd(
        self,
        cmd_list,
        break_list=None,
        break_prompt_re=True,
        sudo=False,
        slot1=False,
        slot2=False,
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
        print(self.ip_set, self.user_set, self.pw_set)
        ssh2 = Ssh2PythonNb(ip=self.ip_set, user=self.user_set, pw=self.pw_set)
        session = ssh2.connect_session(timeout=int(connect_timeout))
        ch = ssh2.connect_channel(session=session)

        if clear_buffer is True:
            ssh2.clear_buffer(ch=ch, break_prompt_re_list=prompts_regex_list)

        # ssh slot
        if slot1 or slot2:
            self.__slot(ssh2=ssh2, ch=ch, slot1=slot1, slot2=slot2)

        # sudo
        if sudo:
            self.__sudo(ssh2=ssh2, ch=ch, sudo=sudo)

        # run cmd's
        for pos, cmd in enumerate(cmd_list):
            break_str = break_list[pos] if break_list else None
            prompts_regex_list_ = prompts_regex_list if break_prompt_re is True else None
            data = ssh2.cmd(ch=ch, cmd=cmd, break_str=break_str, break_prompt_re_list=prompts_regex_list_)
            result_list.append(data)
        ssh2.close_session(session=session)

        return result_list

    # TODO add new func... def cmd_close_between(self):

    def __slot(self, ssh2, ch, slot1=False, slot2=False):

        slot_no = "1" if slot1 else "2"
        if slot1 or slot2:

            # no.1
            cmd = f"ssh{str(slot_no)}\n"
            break_list = ["Password:", "password:", "traffic_module device handler doesn't exist"]
            result = ssh2.cmd(ch=ch, cmd=cmd, break_list=break_list)

            # no.2 "a"
            cmd = f"{self.pw_set}\n"
            break_list = ["Password:", "password:", "Are you sure you want to continue connecting (yes/no)?"]
            result = ssh2.cmd(ch=ch, cmd=cmd, break_list=break_list)

            # no.2 "b" - (after an factorydefault, upgrade etc.)
            if "Are you sure you want to continue connecting (yes/no)?" in result:
                cmd = "yes\n"
                break_list = ["Password:", "password:"]
                ssh2.cmd(ch=ch, cmd=cmd, break_list=break_list)

            # no.3
            cmd = f"{self.pw_set}\n"
            ssh2.cmd(ch=ch, cmd=cmd, break_prompt_re_list=prompts_regex_list)

    def __sudo(self, ssh2, ch, sudo=False):
        if sudo:
            exp_root = "Password:"
            exp_bash = "password for test.script:"
            ssh2.cmd(ch=ch, cmd="sudo -s\n", break_list=[exp_root, exp_bash])
            ssh2.cmd(ch=ch, cmd=f"{self.pw_set}\n", break_prompt_re_list=prompts_regex_list)
