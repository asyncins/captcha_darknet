from pathlib import Path
from parsel import Selector
from settings import *


def get_coo(width: int, height: int, coo: list) -> tuple:
    """ 返回图片中文字的相对坐标信息（Float）"""
    dw = 1.0 / width
    dh = 1.0 / height
    xmin, ymin, xmax, ymax = coo
    x = (xmin + xmax) / 2.0 * dw
    y = (ymin + ymax) / 2.0 * dh
    w = (xmax - xmin) * dw
    h = (ymax - ymin) * dh
    return x, y, w, h


def xml_to_txt(folder: str, labels: str):
    """ 将图片标注得到的xml数据转换成txt """
    file_input = list(Path(folder).glob('*.{}'.format(FILE_TYPE)))
    class_index = 0  # 目标类别index
    for file in file_input:
        text = path.join(labels, str(file.name).replace(FILE_TYPE, 'txt'))
        # 读取xml文件内容
        content = open(file).read()
        sel = Selector(content)
        names = sel.xpath('//name')
        # 循环标签组
        for i, n in enumerate(names):
            # 取出xml中记录的图片宽高和坐标信息
            width = n.xpath('//width/text()').get()
            height = n.xpath('//height/text()').get()
            xmin = n.xpath('//xmin/text()').extract()[i]
            ymin = n.xpath('//ymin/text()').extract()[i]
            xmax = n.xpath('//xmax/text()').extract()[i]
            ymax = n.xpath('//ymax/text()').extract()[i]
            # 整理坐标和边长
            coo = [int(xmin), int(ymin), int(xmax), int(ymax)]
            bndbox = [str(b) for b in get_coo(int(width), int(height), coo)]
            with open(text, 'a+') as f:
                # 将图片中的文字坐标和宽高信息写入txt
                f.write(str(class_index) + ' ' + ' '.join(bndbox) + '\n')
                f.close()


def generate_train_txt(folder: str, name: str):
    """ 读取目录下的文件路径，并将文件路径写入指定文件 """
    file_input = list(Path(folder).glob('*.{}'.format(IMAGE_TYPE)))
    for file in file_input:
        with open(name, 'a+') as f:
            f.write(str(file) + '\n')
            f.close()


if __name__ == '__main__':
    xml_to_txt(PATH_IMAGES, PATH_LABELS)
    generate_train_txt(PATH_PREDICTS, PATH_PREDICT)
    pass
