import argparse

from command import *

# 创建解析器
parser = argparse.ArgumentParser(description="示例程序")

# 添加子命令解析器
subparsers = parser.add_subparsers(dest="command", help="可用命令")

# 创建子命令 'port'
parser_port = subparsers.add_parser("port", help="端口操作")
# 互斥命令
port_group = parser_port.add_mutually_exclusive_group(required=True)
port_group.add_argument("ps", action="store_true", help="列出当前分配的所有端口名称")
port_group.add_argument("allocate", type=str, action="store", help="请求为一个名字分配一个端口, 端口范围: [8001, 8101), 名字不得重复, 重复的名字将会返回失败")
port_group.add_argument("query", type=str, action="store", help="查询为一个名字分配的端口, 如果尚未分配将会返回失败")
port_group.add_argument("del", action="store_true", metavar="delete", help="删除一个名字和对应端口的关系, 需要 sudo 权限. 尝试删除一个不存在的名字将会返回失败")
# port_group.add_argument("query", )


# 创建子命令 'multiply'
parser_multiply = subparsers.add_parser("multiply", help="乘法操作")
parser_multiply.add_argument("a", type=int, help="第一个数字")
parser_multiply.add_argument("b", type=int, help="第二个数字")

# 解析参数
args = parser.parse_args()

match args.command:
    case "port":
        cmd_port(args)
    case "multiply":
        print(f"{args.a} * {args.b} = {args.a * args.b}")

    case _:
        pass


