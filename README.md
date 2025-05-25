# QRmai
动态生成舞萌DX登录二维码，灵感来源于[MaimaiHelper](https://github.com/SomeUtils/MaimaiHelper)

## 为什么使用QRmai而不是使用MaimaiHelper
1. QRmai无需配置运行环境
2. QRmai具有更多的自定义选项
3. QRmai兼容MaimaiHelper APP

## 部署教程
1. 安装[Python3](https://www.python.org/downloads/)
2. 安装依赖
```bash
pip install -r requirements.txt
```
3. 运行main.py
```bash
python main.py
```
4. 访问http://127.0.0.1:5000/qrmai?token=qrmai

## 配置文件
```
{
  "p1": [1087, 799], // 舞萌 | 中二服务号生成二维码按钮的位置
  "p2": [945, 682], // 生成后的二维码的消息的位置
  "token": "qrmai", // 访问二维码的token
  "host": "127.0.0.1", // 服务器地址 设置成0.0.0.0即可内网访问
  "port": 5000 // 服务器端口
}
```