import paramiko
import logging

def ssh_connect(host,username,pem_key_file):
    try:
        sshClient = paramiko.SSHClient()
        sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshClient.connect(hostname=host, username= username, key_filename=pem_key_file)
        return sshClient
    except Exception as e:
        print(f"SSH to {host} failed with exception :{str(e)}")

def logger():
    return 0


def exec_command(ssh,cmd_list):
    for cmd in cmd_list:
        stdin, stdout, stderr = ssh.exec_command(cmd)

        for l in stdout:
            print(l)

        if stderr:
            print(stderr.read().decode())


if __name__ == "__main__":

    hosts = [
        {"ip":"54.197.203.109","username":"ec2-user","key_fn":"ec2_in2.pem"},
        {"ip":"54.163.7.177","username":"ec2-user","key_fn":"ec2_in2.pem"}

    ]

    cmd_list = ["pwd","ps -ef"]

    for h in hosts:
        sshClient = ssh_connect(h["ip"],h["username"],h["key_fn"])

        if sshClient:
            exec_command(sshClient, cmd_list)








