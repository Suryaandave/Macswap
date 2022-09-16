import re
from random import choice, randint
import subprocess

print("Enter 1 for manual mac entry and 2 for random mac entry")
inp = input()
interface = input("Enter your network Interface ").strip()


def main():
    if inp == "1":
        new_mac = input(
            "Enter the new mac address you want to change ").strip()
        change_mac(interface, new_mac)
    elif inp == "2":
        print("You had Selected Random")
        mac_random = random()
        print("this is mac {} ".format(mac_random))
        change_mac(interface, mac_random)


def random():
    cisco = ["00", "40", "96"]
    dell = ["00", "14", "22"]
    mac_address = choice([cisco, dell])
    for i in range(3):
        one = choice(str(randint(0, 9)))
        two = choice(str(randint(0, 9)))
        three = (str(one+two))
        mac_address.append(three)
    return ":".join(mac_address)


def change_mac(interface, new_mac):
    subprocess.call(["sudo ifconfig "+str(interface) + " down"], shell=True)
    subprocess.call(["sudo ifconfig "+str(interface) +
                    " hw ether "+str(new_mac) + " "], shell=True)
    subprocess.call(["sudo  ifconfig "+str(interface) + " up"], shell=True)


def currentmac():
    output = subprocess.check_output(["ifconfig "+"wlan0"], shell=True)
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))
    print("old mac address is {}" .format(current_mac))


if __name__ == "__main__":
    main()
