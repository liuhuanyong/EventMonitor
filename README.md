# EventMonitor
Event monitor based on online news corpus  built by Baidu search enginee using event keyword  for event storyline and analysis，基于给定事件关键词，采集事件资讯，对事件进行挖掘和分析。 
# 项目路线图
 ![image](https://github.com/liuhuanyong/EventMonitor/blob/master/image/project.png)
# 项目细分
#　1)　基于话题关键词的话题历时语料库采集
执行方式：进入EventMonitor目录下，进入cmd窗口，执行"scrapy crawl eventspider -a keyword=话题关键词"，或者直接python crawl.py, 等待数秒后，既可以在news文件夹中存储相应的新闻文件．
如：
from scrapy import cmdline
projcet_name = 'eventspider'
event_list = ['江歌被害案', '红黄蓝幼儿园虐童','于欢杀死辱母者','白银连环杀人',
              '章莹颖失踪','杭州保姆纵火','榆林产妇坠楼','老虎咬人事件',
               '魏则西事件','雷洋涉“嫖娼”致死','如家酒店女子遇袭','罗一笑事件',
              '徐玉玉电信诈骗身亡']

for event in event_list:
    cmdline.execute("scrapy crawl {0} -a keyword={1}".format(projcet_name, event).split())
可以得到相应事件的话题集：
 ![image](https://github.com/liuhuanyong/EventMonitor/blob/master/image/topic.png)
 话题历史文本集：
 ![image](https://github.com/liuhuanyong/EventMonitor/blob/master/image/news.png)
文本内容：
标题:"辱母案"当事人姑妈:于欢刺人时 我正阻拦警察离开
发布时间:2017-03-26 07:48:31
正文:“于欢妈妈被那些人侮辱时，我看到了。他刺杀那些人，我没看见。因为我当时正在门口阻拦正准备离开的警察……”3月25日，在接受华西都市报-封面新闻记者电话采访时，于欢的姑妈于秀荣说。
于欢，山东聊城人，因犯故意伤害罪，2017年2月17日被山东聊城中级人民法院判处无期徒刑。华西都市报-封面新闻记者从该案一审判决书中看到，于欢持刀故意伤害四人，致一人送医不治死亡，两人重伤，一人轻伤。受害的四人系向其母亲讨债者。四人在讨债过程中，存在侮辱、打骂于欢母亲及其本人的行为。
该案经《南方周末》报道后，立即引发公众对聊城中院一审判决的讨论。华西都市报-封面新闻记者注意到，其中最大争议点系“于欢行为是否属正当防卫或防卫过当”。
案情回顾
引发争议的暴力催债
四次拨打110和市长热线
于欢今年22岁，其母亲苏银霞因经营工厂资金周转困难而向某地产公司老板吴学占借款，前后累计借款135万元，约定月息10%。此后陆续归还现金184万，以及一套价值70万的房屋抵债，还剩大约17万余款实在没有资金归还。因此，苏银霞遭受到暴力催债。
2016年4月14日，由社会闲散人员组成的10多人的催债队伍多次骚扰苏银霞的工厂，辱骂、殴打苏银霞。案发前一天，吴学占在苏已抵押的房子里，指使手下拉屎，将苏银霞按进马桶里，要求其还钱。当日下午，苏银霞四次拨打110和市长热线，但并没有得到帮助。
#　2)关于热点事件的情感分析
对于1)得到的历史语料，可以使用基于依存语义和情感词库的篇章级情感分析算法进行情感分析，这部分参考我的篇章级情感分析项目DocSentimentAnalysis：https://github.com/liuhuanyong/DocSentimentAnalysis
#　3)关于热点事件的搜索趋势
对于1)得到的历史语料，可以使用百度指数，新浪微博指数进行采集，这部分参考我的百度指数采集项目BaiduIndexSpyder：https://github.com/liuhuanyong/BaiduIndexSpyder，以及微博指数采集项目WeiboIndexSpyder：https://github.com/liuhuanyong/WeiboIndexSpyder
#　4)关于热点事件的话题分析
对于1)得到的历史语料，可以使用LDA,Kmeans模型进行话题分析，这部分参考我的话题分析项目Topicluster：https://github.com/liuhuanyong/TopicCluster
#　5)关于热点事件的代表性文本分析
对于1)得到的历史语料，可以使用跨篇章的textrank算法，对文本集的重要性进行计算和排序，这部分参考我的文本重要性分析项目ImportantEventExtractor：https://github.com/liuhuanyong/ImportantEventExtractor
#　6)关于热点事件新闻文本的图谱化展示
对于得到每个历史新闻事件文本，可以使用关键词，实体识别等关系抽取方法对文本进行可视化展示，这部分内容，参考我的文本内容可视化项目项目TopicGrapher：https://github.com/liuhuanyong/TextGrapher

# 结束语
关于事件监测的方法有很多，也有很多问题需要去解决，以上提出的方法只是一个尝试，就算法本身还有许多需要改进的地方