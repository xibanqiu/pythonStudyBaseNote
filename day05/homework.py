#一、有如下变量（tu是个元组），请实现要求的功能
tu = ("alex",[11,22,{"k1":'v1',"k2":["age","name"],"k3":(11,22,33)},44])
#1、讲述元组的特性
#2、讲述元组的第一个元素alex是否被修改
#3、请问tu变量中的“k2”，对应的是什么类型，是否可以被修改，如果可以，请在其中添加一个元素‘Seven’
#4、请问tu变量中的“k4”，对应的是什么类型，是否可以被修改，如果可以，请在其中添加一个元素‘Seven’

#二、字典dic,
dic={"k1":"v1","k2":"v2","k3":[11,22,33],}
#1、请循环输出所有的key
#2、请循环输出所有的value
#3、请循环输出所有的key 、value
#4、请在字典后添加一个键值对，"k4"："v4",输出添加后的字典
#5、修改k1的值为 ‘alex’
#6、在k3追加一个元素 44 ，输出修改后的字典
#7、在k3对应的值的第一个位置插入一个元素18，输出修改后的字典

#3、元素分类
#有如下的值 li=[11,22,33,44,55,66,77,88,99,90]，将所有大于66的值保存至字典的第一个key中，将小于66的值保存在第二个key 的值中。

#4、输出商品列表，用户输入序号，显示用户选中的商品
li = ["手机", "电脑", "鼠标垫", "游艇"]  # 商品
'''
要求：1、页面显示  序号 + 商品名称 如：
                1  手机
                2  电脑
      2、用户输入选择的商品序号，然后打印商品名称
      3、如果用户输入的商品序号有误，则提示输入有误，并重新输入
      4、用户输入    Q 或者 q ，退出程序
      


'''