import subprocess

import paramiko


def loginToNode(host, username, keyfilename):
    try:
        sshClient = paramiko.SSHClient()
        sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        sshClient.connect(hostname=host, username=username, key_filename=keyfilename)
        print(f"Successful login to node {host} ")

        return sshClient

    except Exception as e:

        print(f"Failed to login to node {host} with an exception {str(e)}")

    sshClient.close()


def execute_commands(ssh, CommandList):
    for cmd in CommandList:
        try:
            stdin, stdout, stderr = ssh.exec_command(cmd)

            print(stdout.read().decode())

            if stderr:
                print(stderr.read().decode())

        except Exception as e:

            print(f"{cmd} execution failed")


def check_reachability(ip):
    print(ip)
    ping_cmd = ["ping", "-c", "4", ip]

    result = subprocess.run(ping_cmd, stdout=subprocess.PIPE)
    return result.returncode == 0


if __name__ == "__main__":

    hostList = [
        {"ip": "54.197.203.109", "username": "ec2-user", "keyfilename": "ec2_in2.pem"},
        {"ip": "54.163.7.177", "username": "ec2-user", "keyfilename": "ec2_in2.pem"}
    ]

    cmdList = ["pwd", "ps -ef"]

    for host in hostList:

        reachable = check_reachability(host['ip'])
        reachable = True
        if reachable:
            print(f"{host['ip']} is reachable . Proceed to login to node")

            ssh = loginToNode(host["ip"], host["username"], host["keyfilename"])
            if ssh:
                execute_commands(ssh, cmdList)

        else:
            print(f"{host['ip']} not reachable")
