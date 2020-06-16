from pyecharts.charts import Bar    # 柱状图对象
from pyecharts import options  # 配置对象
from pyecharts.globals import ThemeType
# 创建柱状图对象
(Bar({'theme':ThemeType.DARK})
# 添加横坐标
.add_xaxis(["冰箱","洗衣机","彩电","空调","电脑","电饭煲"])
# 添加纵坐标（数据）可以添加多个
.add_yaxis("格力",[100,200,250,150,50,300],stack="strack")
.add_yaxis("小米",[200,100,50,150,240,180],stack="strack")
# 创建标题对象
.set_global_opts(title_opts=options.TitleOpts(title="家电销售情况"),
                 # visualmap_opts=options.VisualMapOpts(max_=200), # 设置阈值
                 datazoom_opts=[options.DataZoomOpts()], # 拉的进度条
                 brush_opts=options.BrushOpts(), # 工具栏
                 yaxis_opts=options.AxisOpts(name="y轴名字"),
                 xaxis_opts=options.AxisOpts(name="x轴名字"),
                 )
.render("家电柱状图.html")
)
