# darknet-yolo

无原创，全搬运

1.把筛选好的图片放在All_picture文件夹

2.运行pic_rename.py,在rename_imgs文件夹下会得到排序好的voc格式的文件名

3.用vott创建连接，source链接rename_imgs文件夹,output链接vott_output文件夹

4.vott标注好之后，在输出设置中改变输出为voc格式，比例不要紧

5.在vott_output里面的输出文件夹下的Annotations和JPEGImages文件夹复制到voc_process文件夹下,ImageSets不用

6.运行voc_process下的grab_dataset.py文件,即在ImageSets下的Main文件夹下生成相应的txt文件

7.运行main文件夹下的voc_shuffle.py得到打乱的txt文件,之后手动覆盖原来的文件

8.可以运行example.py来生成anchor，尽量生成一下在darknet的cfg文件中替换默认的anchor

9.把voc_process下的Annotations，JPEGImages，ImageSets复制到VOCdevkit/VOC2007/下

10.压缩VOCdevkit,放入source文件夹

11.压缩source,上传到云服务器

12.加压darknet.zip,修改相应的makefile cfg/voc.daa cfg/yolov3-tint.cfg data/voc.names具体修改方法https://blog.csdn.net/zhou4411781/article/details/105112058

13.解压source,使darknet目录下有VOCdevkit/VOC2007/xxx 和 voc_label.py 

14.运行voc_label.py生成darknet真正需要的txt文件

15.训练,计算map  https://github.com/AlexeyAB/darknet#how-to-train-tiny-yolo-to-detect-your-custom-objects

16.训练好的可以用run下面的whx_detect.py python调用darknet接口来实现实时检测,这里的whx_detect是做跑在nano上的,做小车用，调用了串口，不需要就把串口去掉即可，也可以用opencvDnn文件夹下的     cv_test.py用opencv的dnn模块加载darknet模型，但这里只是cpu版本，gpu版本要
    安装cuda，然后改net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)，net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU）这两行即可



