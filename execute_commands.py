import paramiko


def ssh_Connect(host, username, filename):
    try:
        sshClient = paramiko.SSHClient()
        sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshClient.connect(hostname=host, username=username, key_filename=filename)
        print(f"SSH connection to {host} successful")
        return sshClient
    except Exception as e:

        print(f"Couldn't connect to {host}:{str(e)}")


def exec_cmd(sshclient, commands_list):
    for command in commands_list:
        try:
            stdin, stdout, stderr = sshclient.exec_command(command)
            for line in stdout:
                print(line)

            print(stderr.read().decode())
        except Exception as e:
            print(f"Command {cmd} execution failed: {str(e)}")


if __name__ == "__main__":
    host = [
        {"ip": "54.197.203.109", "username": "ec2-user", "keyfilename": "ec2_in2.pem"},
        {"ip": "54.163.7.177", "username": "ec2-user", "keyfilename": "ec2_in2.pem"}
    ]

    cmd = ["pwd", "ps -ef"]
    for h in host:
        try:
            sshClient = ssh_Connect(h["ip"], h["username"], h["keyfilename"])
            if sshClient:
                exec_cmd(sshClient, cmd)
            else:
                print("Check.........")
        except Exception as e:
            print(f"Exception {str(e)}")


