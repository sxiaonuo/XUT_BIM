原链接：https://blog.csdn.net/weixin_39715012/article/details/114635415

使用这个annotation-tool.py可以生成txt格式的标注文件
使用TXT2JSON可以将txt转为json格式
使用lcnn中的dataset/wireframe.py可以将json转换为.npz格式，但是这段代码使用多线程，handle函数无法被正确序列化，因此无法运行。可以使用learn.ipynb
