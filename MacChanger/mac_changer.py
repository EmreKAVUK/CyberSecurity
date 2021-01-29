import subprocess
import optparse
parse_object = optparse.OptionParser()
parse_object.add_option("-i","--interface",dest="interface",help="Interface to change")
parse_object.add_option("-m","--mac",dest="mac_adress",help="The mac adress you want")
(user_info,arguments) = parse_object.parse_args()
user_interface = user_info.interface
user_mac_adress = user_info.mac_adress
print("#Mac Changer Started#")
print("Your new mac adress : ",user_mac_adress)
subprocess.call(["ifconfig",user_interface,"down"])
subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_adress])
subprocess.call(["ifconfig",user_interface,"up"])