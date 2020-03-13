import subprocess
import os
import json

#get hostname info
cmd = subprocess.Popen(['hostname'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
(output, err) = cmd.communicate()
hostname=(output.decode().strip())

#get cpu info
cpuinfo = os.popen("cat /proc/cpuinfo | grep 'model name' | uniq | awk -F ':' '{print $2}' | sed 's/^ *//'")
cpuinfo = cpuinfo.read()
cpuinfo = cpuinfo.strip()

#get disks info
diskinfo = os.popen("df -h | grep -v 'tmpfs\|boot\|Filesystem' | awk -F ' ' '{ print $6\" \"$2\" \"}' | tr -d '\n'")
diskinfo = diskinfo.read()
diskinfo = diskinfo.strip()

#get mem info
meminfo = os.popen("free -m | grep '^Mem' | awk -F ' ' '{ print $2  }'")
meminfo = meminfo.read()
meminfo = meminfo.strip()
meminfo = round(int(meminfo)/1000)

#get os info
osinfo = os.popen("uname")
osinfo = osinfo.read()
osinfo = osinfo.strip()

#get os kernel / version info
oskinfo = os.popen("uname -r")
oskinfo = oskinfo.read()
oskinfo = oskinfo.strip()

#get ip addr v4
ipv4info = os.popen("ip addr | grep -w inet | awk -F ' ' '{ print $2\" \"  }' | grep -Ev '^127.0|::1/128' | awk -F '/' '{ print $1\" \" }' | tr -d '\n'")
ipv4info = ipv4info.read()
ipv4info = ipv4info.strip()

#get ip addr v6
ipv6info = os.popen("ip addr | grep -w inet6 | awk -F ' ' '{ print $2\" \"  }' | grep -Ev '^127.0|::1/128' | awk -F '/' '{ print $1\" \" }' | tr -d '\n'")
ipv6info = ipv6info.read()
ipv6info = ipv6info.strip()

#get hardware info

#serial number
serialnmbr = os.popen("sudo dmidecode -s system-serial-number")
serialnmbr = serialnmbr.read()
serialnmbr = serialnmbr.strip()

#product manufacturer
prodman = os.popen("sudo dmidecode -s system-manufacturer")
prodman = prodman.read()
prodman = prodman.strip()

#Product Name
prodname = os.popen("sudo dmidecode -s system-product-name")
prodname = prodname.read()
prodname = prodname.strip()


#print(hostname+" "+cpuinfo+" "+str(meminfo)+" "+diskinfo+" "+osinfo+" "+oskinfo+" "+ipv4info+" "+ipv6info)

print("Hostname: "+hostname)
print("CPU: "+cpuinfo)
print("Memory: "+str(meminfo))
print("Disks: "+diskinfo)
print("OS: "+osinfo)
print("Kernel / Version: "+oskinfo)
print("IP v4 Addr: "+ipv4info)
print("IP v6 Addr: "+ipv6info)
print("Hardware info")
print("Serial number: "+serialnmbr)
print("Product manufacturer: "+prodman)
print("Product name: "+prodname)

inv = {}

inv = {
    'hostname': hostname,
    'cpu': cpuinfo,
    'memory': meminfo,
    'disks': diskinfo,
    'os': osinfo,
    'krnl': oskinfo,
    'ipv4': ipv4info,
    'ipv6': ipv6info,
    'psn': serialnmbr,
    'pmanufacturer': prodman,
    'pname': prodname
}

with open('story.json', 'w') as outfile:
    json.dump(inv, outfile)
