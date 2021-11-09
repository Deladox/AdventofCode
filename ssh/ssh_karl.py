import sys
sys.path.append('/home/kalle/Python/ssh/')
sys.path.append('/home/kalle/Python/ssh/ssh_so')
sys.path.append('/home/kalle/Python/ssh/ssh_so/helper')
import re
import socket
import time
from ssh2.session import Session


class Ssh2PythonNb:
    def __init__(self, ip, user, pw):
        self.ip = ip
        self.user = user
        self.pw = pw

    def connect_session(self, timeout=10):
        """
        ssh2-python in none blocking mode
        note! using IpSettingsSsh e.g.: arg ip, 'out variable': ip_set

        :param timeout: time to try to establish session connection.
        intended use, system is rebooted func "cli ready" (connection --> login to cli, still not up, Please wait. ...)

        :return: session
        """

        #print(f"ip: {self.ip}, user:{self.user}, pw:{self.pw}")

        sock, session = None, None
        start = time.time()
        timeout_ = time.time() + timeout
        while timeout_ >= time.time():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((self.ip, 22))
                session = Session()
                session.handshake(sock)
                session.userauth_password(username=self.user, password=self.pw)
            except:
                sock.close()
                time.sleep(5)
            else:
                break
        time_c = int(time.time() - start)
        print(f"connect, time: {time_c}s") if time_c > timeout - 20 and time_c > 30 else None
        return session

    def connect_channel(self, session):
        """
        info. connect an channel and set session to none blocking
        :param session: object
        :return: the channel
        """

        ch = session.open_session()
        ch.pty(term="vt100")
        ch.shell()
        session.set_blocking(False)
        return ch

    def clear_buffer(self, ch, break_prompt_re_list):
        """
        info. clear buffer is done by reading the stdout. Recommended to be done before sending cmd
        Typically brake at the prompt, e.g. admin@DCP-M40-PAM4-ZR---10>
        if the pattern_re_list doesn't match the stdout it will stop at the cli timeout

        :param ch: ch
        :param break_prompt_re_list:
        :return: stdout_str
        """

        time_measure_start = time.time()
        stdout_str = self.__read_stdout_break(ch=ch, break_re_list=break_prompt_re_list)
        time_m = "{:.2f}".format(time.time() - time_measure_start)
        #logger.log(msg=f"clear the buffer, time: {time_m}s")
        return stdout_str

    def cmd(self, ch, cmd, break_str=None, break_list=None, break_prompt_re_list=None):
        """
        info. not! the ssh2-python lib is transparent and does not add \n char in non-blocking mode
        SO cli (R6.1.1): <cmd> <\n>, <cmd> < \t>, <cmd> < ?>

        :param ch: ch
        :param cmd: cmd as a str
        :param break_str: optional string
        :param break_list: optional list
        :param break_prompt_re_list: regular expression e.g. r'\S+[@].+[>]' used in (re.findall)
        :return: stdout_str
        """

        # TODO fix measure_time...

        ch.write(cmd)

        time_measure_start = time.time()
        result_stdout = self.__read_stdout_break(
            ch=ch, break_list=break_list, break_str=break_str, break_re_list=break_prompt_re_list
        )
        stdout_str = result_stdout

        time_m = "{:.2f}".format(time.time() - time_measure_start)
        return stdout_str

    def __read_stdout_break(self, ch, break_str=None, break_list=None, break_re_list=None):
        """
        info. read stdout until an user brake occur (break_str, break_list, break_re_list) or timeout

        :param ch: ch
        :param break_str: optional string
        :param break_list: optional list
        :param break_re_list: regular expression e.g. r'\S+[@].+[>]' used in (re.findall)
        :return: stdout_str
        """

        stdout_str = ""
        timeout_cli = time.time() + 32  # cli has an timeout at 30s in R6.1.1

        flag_break = False
        while True:
            size, data = ch.read()
            if size > 0:
                stdout_str += data.decode("utf-8")

            # 1. break at - regular expression (e.g. cli prompt, bash prompt, server prompt)
            if type(break_re_list) is list:
                for pattern_re in break_re_list:
                    exp_list = re.findall(pattern=pattern_re, string=stdout_str)
                    exp_str = exp_list[0] if exp_list else "!¤%#&=}!_timeout_pattern_!¤%#&=}!"
                    if exp_str in stdout_str:
                        flag_break = True
                        break

            # 2. break at - expected string
            if break_str is not None and break_str in stdout_str:
                flag_break = True

            # 3 break at - expected string in list
            if break_list is not None:
                for break_str in break_list:
                    if break_str in stdout_str:
                        flag_break = True

            # 4. break at - cli timeout
            if time.time() > timeout_cli:
                msg = f"the ssh stdout reading is about to timeout! stdout_str:{stdout_str}"
                flag_break = True

            # break
            if flag_break is True:
                return stdout_str

    def close_session(self, session):
        session.disconnect()
