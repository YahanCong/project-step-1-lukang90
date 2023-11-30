import fruit
import pandas as pd


class PlantingRegion():
    areaType_list = ["market", "pick"]
    areaType = "market"

    def __init__(self, regionId, fruit_type_num, variety, area):
        self.regionId = regionId
        self.fruit_type_num = fruit_type_num
        self.variety = variety
        self.area = area

    def get_area_type(self):
        return PlantingRegion.areaType

    def set_area_type(self, areaType):
        if areaType in PlantingRegion.areaType_list:
            self.__areaType = areaType
        else:
            print("Invalid area type")

    def get_area(self):
        return self.area

    def get_fruit(self):
        return self.fruit

def set_picking_region(plantingRegion):
    plantingRegion.set_area_type("pick")


# 查询特定果种的种植面积（type_num + variety都需要用到）
def area_account_variety(plantation_list, fruit):
    fruit_type_num = fruit.get_type_num()
    fruit_variety = fruit.variety
    area_sum = 0

    for region in plantation_list:
        f = region.get_fruit()
        f_type_num = f.get_type_num()
        f_variety = f.variety

        if f_type_num == fruit_type_num and fruit_variety == f_variety:
            area_sum += region.area
    return area_sum


#所有水果+种类汇总
# 还在改
# {(apple, apple_variety): picking_area, marketing_area}
# {"1_variety": picking_area, marking_area}
# method返回时把name跟variety合并成string传过去
# 传过去一个dataframe
# 这里要配合一个region_class_list 使用
def area_summary(region_list):
    fruit_list = fruit.fruit_class_load()
    area_dict_pick = {}
    area_dict_market = {}

    for f in fruit_list:
        fruit_type_num = f.get_type_num()
        variety = f.variety
        f_name = str(fruit_type_num) + " " + variety

        for r in region_list:
            region_type = r.get_area_type()
            if region_type == "pick":
                if r.fruit_type_num == fruit_type_num and r.variety == variety:
                    try:
                        area_dict_pick[f_name] += r.area
                    except KeyError:
                        area_dict_pick[f_name] = r.area
            elif region_type == "market":
                if r.fruit_type_num == fruit_type_num and r.variety == variety:
                    try:
                        area_dict_market[f_name] += r.area
                    except KeyError:
                        area_dict_market[f_name] = r.area
            else:
                print("Invalid region type")
    df_area_pick = pd.DataFrame(area_dict_pick, index= ["pick"])
    df_area_market = pd.DataFrame(area_dict_market, index= ["market"])
    df_area = pd.concat([df_area_pick, df_area_market], axis=1)
    df_area = df_area.fillna(0)
    df_area = df_area.transpose()
    return df_area


















# 用dataframe储存regions
# 这个还要再修改
# 感觉好像不如
def region_saving(region_list):
    data_region = region_loading()

    region_info_list = []
    for r in region_list:
        regionId = r.regionId
        fruit_type_num = r.fruit_type_num
        fruit_variety = r.variety
        area_type = r.get_area_type()
        area = r.area

        region_info = [regionId, fruit_type_num,fruit_variety, area, area_type]
        region_info_list.append(region_info)

    temp_df = pd.DataFrame(region_info_list, columns=data_region.columns)
    data_region = temp_df

    data_region.to_csv('plantations.csv', index=False)
    print("successful save")


# 提取csv文件，转化成dataframe
def region_loading():
    try:
        data_region = pd.read_csv("plantations.csv")
    except FileNotFoundError:
        title_list = ["regionId", "fruit_type_num","fruit_variety", "area_type", "area"]
        data_region = pd.DataFrame(columns=title_list)
    return data_region


# # 把读取的csv文件转换成class
# def region_class_tranfer(data_region):




















































































