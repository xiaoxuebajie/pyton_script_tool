# 去除同级目录下重复图片



## :paperclip:  ​功能介绍

1. 可以删除同级目录下的重复图片
2. 或者将重复图片重命名进行特殊标记
3. 保存所有不重复图片到指定文件夹下
4. 打印重复图片数量以及不重复图片数量



## :paperclip:  使用说明

1. 示例代码数据结构：structure文件夹下有若干子文件夹，每个子文件夹下有若干待检测的图片，remove_duplicated.py以及config.py与structure文件夹同级
2. 在config.py中配置参数
   - 数据路径（例如"./structure/"，右侧含"/"）
   - 保存路径（例如“./save/”，右侧含"/"）
   - 是否删除重复图片（isRemove=True，删除）
   - 是否重命名重复图片（isRename=True，重命名）
   - 是否保存所有不重复图片（isSave=True，保存 ）



## :paperclip:  原理简介

主要是通过判断图片与图片的md5值是否相同来确定两张图片是否重复



## :paperclip:  知识推送

**MD5信息摘要算法**（英语：MD5 Message-Digest Algorithm），一种被广泛使用的[密码散列函数](https://baike.baidu.com/item/密码散列函数/14937715)，可以产生出一个128位（16[字节](https://baike.baidu.com/item/字节/1096318)）的散列值（hash value），用于确保信息传输完整一致。MD5由美国密码学家[罗纳德·李维斯特](https://baike.baidu.com/item/罗纳德·李维斯特/700199)（Ronald Linn Rivest）设计，于1992年公开，用以取代[MD4](https://baike.baidu.com/item/MD4/8090275)算法。这套算法的程序在 RFC 1321 标准中被加以规范。1996年后该算法被证实存在弱点，可以被加以破解，对于需要高度安全性的数据，专家一般建议改用其他算法，如[SHA-2](https://baike.baidu.com/item/SHA-2/22718180)。2004年，证实MD5算法无法防止碰撞（collision），因此不适用于安全性认证，如[SSL](https://baike.baidu.com/item/SSL/320778)公开密钥认证或是[数字签名](https://baike.baidu.com/item/数字签名/212550)等用途。



### :paperclip:  此外

喜欢的朋友请点点 star，关注我的[CSDN](https://mp.csdn.net/console/article)博客，关注我的[哔哩哔哩](https://space.bilibili.com/424394389?spm_id_from=333.788.b_765f7570696e666f.1)，关注我的公众号CV伴读社

<div align=center><img src="https://github.com/xiaoxuebajie/LeetCode/raw/master/solution_python/images/qrcode.jpg" style='zoom:100%'>

