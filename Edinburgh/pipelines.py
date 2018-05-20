# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from Crawler.Edinburgh.Edinburgh import settings


class EdinburghPipeline(object):

    '''
    #链接数据库
    def __init__(self):
        self.connect = pymysql.connect(
            host = settings.Mysql_host,
            db = settings.Mysql_dbname,
            user = settings.Mysql_user,
            passwd = settings.Mysql_passwd
        )

        #通过游标对数据库进行操作
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        #定义sql语句
        #sql_1 = "create table {} (description, structure, learning_outcomes, career_opportunities, bachelor_requirements, language_requirements, application_deadlines, full_time_fee);"
        sql = "insert into {}(description, structure, learning_outcomes, career_opportunities, bachelor_requirements, language_requirements, application_deadlines, full_time_fee) values(%s,%s,%s,%s,%s,%s,%s,%s);"
        content = (item['description'],
                   item['structure'],
                   item['learning_outcomes'],
                   item['career_opportunities'],
                   item['bachelor_requirements'],
                   item['language_requirements'],
                   item['application_deadlines'],
                   item['full_time_fee'],)
        #执行sql语句
        self.cursor.execute(sql.format(input("输入表名:")),content)
        #提交sql语句
        self.connect.commit()
        return item
    '''

    #输出成txt文件
    def process_item(self, item, spider):
        #文件路径名可改变(下面是我电脑上的文件存放路径)
        file_name = '/Users/digger/anaconda3/lib/python3.6/site-packages/Crawler/Edinburgh/{}.txt'
        with open(file_name.format(input("请输入文件名:")),'a') as file:
            file.write(item['programme'] + '\n')
            file.write('Description:'+'\n'+item['description']+'\n\n')
            file.write('Compulsory_Courses:'+'\n'+item['Compulsory_Courses'] + '\n\n')
            file.write('Option_Courses:'+'\n'+item['Option_Courses'] + '\n\n')
            file.write('learning_outcomes:'+'\n'+item['learning_outcomes'] + '\n\n')
            file.write('career_opportunities:'+'\n'+item['career_opportunities'] + '\n\n')
            file.write('bachelor_requirements:'+'\n'+item['bachelor_requirements'] + '\n\n')
            file.write('language_requirements:'+'\n'+item['language_requirements'] + '\n\n')
            file.write('application_deadlines:'+'\n'+item['application_deadlines'] + '\n\n')
            file.write('full_time_fee:'+'\n'+item['full_time_fee'] + '\n\n')
            return item

