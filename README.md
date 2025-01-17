# QASystemOnMedicalGraph

该项目是基于医疗领域知识图谱的问答系统。实现比较简单。

从无到有搭建一个医疗领域知识图谱(知识图谱规模较小)，并基于此知识图谱搭建问答系统实现自动问题解析和回答。

本文参考：[https://github.com/zhihao-chen/QASystemOnMedicalKG](https://github.com/zhihao-chen/QASystemOnMedicalKG)

# 项目复现

> 邮箱 boli_lemon boli_lemon@foxmail.com

复现时间： <u>2023/03/29</u>

环境：neo4j-5.5.0 python-3.8.16 windows11

- [解决 AttributeError: module ‘numpy‘ has no attribute ‘int‘_there2belief的博客-CSDN博客](https://blog.csdn.net/dou3516/article/details/129007534) numpy如果出现以上报错需要手动改一下

- 添加了requirement.txt

- 解各种第三方库的版本冲突

- 修改了部分源码（注释），不影响项目效果

- neo4j配置文件独立于secret/keys.csv，文件结构如下

## 复现步骤

1. 下载neo4j-5.5.0并启动

2. 从下面的**百度网盘**链接里下载**预训练词向量**到**data/**（因为这文件太大了，所以没放在仓库里）

3. 下载安装anaconda并使用conda创建及激活环境 (接下来的操作*均在*conda虚拟环境中进行)
   
   **TIPS**:  不习惯命令行的话可以用anaconda自带的图形界面Anaconda Navigator来做
   
   ```shell
   conda create -n medical-qa python=3.8
   
   conda activate medical-qa
   ```

4. 安装第三方库
   
   ```
   pip install -r requirement.txt
   ```

5. 配置csv文件（如有需求可自行拓展）
   
   默认：secret/keys.csv
   
   ```
   url,http://localhost:7474
   username,neo4j
   password,neo4j
   database,neo4j
   ```

6. 搭建知识图谱：python build_grapy.py（配置还可以的话没有几小时那么慢）

7. 启动问答测试：python kbqa_test.py

# 项目效果

以下两张图是系统实际运行效果：
![系统运行效果图](https://github.com/zhihao-chen/QASystemOnMedicalGraph/blob/master/img/%E6%95%88%E6%9E%9C%E5%9B%BE.png)

# 项目运行方式

运行环境：Python3
数据库：neo4j
预训练词向量：[https://github.com/Embedding/Chinese-Word-Vectors](https://github.com/Embedding/Chinese-Word-Vectors)或https://pan.baidu.com/s/14JP1gD7hcmsWdSpTvA3vKA

1、搭建知识图谱：python build_grapy.py。大概几个小时，耐心等待。
2、启动问答测试：python kbqa_test.py

# 医疗知识图谱

数据源：39健康网。包括15项信息，其中7类实体，约3.7万实体，21万实体关系。

**本系统的知识图谱结构如下：**

![知识图谱结构](https://github.com/zhihao-chen/QASystemOnMedicalGraph/blob/master/img/%E7%9F%A5%E8%AF%86%E5%9B%BE%E8%B0%B1.png)

**1.1 知识图谱实体类型**

| 实体类型         | 中文含义 | 实体数量  | 举例          |
| ------------ | ---- | ----- | ----------- |
| Disease      | 疾病   | 14336 | 乙肝，癫痫       |
| Alias        | 别名   | 8877  | 小儿褐黄病综合征，广疮 |
| Symptom      | 症状   | 5622  | 手足烦热，四肢麻木   |
| Part         | 发病部位 | 82    | 手部，上肢       |
| Department   | 所属科室 | 82    | 感染科，外科      |
| Complication | 并发症  | 3201  | 落枕，流感       |
| Drug         | 药品   | 4625  | 西黄胶囊，司帕沙星   |
| Total        | 总计   | 36825 |             |

**1.2 知识图谱实体关系类型**

| 实体关系类型           | 中文含义  | 关系数量   | 举例              |
| ---------------- | ----- | ------ | --------------- |
| ALIAS_IS         | 别名是   | 52578  | 癫痫 别名是 羊角风      |
| HAS_SYMPTOM      | 症状有   | 62105  | 乙肝 症状有 肝功能异常    |
| PART_IS          | 发病部位是 | 26660  | 乙肝 发病部位是 肝      |
| DEPARTMENT_IS    | 所属科室是 | 33867  | 乙肝 所属科室是 传染科    |
| HAS_COMPLICATION | 并发症有  | 25183  | 乙肝 并发症有 肝硬化     |
| HAS_DRUG         | 可用药品  | 35914  | 乙肝 可用药品 恩替卡韦分散片 |
| TOTAL            | 总计    | 210018 | 约210018对关系      |

**1.3 知识图谱疾病属性**

| 疾病属性      | 中文含义 | 举例         |
| --------- | ---- | ---------- |
| age       | 发病人群 | 老人，小孩      |
| insurance | 是否医保 | 医保         |
| infection | 是否传染 | 有传染性       |
| checklist | 检查项目 | 肝功能检查      |
| treatment | 治疗方法 | 药物治疗、心理治疗  |
| period    | 治愈周期 | 一周         |
| rate      | 治愈率  | 0.1%       |
| money     | 费用   | 1000-2000元 |

# 问题意图识别

基于特征词分类的方法来识别用户查询意图

| 意图类型             | 中文含义     | 举例        |
| ---------------- | -------- | --------- |
| query_disease    | 查询疾病     | 肝肿大是什么病   |
| query_symptom    | 查询症状     | 慢性乙肝有什么表现 |
| query_cureway    | 查询治疗方案   | 肚子一直痛怎么办  |
| query_checklist  | 查询检查项目   | 乙肝需要做哪些检查 |
| query_department | 查询所属科室   | 乙肝去哪个科    |
| query_rate       | 查询治愈率    | 乙肝能治好吗    |
| query_period     | 查询治愈周期   | 乙肝多久能治好   |
| disease_describe | 查询疾病所以属性 | 慢性咽炎      |

# 总结

1、本项目构建简单，通过本项目能了解KBQA的工作流程。

2、本次通过手工标记210条意图分类训练数据，并采用朴素贝叶斯算法训练得到意图分类模型。其最佳测试效果的F1值达到了96.68%。选用NB的原因是通过与SVM训练效果比较后决定的。

3、不足之处：

- 训练数据还是太少，且对问题进行标注时易受主观意见影响。意图类别还是太少，本系统得到分类模型只能预测出上面设定的7类意图。(修改于2019.02.26)
- 对于问题句子中有多个意图的情况只能预测出一类，今后有时间再训练多标签模型吧。(最近在写论文，没时间)。
- 知识图谱太小了，对于许多问题都检索不出答案。今后可以爬取其它的健康网站数据或者利用命名实体识别和关系抽取技术从医学文献中抽取出实体与关系，以此来扩充知识图谱。
- 在本项目中采用了预训练的词向量来找近似词。由于该词向量特别大，加载非常耗时，因此影响了整个系统的效率。这个可能是因为电脑配置太低的原因吧。
- 没有实现推理的功能，后续将采用多轮对话的方式来理解用户的查询意图。同时将对检索出的结果进行排序，可靠度高的排在前面。

希望各位不吝赐教，任何建议请联系我。
邮箱：andrew_czh@163.com
