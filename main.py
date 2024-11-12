from sys import argv
from command import *

def panic(info: str = "error") -> None:
    print(info)
    # print(help msg)
    exit()

argc = len(argv)

# argv[0] 是脚本名称
if argc < 2:
    panic()

if argv[1] == "port":
    cmd_port(argv=argv[2:])












