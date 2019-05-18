"""
this is an example program which used to record tick data
database:pymongo / redis

:keyword 补录数据  ---> will be developed in marrd -> developing at https://github.com/somewheve/marrd
关于补录数据的一点想法:
能不能构建多个类似的程序运行在不同的服务， 然后将数据提交到 同时提交到web服务器，
web服务器经过校验之后（出错数据， 缺失数据进行修正和补录）写入到内存（or redis）中，负责提供每天的数据。
这样每天的数据应该基本不会出错，然后外部程序每天访问这个web服务器提供的数据接口，
将数据维护到自己本地

"""
from json import dumps
from pymongo import MongoClient
from redis import Redis
from recorder import DataRecorder

from ctpbee import CtpBee
from ctpbee import DataSolve
from ctpbee import subscribe

app = CtpBee(__name__)
info = {
    "CONNECT_INFO": {
        "userid": "142164",
        "password": "040501",
        "brokerid": "9999",
        "md_address": "tcp://180.168.146.187:10011",
        "td_address": "tcp://180.168.146.187:10000",
        "product_info": "",
        "auth_code": "",
    },
    "TD_FUNC": True,
    "XMIN": [3]
}
app.config.from_mapping(info)
app.start()
for contracts in app.recorder.get_all_contracts():
    subscribe(contracts.symbol)
