from bs4 import BeautifulSoup

with open('yellow_pages_project/data.html','r') as file:
    data = file.read()

d = {}
i = 0

soup = BeautifulSoup(data,'lxml')

elems = soup.select('div.eachPopular')
for elem in elems:
    name = elem.select_one('a.eachPopularTitle.hasOtherInfo').text
    rating = elem.select_one('div.eachPopularRatingBlock').span.get('class')[-1].split('-')[0].strip('r')
    num_reviews = elem.select_one('a.ratingCount').text.split()[0]
    try:
        tags = elem.select_one('ul.eachPopularTagsList').select('li')
        tag = ''
        for _ in tags:
            tag += _.select_one('a').text + ', '
        tag = tag.strip(' ,')
    except:
        tag = 'no tags'
    phone = elem.select_one('a.businessContact').text
    location = elem.select_one('address.businessArea').strong.text
    try:
        email = elem.select_one('div.eachPopularLink').a.get('href').split(':')[1]
    except:
        email = 'not mentioned'
    
    d[i] = [name,rating,num_reviews,tag,phone,location,email]
    i += 1

with open('yellow_pages_project/result.csv','w',encoding='utf-8',newline='') as file:
    import csv
    writer = csv.writer(file)
    writer.writerow(['name','rating','number of rating','tags','phone number','location','email'])
    for i in d:
        writer.writerow(d[i])
        