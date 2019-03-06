# coding = utf-8

import os
import paramiko


class SSHHelper:
    def __init__(self, ip, port, user, pwd):
        self.__ip = ip
        self.__port = port
        self.__user = user
        self.__pwd = pwd

    def __getssh(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 建立连接
        ssh.connect(self.__ip, self.__port, self.__user, self.__pwd, timeout=10)
        return ssh

    def do_command(self, *cmds):
        ssh = self.__getssh()
        result = ""
        # 输入linux命令
        for cmd in cmds:
            print("cmd:%s" % (cmd))
            stdin, stdout, stderr = ssh.exec_command(cmd)
            # 输出命令执行结果
            result = str(stdout.read())

            print("result:%s" % (result))
        # 关闭连接
        ssh.close()
        return result


# 获取进程id
def getpid():
    appPid = str(ssh.do_command("ps -A|grep %s" % (appname)))
    if appPid == "b''":
        return '', False
    appPid = appPid.replace("b'", "")
    print(appPid)
    if appPid.startswith(" "):
        appPid = appPid[1:]
    return appPid[:appPid.find(" ")], True


# ssh = SSHHelper("10.169.3.7", "22", "root", "root234")
# print(ssh.do_command("pwd"))
#os.chdir("/home/luzq/gopath/sanbao/src/apivideo")

# 远程服务器信息
ip = "10.169.3.7"
user = "root"
port = "22"
pwd = "root234"

# 编译文件
output = os.popen("pwd")
info = output.read()
appname = info[info.rfind("/") + 1:-1]

yon = input("是否重新部署%s(y/n):" % (appname))

if yon != "y" and yon != "Y":
    print("程序退出")
    exit(0)

print("开始构建程序")
try:
    output = os.popen("go build")
except Exception as e:
    print(e)
    exit(100)

print("程序构建成功")

print("开始删除远程服务器文件")
# 删除远程服务器文件
ssh = SSHHelper(ip, port, user, pwd)
# ssh.do_command("cd /data/gopath/" + appname)
apppath = "/data/gopath/%s" % (appname)
result = ssh.do_command("rm -f %s/%s" % (apppath, appname))
print("远程服务器删除成功")

print("开始上传程序")
# 传输文件
try:
    os.system("scp %s %s@%s:%s" % (appname, user, ip, apppath))
except Exception as e:
    print("文件传输失败")
    print(e)
    exit(200)
print("程序上传成功")

print("开始启动程序")
# 远程启动
pid, ok = getpid()
if ok:
    ssh.do_command("kill -9 %s" % (pid))

ssh.do_command("cd %s" % (apppath) + ";" + "nohup ./%s >/dev/null 2>&1 &" % (appname))

pid, ok = getpid()
if ok:
    print("程序启动成功,PID:%s" % (pid))
else:
    print("程序启动失败")
