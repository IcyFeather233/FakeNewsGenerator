from models import News

data = {'author': "cmz", 'type': '12', 'topic': 'sda', 'time': 'asd', 'position': 'dsf', 'members': 'ss'}
"{'author': \"cmz\", 'type': '12', 'topic': 'sda', 'time': 'asd', 'position': 'dsf', 'members': 'ss'}"
print(data['author'])
print(data['type'])

news = News(data)
print(news.content)