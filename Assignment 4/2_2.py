# Assignment 4 - Question 2
# Get the IP address of a remote host given its name

import socket

def get_remote_host_info():

    remote_host_name = input("Enter remote host name: ")

    try:
        gets_ip_remote = socket.gethostbyname(remote_host_name)

    except socket.error as sockerr:
        print("Error on %s is %s:" % (remote_host_name, sockerr))

    else:
        print("IP Address of %s is %s" %
              (remote_host_name, gets_ip_remote))


# End of Function

if __name__ == "__main__":
    get_remote_host_info()
