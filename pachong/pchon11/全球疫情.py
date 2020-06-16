import requests
import json
def get_canshu():
    url='https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
    res0=requests.get(url).text
    res1=json.loads(res0)['data']
    names=[]
    confirms=[]
    for i in res1:
        name=i['name']
        confirm=i['confirm']
        names.append(name)
        confirms.append(confirm)
    return names,confirms
# print(get_canshu())
# 3d世界地图
# import pyecharts.options as opts
# from pyecharts.charts import MapGlobe
# datas=zip(get_canshu()[0],get_canshu()[1])
# data = get_canshu()[1]
# print(data)
# low, high = min(data), max(data)
# print(low,high)
# c = (
#     MapGlobe()
#     .add_schema()
#     .add(
#         maptype="world",
#         series_name="World Population",
#         data_pair=datas,
#         is_map_symbol_show=True,
#         label_opts=opts.LabelOpts(is_show=True),
#     )
#     .set_global_opts(
#         visualmap_opts=opts.VisualMapOpts(
#             min_=low,
#             max_=high,
#             range_text=["max", "min"],
#             is_calculable=True,
#             range_color=["blue", "yellow", "orangered"],
#         )
#     )
#     .render("map_globe_base.html")
# )
from pyecharts import options as opts
from pyecharts.charts import Map
zip(get_canshu()[0],get_canshu()[1])
print(get_canshu()[0])
c = (
    Map()
    .add("商家A", [list(z) for z in zip(get_canshu()[0],get_canshu()[1])], "world")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-世界地图"),
        visualmap_opts=opts.VisualMapOpts(max_=7000),
    )
    .render("map_world.html")
)


