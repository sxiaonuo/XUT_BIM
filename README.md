# XUT_BIM
![image](/图片库/5d1ff55687d61f2ec3fdc3fd971449d.png)
## 项目简介
本软件为智能化BIM软件。为节约成本，提高效率。
*建筑信息模型（BIM）是指在建设工程及设施的规划、设计、施工以及运营维护阶段全寿命周期创建和管理建筑信息的过程，全过程应用三维､实时､动态的模型涵盖了几何信息､空间信息､地理信息､各种建筑组件的性质信息及工料信息。——《建筑信息模型（BIM）职业技能等级标准》*

## 运行环境说明
### Python环境
```python 
python == 3.9
```
`requirements.txt`
```text
jupyter
ezdxf
pyautocad
```

## 图像重构
### 实例分割
**图像分类** 建筑设计，室内设计，管线设计
**实例分割** 在设计图上分割每一种实例，目标：1. 可分割超大图，2. 精度高， 3. 对速度无要求

## 资料
### CAD安装教程
cad学生认证：[学生认证](https://zhuanlan.zhihu.com/p/341446584)
[CAD中文官网](https://www.autodesk.com.cn/)
### ezdxf
中文教程 [python：ezdxf——教程-CSDN博客](https://blog.csdn.net/weixin_44374471/article/details/106974561)
ezdxf官方文档 [Quick-Info — ezdxf 1.2.0b1 documentation (mozman.at)](https://ezdxf.mozman.at/docs/)

### 视觉
[OpenSNN文章推荐:【python-opencv】canny边缘检测_opencv 开源社区-CSDN博客](https://blog.csdn.net/snngrow/article/details/131728827)
[从R-CNN到YOLO，2020 图像目标检测算法综述 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/268566357)
[肺部CT图像分割及重建系统-CSDN博客](https://blog.csdn.net/H_SWhite/article/details/86006886)
[使用 Keras 深度学习库进行CNN 图像识别_keras 图片识别-CSDN博客](https://blog.csdn.net/m0_59596937/article/details/128789102)
[改进卷积神经网络SAR图像去噪算法 (ceaj.org)](http://cea.ceaj.org/CN/abstract/abstract38872.shtml#:~:text=%E6%91%98%E8%A6%81%EF%BC%9A%20%E5%90%88%E6%88%90%E5%AD%94%E5%BE%84%E9%9B%B7%E8%BE%BE%EF%BC%88SAR%EF%BC%89%E9%80%9A%E5%B8%B8%E4%BC%9A%E8%A2%AB%E4%B8%80%E7%A7%8D%E7%A7%B0%E4%B8%BA%E6%95%A3%E6%96%91%E7%9A%84%E4%B9%98%E6%80%A7%E5%99%AA%E5%A3%B0%E5%B9%B2%E6%89%B0%EF%BC%8C%E8%BF%99%E4%BD%BF%E5%BE%97%E5%9B%BE%E5%83%8F%E7%9A%84%E8%A7%A3%E9%87%8A%E5%8F%98%E5%BE%97%E5%9B%B0%E9%9A%BE%E3%80%82,%E4%B8%BA%E8%A7%A3%E5%86%B3%E8%BF%99%E4%B8%80%E9%97%AE%E9%A2%98%EF%BC%8C%E6%8F%90%E5%87%BA%E4%B8%80%E7%A7%8D%E6%94%B9%E8%BF%9B%E5%8D%B7%E7%A7%AF%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9CSAR%E5%9B%BE%E5%83%8F%E5%8E%BB%E5%99%AA%E6%96%B9%E6%B3%95%E3%80%82%20%E5%AF%B9%E5%9B%BE%E5%83%8F%E8%BF%9B%E8%A1%8C%E4%B8%8B%E9%87%87%E6%A0%B7%E5%86%8D%E5%AF%B9%E4%B8%8B%E9%87%87%E6%A0%B7%E5%AD%90%E5%9B%BE%E5%83%8F%E8%BF%9B%E8%A1%8C%E5%8D%B7%E7%A7%AF%E6%8F%90%E5%8F%96%E7%89%B9%E5%BE%81%EF%BC%8C%E8%BF%99%E5%8F%AF%E4%BB%A5%E6%9C%89%E6%95%88%E6%89%A9%E5%A4%A7%E6%84%9F%E5%8F%97%E9%87%8E%E6%8F%90%E9%AB%98%E5%8E%BB%E5%99%AA%E6%95%88%E7%8E%87%EF%BC%9B%E4%B8%BA%E4%BA%86%E5%87%8F%E5%B0%91%E6%A2%AF%E5%BA%A6%E6%B6%88%E5%A4%B1%E9%97%AE%E9%A2%98%E5%92%8C%E6%8F%90%E9%AB%98%E6%A8%A1%E5%9E%8B%E5%8E%BB%E5%99%AA%E6%80%A7%E8%83%BD%EF%BC%8C%E7%BD%91%E7%BB%9C%E5%8F%88%E5%BC%95%E5%85%A5%E4%BA%86%E8%B7%B3%E8%B7%83%E8%BF%9E%E6%8E%A5%E5%92%8C%E6%AE%8B%E5%B7%AE%E5%AD%A6%E4%B9%A0%E7%AD%96%E7%95%A5%EF%BC%9B%E5%88%A9%E7%94%A8%E4%BB%BF%E7%9C%9F%E5%92%8C%E5%AE%9E%E6%B5%8B%E6%95%B0%E6%8D%AE%E5%AF%B9%E7%BD%91%E7%BB%9C%E8%BF%9B%E8%A1%8C%E6%B5%8B%E8%AF%95%E4%B8%8E%E8%AF%84%E4%BC%B0%EF%BC%8C%E5%AE%9E%E9%AA%8C%E7%BB%93%E6%9E%9C%E8%A1%A8%E6%98%8E%E6%8F%90%E5%87%BA%E7%9A%84%E6%96%B9%E6%B3%95%E5%85%B7%E6%9C%89%E8%89%AF%E5%A5%BD%E7%9A%84%E5%8E%BB%E5%99%AA%E6%95%88%E6%9E%9C%E5%92%8C%E8%BE%83%E9%AB%98%E7%9A%84%E8%AE%A1%E7%AE%97%E6%95%88%E7%8E%87%EF%BC%8C%E5%AF%B9%E6%AF%94%E5%85%B6%E4%BB%96%E5%8E%BB%E5%99%AA%E6%96%B9%E6%B3%95%EF%BC%8C%E8%AF%A5%E6%96%B9%E6%B3%95%E4%B8%8D%E4%BB%85%E5%8E%BB%E5%99%AA%E6%95%88%E6%9E%9C%E5%A5%BD%EF%BC%8C%E8%80%8C%E4%B8%94%E6%95%88%E7%8E%87%E6%9B%B4%E9%AB%98%E3%80%82)
[260：vue+openlayers 通过webgl方式加载矢量图层-CSDN博客](https://blog.csdn.net/cuclife/article/details/135838593)
[实例分割最新最全面综述：从Mask R-CNN到BlendMask - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/110132002)

### 相关
[格式转换](/笔记/格式转换.md)
[相关项目](/笔记/相关项目.md)
