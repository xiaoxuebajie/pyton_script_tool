import os
import hashlib
import numpy as np
from PIL import Image
from config import Config

def remove_duplicated(data_dir, save_dir, isRename, isRemove, isSave):
    temp = set()
    count = 0
    classes = os.listdir(data_dir)

    for cls in classes:
            files = os.listdir(data_dir + cls)
            for file in files:
                file_path = data_dir + cls + '/' + file  # 获得完整的路径
                rename_path = data_dir + cls + '/' + 'duplicated' + file
                img = Image.open(file_path)  # 打开图片
                img_array = np.array(img)  # 转为数组
                md5 = hashlib.md5()  # 创建一个hash对象
                md5.update(img_array)  # 获得当前文件的md5码
                if md5.hexdigest() not in temp:  # 如果当前的md5码不在集合中
                    temp.add(md5.hexdigest())  # 则添加当前md5码到集合中
                    if isSave:
                        img.save(save_dir + file)  # 并保存当前图片到保存文件的路径
                else:
                    count += 1  # 否则删除图片数加一
                    if isRemove:
                        os.remove(file_path)
                    elif isRename:
                        os.rename(file_path, rename_path)

    print('total duplicated images:', count)
    print('total non duplicated images', len(temp))

if __name__ == '__main__':
    opt = Config()
    remove_duplicated(opt.data_dir, opt.save_dir, opt.isRename, opt.isRemove, opt.isSave)