# Assignment 4 - Question 2
# Get the hostname of a remote host given its IP address

import socket

def get_remote_host_name():

    remote_ip_address = input("Enter IP address: ")

    try:
        hostname = socket.gethostbyaddr(remote_ip_address)

    except socket.error as sockerr:
        print("Error on %s is %s:" % (remote_ip_address, sockerr))

    else:
        print("Hostname of %s is %s" %
              (remote_ip_address, hostname))


# End of Function

if __name__ == "__main__":
    get_remote_host_name()
