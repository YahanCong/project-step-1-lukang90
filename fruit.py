import csv
from datetime import datetime
from abc import ABCMeta, abstractmethod


class Fruit(metaclass=ABCMeta):
    # 品种，大小，酸度，甜度，口感（e.g. crunchy), 用途
    def __init__(self, variety, size, sweet, sour, taste, price, use):
        self.variety = variety
        self.size = size
        self.sweet = sweet
        self.sour = sour
        self.taste = taste
        self.__price = price
        self.use = use

    def describe(self):
        describe_sentence = (f"{self.variety},{self.size}, {self.sour}, {self.sweet}, {self.taste}." +
                             f"It is good for {self.use}")
        return describe_sentence

    def __str__(self):
        return Fruit.describe(self)

    def get_price(self):
        return self.__price

    @property
    def set_price(self, price):
        self.__price = price

    @abstractmethod
    def get_type_num(self):
        pass

    @abstractmethod
    def get_available_season(self, date):
        pass

class Apple(Fruit):
    type_num = 1
    season_dict = {"Ambrosia": [9,10],
                   "Gala": [8,9,10],
                   "Honeycrisp": [9,10]}

    def __init__(self, variety, size, sweet, sour, taste, price, use):
        Fruit.__init__(self, variety, size, sweet, sour, taste, price, use)

    def get_type_num(self):
        return Apple.type_num

    def get_available_season(self, date):
        season_list = Apple.season_dict[self.variety]
        if date in season_list:
            print(f"{self.variety} Apple is available now")
            return True
        elif date < min(season_list):
            print(f"Sorry, {self.variety} Apple is not ripe now.")
            return False
        else:
            print(f"Sorry, {self.variety} Apple season has ended.")
            return False


class Cherry(Fruit):
    type_num = 2
    season_dict = {"Lapins": [6,7],
                   "Sweetheart": [6,7],
                   "Skeena": [7,8]}

    def __init__(self, variety, size, sweet, sour, taste, price, use):
        Fruit.__init__(self, variety, size, sweet, sour, taste, price, use)

    def get_type_num(self):
        return Cherry.type_num

    def get_available_season(self, date):
        season_list = Cherry.season_dict[self.variety]
        if date in season_list:
            print(f"{self.variety} Cherry is available now")
            return True
        elif date < min(season_list):
            print(f"Sorry, {self.variety} Cherry is not ripe now.")
            return False
        else:
            print(f"Sorry, {self.variety} Cherry season has ended.")
            return False


class Peach(Fruit):
    type_num = 3
    season_dict = {"Redhaven": [7, 8],
                   "Elberta": [8, 9],
                   "Cresthaven": [8, 9]}

    def __init__(self, variety, size, sweet, sour, taste, price, use):
        Fruit.__init__(self, variety, size, sweet, sour, taste, price, use)

    def get_type_num(self):
        return Peach.type_num

    def get_available_season(self, date):
        season_list = Peach.season_dict[self.variety]
        if date in season_list:
            print(f"{self.variety} Peach is available now")
            return True
        elif date < min(season_list):
            print(f"Sorry, {self.variety} Peach is not ripe now.")
            return False
        else:
            print(f"Sorry, {self.variety} Peach season has ended.")
            return False



# 辅助method: 把按照'YYYY-MM-DD'输入的日期转换成月份
def datetime_transfer(date):
    try:
        if isinstance(date, str):
            # data_string formate 'YYYY-MM-DD'
            date = datetime.strptime(date, '%Y-%m-%d')
        month = date.month
        return month
    except:
        print("Invalid datetime")


# 检查输入的特定水果是否应季
def fruit_available_check(date, fruit):
    month = datetime_transfer(date)
    return fruit.get_available_season(month)


# 检查所有水果中哪些应季, 返回list of fruit
def available_season_fruit(date,fruit_list):
    month = datetime_transfer(date)
    available_list = []
    for f in fruit_list:
        variety = f.variety
        fruit_season = f.season_dict[variety]
        season_list = f.season_dict[variety]
        if month in season_list:
            available_list.append(f)
    return available_list


#水果价格计算
def fruit_selling_price(fruit, weight, discount = 1):
    fruit_price = fruit.get_price()*discount
    fee = fruit_price * weight
    return fee


# 辅助method,将需要储存的数据传入csv文件中
def file_store(file_path, store_data):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # # 写入标题
        # writer.writerow(title_list)
        # 写入数据
        writer.writerows(store_data)


# 储存水果信息，方便之后调用
def fruit_information_store(fruit_list):
    csv_file_path = "fruits.csv"
    #title_list = ["type_num", "variety", "size", "sweet", "sour", "taste", "price", "use"]

    fruit_info_list = []
    for fruit in fruit_list:
        type_num = fruit.get_type_num()
        variety = fruit.variety
        size = fruit.size
        sweet = fruit.sweet
        sour = fruit.sour
        taste = fruit.taste
        price = round(fruit.get_price(),2)
        use = fruit.use

        fruit_info = tuple([type_num, variety, size, sweet, sour, taste, price, use])
        fruit_info_list.append(fruit_info)
    #file_store(csv_file_path, title_list, fruit_info_list)
    file_store(csv_file_path, fruit_info_list)

# 辅助method: file load
def file_load(file_path):
    file_rows = []
    try:
        with open(file_path, "r") as infile:
            for line in infile:
                line = line.strip(" \n")
                fields = line.split(",")
                for i in range(0, len(fields)):
                    fields[i] = fields[i].strip()
                file_rows.append(fields)
        return file_rows
    except FileNotFoundError:
        print(f"There is no file {file_path}")


def fruit_class_load():
    fruit_file = "fruits.csv"
    file_rows = file_load(fruit_file)
    fruit_list = []
    for row in file_rows:
        fruit = None
        # title_list = ["type_num", "variety", "size", "sweet", "sour", "taste", "price", "use"]
        type_num = int(row[0])
        variety = row[1]
        size = row[2]
        sweet = row[3]
        sour = row[4]
        taste = row[5]
        price = float(row[6])
        use = row[7]

        if type_num == 1:
            fruit = Apple(variety, size, sweet, sour, taste, price, use)
        elif type_num == 2:
            fruit = Cherry(variety, size, sweet, sour, taste, price, use)
        elif type_num == 3:
            fruit = Peach(variety, size, sweet, sour, taste, price, use)
        else:
            print("These is not a valid fruit type num, please check your file content")
        fruit_list.append(fruit)
    return fruit_list


































