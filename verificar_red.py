import nmap
def scan_network():
    #crea un objeto de escaneo
    nm = nmap.PortScanner()
    #especifica el rango
    ip_range = "190.108.92.19/24"

    #realiza e escaneo en la red
    nm.scan(hosts=ip_range, arguments='-sn')

    #recorre los resultados del escaneo
    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            ip = nm[host]['addresses']['ipv4']
            mac = nm[host]['addresses']['mac']

            print("IP: ", ip)
            print("MAC: ", mac)
scan_network()