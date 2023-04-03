# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import hashlib
from pymongo import MongoClient


class JobparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client['vacancy_hw6']

    def process_item(self, item, spider):

        salary_dict = self.process_salary(item['salary'], spider)
        del item['salary']
        item['salary_min'] = salary_dict['min']
        item['salary_max'] = salary_dict['max']
        item['salary_currency'] = salary_dict['cur']
        item['city'] = self.process_city(item['city'])
        item['_id'] = self.process_id(item['url'])  # получаем хэш из ссылки

        collection = self.mongobase[spider.name]
        collection.insert_one(item)

        return item

    def process_salary(self, salary, spider):
        if spider.name == 'superjob':
            salary_dict = {'min': None, 'max': None, 'cur': None}

            if salary[0] != 'По договорённости':
                salary = ' '.join(salary)
                raw_salary = self.__pseudo_space_handling(salary.replace('\xa0', ' ')).\
                    replace(' — ', ' ').replace('вахта 45 дней', 'месяц').split()

                if len(raw_salary) == 2:
                    salary_dict['min'] = int(raw_salary[0])
                    salary_dict['max'] = int(raw_salary[0])
                    salary_dict['cur'] = raw_salary[1]
                else:
                    if raw_salary[0] == 'до':
                        salary_dict['max'] = int(raw_salary[1])
                    elif raw_salary[0] == 'от':
                        salary_dict['min'] = int(raw_salary[1])
                    else:
                        salary_dict['min'] = int(raw_salary[0])
                        salary_dict['max'] = int(raw_salary[1])
                    salary_dict['cur'] = raw_salary[2].split('/')[0]
                return salary_dict
            return salary_dict

        elif spider.name == 'hhru':
            salary = [x for x in salary if x not in [' ', 'на руки']]
            print(salary)
            salary_dict = {'min': None, 'max': None, 'cur': None}

            if len(salary) > 1:
                salary = ' '.join([s.strip() for s in salary])
                raw_salary = salary.replace(' – ', ' ').replace('\xa0', '').split()
                if len(raw_salary) == 5:
                    salary_dict['min'] = int(raw_salary[1])
                    salary_dict['max'] = int(raw_salary[3])
                    salary_dict['cur'] = ''.join(raw_salary[4:])
                else:
                    if raw_salary[0] == 'от':
                        salary_dict['min'] = int(raw_salary[1])
                        salary_dict['cur'] = ''.join(raw_salary[2:])
                    elif raw_salary[1] == 'до':
                        salary_dict['max'] = int(raw_salary[1])
                        salary_dict['cur'] = ''.join(raw_salary[2:])

            return salary_dict

    def process_city(self, city):
        return ', '.join(city)

    def process_id(self, url):
        return hashlib.sha224(url.encode()).hexdigest()[0:20]

    def __pseudo_space_handling(self, raw_salary):
        pseudo_space_indexes = []
        for i, letters in enumerate(zip(raw_salary[:-2], raw_salary[1:-1], raw_salary[2:])):
            x, y, z = letters
            if y == ' ' and x.isdigit() and z.isdigit():
                pseudo_space_indexes.append(i)
        temp = list(raw_salary)
        for ind in pseudo_space_indexes:
            temp[ind + 1] = '.'
        raw_salary = ''.join(temp).replace('.', '')
        return raw_salary