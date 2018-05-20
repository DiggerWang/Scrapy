# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from Crawler.Edinburgh.Edinburgh.items import EdinburghItem
from  scrapy.loader import ItemLoader


class EdinburghSpider(scrapy.Spider):
    name = 'Edinburgh'
    allowed_domains = ['www.ed.ac.uk'] #域名务必取掉http
    start_urls = ['https://www.ed.ac.uk/studying/postgraduate/degrees']

    def parse(self, response):
        name = []
        num = []
        url = []

        for i in range(1,23):
            name += response.xpath('//*[@id="proxy_leftSubjects"]/div/a['+str(i)+']/text()').extract()
            name.remove('\n\t')
            num += response.xpath('//*[@id="proxy_leftSubjects"]/div/a['+str(i)+']/span/text()').extract()
            url += response.xpath('//*[@id="proxy_leftSubjects"]/div/a['+str(i)+']/@href').extract()

        for i in range(1,22):
            name += response.xpath('//*[@id="proxy_rightSubjects"]/div/a['+str(i)+']/text()').extract()
            name.remove('\n\t')
            num += response.xpath('//*[@id="proxy_rightSubjects"]/div/a['+str(i)+']/span/text()').extract()
            url += response.xpath('//*[@id="proxy_rightSubjects"]/div/a['+str(i)+']/@href').extract()

        for i in name:
            print(str(name.index(i)+1)+"."+i)
        input_name = input("输入你想要查询的学位:")

        if input_name.isdigit(): #判断input_name是否为数字
            input_name = name[int(input_name)-1]
        else:
            input_name = " " + input_name

        def get_url(input_name):
            for i in name:
                if i == input_name:
                    url_to = "https://www.ed.ac.uk" + url[name.index(i)]
            return url_to

        yield scrapy.Request(url = get_url(input_name), callback=self.ShowProgramme)

    #查看项目信息
    def ShowProgramme(self, response):
        type_1 = response.xpath('//*[@id="proxy_leftContent"]/div[1]/div[1]/h2/text()').extract()
        type_2 = response.xpath('//*[@id="proxy_leftContent"]/div[1]/div[2]/h2/text()').extract()
        type_3 = 'Basci Degree'
        type_4 = response.xpath('//*[@id="proxy_leftContent"]/h2/text()').extract()

        list_1 = response.xpath('//*[@id="proxy_leftContent"]/div[1]/div[1]/div/a/text()').extract()
        list_2 = response.xpath('//*[@id="proxy_leftContent"]/div[1]/div[2]/div/a/text()').extract()
        list_3 = response.xpath('//*[@id="proxy_leftContent"]/div[2]/div[1]/div/a/text()').extract()
        list_4 = response.xpath('//*[@id="proxy_leftContent"]/div[2]/div[2]/div/a/text()').extract()

        i = 0
        while i < len(list_1):
            if len(list_1[i]) <= 7:
                list_1.remove(list_1[i])
                i -= 1
            i += 1
        i = 0
        while i < len(list_2):
            if len(list_2[i]) <= 7:
                list_2.remove(list_2[i])
                i -= 1
            i += 1
        i = 0
        while i < len(list_3):
            if len(list_3[i]) <= 7:
                list_3.remove(list_3[i])
                i -= 1
            i += 1
        i = 0
        while i < len(list_4):
            if len(list_4[i]) <= 7:
                list_4.remove(list_4[i])
                i -= 1
            i += 1
        len_1 = len(list_1)
        len_2 = len(list_2)
        len_3 = len(list_3)
        len_4 = len(list_4)

        item_1 = []
        item_2 = []
        item_3 = []
        item_4 = []
        item_5 = []
        item_6 = []
        item_7 = []
        item_8 = []
        pro_1 = []
        pro_2 = []
        pro_3 = []
        pro_4 = []
        url_1 = []
        url_2 = []
        url_3 = []
        url_4 = []
        for i in range(len_1):
            item_1 += response.xpath('//*[@id="proxy_leftContent"]/div[1]/div[1]/div/a['+str(i+1)+']/text()').extract()
            item_3 += response.xpath('//*[@id="proxy_leftContent"]/div[1]/div[1]/div/a['+str(i+1)+']/span/text()').extract()
            url_1 += response.xpath('//*[@id="proxy_leftContent"]/div[1]/div[1]/div/a['+str(i+1)+']/@href').extract()

        for i in range(len_3):
            item_5 += response.xpath('//*[@id="proxy_leftContent"]/div[2]/div[1]/div/a['+str(i+1)+']/text()').extract()
            item_7 += response.xpath('//*[@id="proxy_leftContent"]/div[2]/div[1]/div/a['+str(i+1)+']/span/text()').extract()
            url_3 += response.xpath('//*[@id="proxy_leftContent"]/div[2]/div[1]/div/a['+str(i+1)+']/@href').extract()

        i = 0
        while i < len(item_1):
            if len(item_1[i]) <= 7:
                item_1.remove(item_1[i])
                i -= 1
            i += 1
        i = 0
        while i < len(item_3):
            if len(item_3[i]) <= 7:
                item_3.remove(item_3[i])
                i -= 1
            i += 1
        i = 0
        while i < len(item_5):
            if len(item_5[i]) <= 7:
                item_5.remove(item_5[i])
                i -= 1
            i += 1
        i = 0
        while i < len(item_7):
            if len(item_7[i]) <= 7:
                item_7.remove(item_7[i])
                i -= 1
            i += 1

        for i in range(len(item_1)):
            pro_1.append((item_1[i],item_3[i]))
        for i in range(len(item_5)):
            pro_3.append((item_5[i],item_7[i]))

        for i in range(len_2):
            item_2 += response.xpath('//*[@id="proxy_leftContent"]/div[1]/div[2]/div/a['+str(i+1)+']/text()').extract()
            item_4 += response.xpath('//*[@id="proxy_leftContent"]/div[1]/div[2]/div/a['+str(i+1)+']/span/text()').extract()
            url_2 += response.xpath('//*[@id="proxy_leftContent"]/div[1]/div[2]/div/a['+str(i+1)+']/@href').extract()

        for i in range(len_4):
            item_6 += response.xpath('//*[@id="proxy_leftContent"]/div[2]/div[2]/div/a['+str(i+1)+']/text()').extract()
            item_8 += response.xpath('//*[@id="proxy_leftContent"]/div[2]/div[2]/div/a['+str(i+1)+']/span/text()').extract()
            url_4 += response.xpath('//*[@id="proxy_leftContent"]/div[2]/div[2]/div/a['+str(i+1)+']/@href').extract()

        i = 0
        while i < len(item_2):
            if len(item_2[i]) <= 7:
                item_2.remove(item_2[i])
                i -= 1
            i += 1
        i = 0
        while i < len(item_4):
            if len(item_4[i]) <= 7:
                item_4.remove(item_4[i])
                i -= 1
            i += 1
        i = 0
        while i < len(item_6):
            if len(item_6[i]) <= 7:
                item_6.remove(item_6[i])
                i -= 1
            i += 1
        i = 0
        while i < len(item_8):
            if len(item_8[i]) <= 7:
                item_8.remove(item_8[i])
                i -= 1
            i += 1

        for i in range(len(item_2)):
            pro_2.append((item_2[i],item_4[i]))
        for i in range(len(item_6)):
            pro_4.append((item_6[i], item_8[i]))

        print('1.'+''.join(type_3)+'\n'+'2.'+''.join(type_4))
        input_1 = input("输入你想要查询的模块:")

        print('1.'+''.join(type_1)+'\n'+'2.'+''.join(type_2))
        input_2 = input("输入你想要查询的项目:")

        if input_1 == '1':
            if input_2 == '1':
                for i in range(len(pro_1)):
                    print(str(i+1),end='.')
                    print(pro_1[i])
            elif input_2 == '2':
                for i in range(len(pro_2)):
                    print(str(i + 1), end='.')
                    print(pro_2[i])
        if input_1 == '2':
            if input_2 == '1':
                for i in range(len(pro_3)):
                    print(str(i + 1), end='.')
                    print(pro_3[i])
            elif input_2 == '2':
                for i in range(len(pro_4)):
                    print(str(i + 1), end='.')
                    print(pro_4[i])

        x = input("输入你感兴趣的具体专业:")

        item = EdinburghItem()
        def get_url(input):
            if input_1 == '1':
                if input_2 == '1':
                    item['programme'] = pro_1[int(x) - 1][0]+pro_1[int(x) - 1][1]
                    return 'https://www.ed.ac.uk'+url_1[int(x)-1]
                elif input_2 == '2':
                    item['programme'] = pro_2[int(x) - 1][0]+pro_2[int(x) - 1][1]
                    return 'https://www.ed.ac.uk'+url_2[int(x)-1]
            if input_1 == '2':
                if input_2 == '1':
                    item['programme'] = pro_3[int(x) - 1][0]+pro_3[int(x) - 1][1]
                    return 'https://www.ed.ac.uk'+url_3[int(x)-1]
                elif input_2 == '2':
                    item['programme'] = pro_4[int(x) - 1][0]+pro_4[int(x) - 1][1]
                    return 'https://www.ed.ac.uk'+url_4[int(x)-1]

        yield scrapy.Request(url = get_url(input), meta = {'item':item}, callback=self.Information)


    #获取每个专业的信息，并用item储存
    def Information(self,response):
        #定义itemloader
        itemloader = ItemLoader(item=response.meta['item'], response=response)

        c_name = ''
        o_name = ''
        #item = EdinburghItem()
        description = response.xpath('//*[@id="proxy_collapseprogramme"]/div/p/text()').extract()
        #将description逐个加入容器中
        for i in range(len(description)):
            itemloader.add_value('description',description[i])

        c_cource = response.xpath('//*[@id="proxy_collapsehow_taught"]/div/ul[1]/li/text()').extract()
        o_cource = response.xpath('//*[@id="proxy_collapsehow_taught"]/div/ul[2]/li/text()').extract()
        #将课程信息加入容器
        if len(c_cource): #判断list是否为空
            for i in c_cource:
                itemloader.add_value('Compulsory_Courses',i)
        else:
             itemloader.add_value('Compulsory_Courses','No compulsory courses')
        if len(o_cource):
            for i in o_cource:
                itemloader.add_value('Option_Courses',i)
        else:
            itemloader.add_value('Option_Courses','No option courses')


        learning_outcomes = response.xpath('//*[@id="proxy_collapselearning_outcomes"]/div/ul/li/text()').extract()
        if len(learning_outcomes):
            for i in learning_outcomes:
                itemloader.add_value('learning_outcomes',i)
        else:
            itemloader.add_value('learning_outcomes','None')

        career_opportunities = response.xpath('//*[@id="proxy_collapsecareer_opp"]/div/p/text()').extract()
        if len(career_opportunities):
            for i in career_opportunities:
                itemloader.add_value('career_opportunities',i)
        else:
            itemloader.add_value('career_opportunities','None')

        bachelor_requirements = response.xpath('//*[@id="proxy_collapseentry_req"]/div/p/text()').extract()
        if len(bachelor_requirements):
            for i in bachelor_requirements:
                itemloader.add_value('bachelor_requirements',i)
        else:
            itemloader.add_value('bachelor_requirements','None')

        language_requirements = response.xpath('//*[@id="proxy_collapseentry_req"]/div/ul[2]/li/text()').extract()[1:4]

        for i in range(len(language_requirements)):
            x = response.xpath('//*[@id="proxy_collapseentry_req"]/div/ul[2]/li['+str(i+2)+']/abbr/text()').extract()
            language_requirements[i] = ''.join(x)+language_requirements[i]
            itemloader.add_value('language_requirements',language_requirements[i])

        application_deadlines = response.xpath('//*[@id="proxy_collapseDeadlines"]/div/p/text()').extract()
        for i in application_deadlines:
            itemloader.add_value('application_deadlines',i)

        fee_url = response.xpath('//*[@id="proxy_collapsefees"]/div/ul[1]/li/a/@href').extract()

        item = itemloader.load_item()

        yield scrapy.Request(url = fee_url[0], meta = {'item':item}, callback=self.Getfee) #meta将上述的item传递给回掉函数

    #获取学费信息
    def Getfee(self,response):
        itemloader = ItemLoader(item=response.meta['item'], response=response)
        fee_type = response.xpath('//*[@id="block-system-main"]/table/tr[1]/th/text()').extract()
        fee = response.xpath('//*[@id="block-system-main"]/table/tr[2]/td/text()').extract()
        while len(fee)<len(fee_type):
            fee += ['']
        for i in range(len(fee_type)):
            itemloader.add_value('full_time_fee',fee_type[i]+':'+fee[i])

        item = itemloader.load_item()
        yield item