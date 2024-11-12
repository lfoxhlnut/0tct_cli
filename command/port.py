from requests import get, post, delete, Response
from os import system


# 服务器规定名字最长 8 个字符, 
NAME_MAXLEN = 8

def panic(res: Response) -> None:
    print(res.status_code, res.reason)
    exit()

def check_status(res: Response) -> None:
    if res.status_code != 200:
        panic(res)


def cmd_port(argv: list[str]):
    # TODO: 错误检查
    # TODO: 缩进
    match argv[0]:
        case "ps":
            ps()
        case "allocate":
              allocate(argv[1])
        case "query":
              query(argv[1])
        case "del":
              status = system("ls /root >/dev/null 2>&1")
              if status:
                   print(f"cannot del user {argv[1]}: Permission denied")
              else:
                    delete(argv[1])
    pass

    
# 跑在云服上, 所以只需 localhost
base_url = "http://localhost:8000/port"
params = {} # 查询参数
data = {}   # 请求体:表单
json = {}   # 请求体:json
cookies = {}# cookie
headers = {'User-Agent': '0lineTekCenter/tutorial_cli', 'Accept': 'application/json'}

def ps():
    res = get(base_url + "/all", headers=headers)
    check_status(res)
    pair: list = list(res.json())
    
    # 但是 f-string 似乎不支持粘滞位,先这样写
    print(f"{"Name":>8} : Port")
    for i in pair:
        print(f"{i["full_name"]:>8} : {i["port"]}")

# TODO: 抽象以下函数
def allocate(user_name: str):
    res = get(base_url + "/allocate/" + user_name, headers=headers)
    check_status(res)
    print(res.json())


def query(user_name: str):
        res = get(base_url + "/query/" + user_name, headers=headers)
        check_status(res)
        print(res.json())


def delete(user_name: str):
        # TODO: sudo require
        res = delete(base_url + "/del/" + user_name, headers=headers)
        check_status(res)
        print(res.json())
