# Author: Laurel Miller
from collections import Counter


class GrabData:
    def __init__(self, driver):
        self.driver = driver

    def row_data(self):
        table = self.driver.find_element_by_id('serverSideDataTable')
        assert 'no such name' not in self.driver.page_source
        row_number = 0
        while row_number < 101:
            row = table.find_elements_by_xpath('//tr[' + str(row_number) + ']/td')
            rData = []
            for text in row:
                rData.append(text.text)
            row_number += 1
            return rData

    def find_model(self):
        table = self.driver.find_element_by_id('serverSideDataTable')
        assert 'no such name' not in self.driver.page_source
        column = table.find_elements_by_xpath('//tr/td[6]')
        col = []
        for model in column:
            col.append(model.text)
        return col

    def find_damages(self):
        table = self.driver.find_element_by_id('serverSideDataTable')
        assert 'no such name' not in self.driver.page_source
        column_12 = table.find_elements_by_xpath('//tr/td[12]')
        damage = []
        for damg in column_12:
            damage.append(damg.text)
        return damage

    def count_damage(self):
        def rear_end():
            rear = []
            rear.append(1)

        def front_end():
            front = []
            front.append(2)

        def minor():
            minor = []
            minor.append(3)

        def under():
            under = []
            under.append(4)

        switcher = {
            'REAR END': rear_end,
            'FRONT END': front_end,
            'MINOR DENT/SCRATCHES': minor,
            'UNDERCARRIAGE': under
        }

        p = '\n Types and Number of Damage:'
        print(p)
        print('*' * len(p + '*'))
        damage = self.find_damages()
        damage_count = Counter(damage)
        misc = []
        for damages in damage_count:
            dmg = (damages.title(), damage_count[damages])
            if damages in switcher:
                print('  ', dmg)
            else:
                misc.append(damage_count[damages])
        print('   (\'Misc\',', sum(misc), ')')


    def count(self):
        p = ' Number of Exotic Models:'
        print(p)
        print('*' * len(p + '*'))
        cars = self.find_model()
        car_count = Counter(cars)
        for car in car_count:
            print('  ', car.title(), '=', car_count[car], )

    def models_count(self):
        self.row_data()
        self.find_model()
        self.count()

    def damages_count(self):
        self.row_data()
        self.count_damage()




