import threading
import paramiko
import time

THREADS = 10
PRIVATE_KEY = "torservers_id_ed25519"
TORRC = "torrcs/guard.txt"

def install_server(hostname: str):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname, username="root", key_filename=PRIVATE_KEY)

    sftp_client = ssh_client.open_sftp()

    print(f"APT Updating at {hostname}")
    stdin, stdout, stderr = ssh_client.exec_command("apt update -y")
    stdout.read()
    print(f"APT update done at {hostname}")

    print(f"Installing Tor at {hostname}")
    stdin, stdout, stderr = ssh_client.exec_command("apt install tor -y")
    stdout.read()
    print(f"Tor installation completed at {hostname}")

    print(f"Uploading {TORRC} config to {hostname}:/etc/tor/torrc")
    sftp_client.put(TORRC, "/etc/tor/torrc")
    print(f"Uploaded {TORRC} config to {hostname}:/etc/tor/torrc")

    print(f"Restarting Tor at {hostname}")
    stdin, stdout, stderr = ssh_client.exec_command("systemctl restart tor@default")
    stdout.read()
    print(f"Tor successfully installed at {hostname}. Thanks for contributing to the Tor community!")
    
    sftp_client.close()
    ssh_client.close()

def main():
    with open("server_list.txt", "r") as file:
        server_list = [x.strip() for x in file.read().splitlines() if x.strip() and not x.strip().startswith("#")]
        file.close()
    
    for server in server_list:
        while True:
            if threading.active_count() > THREADS:
                time.sleep(0.05)
                continue
            break

        threading.Thread(target=install_server, args=[server], daemon=True).start()
    
    while True:
        time.sleep(0.05)
        if threading.active_count() <= 1:
            break
    
    print(f"Mass Tor nodes distribution completed.")

if __name__ == "__main__":
    main()
