# regex_regular expression
class ConstantsPromptsRegex:
    def prompts_re_no1(self):
        """
        info. regular expression corresponds to different prompts,
        intended to be used when stop reading stdout ssh non-blocking mode
        :return:
        """

        # unique pattern's
        cli_re = r"\S+[@].+[>]"  # e.g.: admin@DCP-M40-PAM4-ZR---10>  # r"\S+[@].+[>]"
        root_re = r".+[:][~][$]"  # e.g.: DCP-M40-PAM4-ZR---10:~$
        bash_re = r".+[@].+[:][~][$]"  # e.g: test.script@SO-SRV-TEST01:~$

        root_sudo_re = r".+[:][/].+[/].+[#]"  # e.g: DCP-M40-PAM4-ZR---10:/home/smartroot#
        bash_sudo_re = r".+[@].+[:][/].+[/].+[#]"  # e.g. root@SO-SRV-TEST01:/home/test.script#

        break_prompt_re_list = [cli_re, root_re, bash_re, root_sudo_re, bash_sudo_re]
        return break_prompt_re_list
