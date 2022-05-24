# 文件结构

```ansi
.
|-- backup(备份数据集)
|-- Data(数据集存放)
|   |--train_data(训练集)
|   |--valid_data(验证集)
|   |--test_data(测试集)
|-- input/in(存放输入图片转换后的文件夹)
|-- input_convert(存放输入图片的文件夹)
|-- logs(tensorboard日志目录)
|-- output_log(测试用的tensorboard的日志目录)
|-- apply.ipynb(将训练好的模型用于预测给出的图片->应用层)
|-- Dataset_process.py(对数据集进行预处理分类)
|-- module_yy.py(基于nn.Module搭建模型)
|-- train_yy.ipynb(训练模型&保存模型参数)
|-- test_yy.ipynb(用测试集测试模型的准确度)
|-- ZH_Module.pth(保存训练好模型的参数)
```
+ 几个重要文件：
  + Data目录 ->存放训练集，验证集，测试集
  + module_yy.py ->存放模型的类对象
  + train_yy.ipynb ->训练和保存模型参数的文件
  + test_yy.ipynb ->测试模型在测试集上的准确率
  + ZH_Module.pth ->以字典形式保存模型的参数
注意：
- 最后测试集的准确率测试放在test_yy.ipynb，运行代码既可以查看打印出的准确率
- 如果想要识别传入的图片是哪一个类别，可以将图片放入input_convert文件夹中，运行apply.ipynb查看结果（不限制输入图片的size）[可从test_data测试集文件夹中复制图片到测试输出文件夹中]

```ansi
网络结构：(参考LeNet5模型)
# 假设batch_size = 64
part 1(特征提取)
1. 卷积层1，kernel_size = 3, padding = same
64x3x64x64 -> 64x8x64x64
2. 非线性激活ReLU
3. 池化层1, kernel_size = 2, 步长 = 2
64x8x64x64 -> 64x8x32x32

4. 卷积层2，kernel_size = 3, padding = same
64x8x32x32 -> 64x16x32x32
5. 非线性激活ReLU
6. 池化层2, kernel_size = 2, 步长 = 2
64x16x32x32 -> 64x16x16x16

7. 卷积层3，kernel_size = 3, padding = same
64x16x16x16 -> 64x32x16x16
7. 非线性激活ReLU
9. 池化层3, kernel_size = 2, 步长 = 2
64x32x16x16 -> 64x32x8x8

10. 卷积层4，kernel_size = 3, padding = same
64x32x8x8 -> 64x64x8x8
11. 非线性激活ReLU

12. Flatten展开
64x64x8x8 -> 64x4096

13. 全连接层1
64x4096 -> 64x128
14. 非线性激活ReLU

15. Droupout正则化层，p=0.15

16. 全连接层2
64x128 -> 64x10
17. Softmax
->得到十个类别的概率
```


