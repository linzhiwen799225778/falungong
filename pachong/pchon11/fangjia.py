import requests
from lxml import etree
from pyecharts.charts import Bar
from pyecharts import options
def get_city_money():
    url='https://www.maigoo.com/news/480610.html'
    res=requests.get(url).text
    ele=etree.HTML(res)
    city=ele.xpath('//table[@class="mod_table"]/tr/td[2]/text()')
    money=ele.xpath('//table[@class="mod_table"]/tr/td[4]/text()')
    return city[1:-1],money[1:-1]
(
    Bar()
    .add_xaxis(get_city_money()[0])
    .add_yaxis('价格',get_city_money()[1])
    .set_global_opts(title_opts=options.TitleOpts(title="各省房价"),
                 visualmap_opts=options.VisualMapOpts(max_=15000,min_=5000), # 设置阈值
                 datazoom_opts=[options.DataZoomOpts()], # 拉的进度条
                 brush_opts=options.BrushOpts(), # 工具栏
                 yaxis_opts=options.AxisOpts(name="均价"),
                 xaxis_opts=options.AxisOpts(name="城市"),)
    .render('房价.html')
)


