import sys
import os
# from WebAutomation import log

hostname = ""


def main():
    thirdpartyinvoke(sys.argv[1])


def thirdpartyinvoke(hostname):
    try:

        os.system('nmap ' + '-sV ' + hostname)

        os.system('SSLscan ' + hostname)

        print ('SSLScan ' + hostname)

    except Exception as e:
        print(e.message)
        # log.record('debug', e.message)


main()
