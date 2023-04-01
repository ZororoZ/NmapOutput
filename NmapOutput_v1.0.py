# -*- coding : utf-8 -*-
# -*- author : zoro123 -*-
# -*- version : v1.0 -*-
# -*- date : 2023 -*-

import csv
import requests
import re
import ipaddress
import sys
import os


def get_title(url):

    # 获取title
    try:
        r = requests.get(url, timeout=3)
        title = re.findall('<title>(.*?)</title>', r.text)[0]
    except:
        title = "None"
    return title


def getInput():

    if len(sys.argv) != 3:
        print("\nNmap结果整理脚本，输出为.csv文件\n\nUsage: \n    python3 nmapoutput.py result.txt result.csv\n")
        exit()

    if not os.path.exists(sys.argv[1]):
        print(f"[{sys.argv[1]}] 文件不存在")
        exit()

    infile = sys.argv[1]

    outfile = sys.argv[2]

    return infile, outfile


def Open_Write():

    infile, outfile = getInput()

    # 打开nmap导出的txt文件
    with open(infile, 'r') as f:
        lines = f.readlines()

    # 创建csv文件并写入表头
    with open(outfile, 'w', newline='') as csvfile:
        fieldnames = ['Host', 'Port', 'Server']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # 遍历每一行扫描结果，输出开放的端口到csv文件
        for line in lines:
            if "Nmap scan report for" in line:
                ip = line.split()[-1]
            elif "/tcp" in line and "open" in line:
                port = line.split('/')[0]
                alls = line.split('/')[1]
                server = alls.split()[2]
                writer.writerow({'Host': ip, 'Port': port,'Server': server})


def Url_Scan():

    infile, outfile = getInput()

    # 打开nmap导出的txt文件
    with open(infile, 'r') as f:
        lines = f.readlines()

    # 创建csv文件并写入表头
    with open(outfile, 'w', newline='') as csvfile:
        fieldnames = ['Host', 'Port', 'Server', 'Url', 'Title']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # 遍历每一行扫描结果，输出开放的端口到csv文件
        for line in lines:
            if "Nmap scan report for" in line:
                ip = line.split()[-1]
            elif "/tcp" in line and "open" in line:
                port = line.split('/')[0]
                alls = line.split('/')[1]
                server = alls.split()[2]
                addr = ipaddress.ip_address(ip)
                if addr.version == 4:
                    url = f"http://{ip}:{port}"
                elif addr.version == 6:
                    url = f"http://[{ip}]:{port}"
                title = get_title(url)
                print(f"{url}正在获取title···[{title}]")
                writer.writerow({'Host': ip, 'Port': port, 'Server': server, 'Url': url, 'Title': title})


if __name__ == '__main__':

    print('''

███╗   ██╗███╗   ███╗ █████╗ ██████╗  ██████╗ ██╗   ██╗████████╗██████╗ ██╗   ██╗████████╗
████╗  ██║████╗ ████║██╔══██╗██╔══██╗██╔═══██╗██║   ██║╚══██╔══╝██╔══██╗██║   ██║╚══██╔══╝
██╔██╗ ██║██╔████╔██║███████║██████╔╝██║   ██║██║   ██║   ██║   ██████╔╝██║   ██║   ██║   
██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝ ██║   ██║██║   ██║   ██║   ██╔═══╝ ██║   ██║   ██║   
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║     ╚██████╔╝╚██████╔╝   ██║   ██║     ╚██████╔╝   ██║   
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝      ╚═════╝  ╚═════╝    ╚═╝   ╚═╝      ╚═════╝    ╚═╝   
                                                                          v1.0  by:Zoro123

        ''')
    getInput()

    while True:

        TorF = input("[注]：T表示进行URL探测；F表示不进行URL探测；\n请输入'T'或者'F'选择您是否进行URL探测(不区分大小写)：")
        if TorF not in ('T', 't', 'F', 'f'):
            print("【*】您的输入有误！请按照提示重新输入。\n")
        elif TorF in ('F', 'f'):
            Open_Write()
            print("\n【-】不进行URL探测，结果即将输出！")
            print(f"\n【+】[{sys.argv[2]}]文件已生成，请尽情享用。")
            break
        elif TorF in ('T', 't'):
            Url_Scan()
            print("\n【+】开始URL探测,请等待····\n")
            print(f"\n【+】[{sys.argv[2]}]文件已生成，请尽情享用。")
            break
