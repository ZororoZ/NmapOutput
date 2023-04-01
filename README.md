# NmapOutput
Nmap输出结果整理工具，更直观查看大批量端口扫描结果，让你扫端口快人一步！！！

目前仅支持Nmap扫描结果为.txt文件的处理，因为看到Git上已经有大佬写了处理.xml文件的工具，后期根据需求再做更改。

## 关于工具的说明及使用，如下：

1、同时支持IPv6和IPv4的扫描结果处理；

2、根据需求可以自行选择是否需要进行URL探测；

Usage:

```
python3 NmapOutput.py result.txt result.csv
```

![image](https://user-images.githubusercontent.com/46238787/229304066-63822933-fa5c-4a3e-8b7f-656ea1ef468d.png)

根据需求选择是否需要进行URL探测:

[注]：T表示进行URL探测；F表示不进行URL探测(不区分大小写)

![image](https://user-images.githubusercontent.com/46238787/229304696-79303ebe-fb47-4ebe-80dd-146fc7bc98fc.png)

![image](https://user-images.githubusercontent.com/46238787/229304711-724ebee7-448d-4522-a003-577172db68a8.png)

## 输出结果如下：

![image](https://user-images.githubusercontent.com/46238787/229304556-9fe674a4-42e6-4b22-af5f-6e6802659fee.png)
