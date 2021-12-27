import os
import json
import sys
import os
import random
from django.db import models

# Create your models here.

# 定义一个forms类，用于接收表单数据

class News:
    def __init__(self, form):
        self.author = form['author']
        self.type = form['type']
        self.topic = form['topic']
        self.time = form['time']
        self.position = form['position']
        self.members = form['members']

    def gen(self):
        dirpath = os.path.dirname(os.path.abspath(__file__)) + '\\Data'
        # Open json data file
        with open(os.path.join(dirpath, self.type, 'data.json'), encoding='utf-8') as f:
            data = json.load(f)
            # Randomly load one passage
            passage = [data['intro'][random.randint(0, len(data['intro']) - 1)],
                       data['body'][random.randint(0, len(data['body']) - 1)],
                       data['end'][random.randint(0, len(data['end']) - 1)]]
            # Replace args
        context = []
        for seg in passage:
            seg = seg.replace("#DATE#", self.time)
            while True:
                oldSeg = seg
                seg = seg.replace('#NAME#', self.members)
                if oldSeg == seg:
                    break
            seg = seg.replace("#TOPIC#", self.topic)
            seg = seg.replace("#POSITION#", self.position)

            context.append(seg)

        content = ''
        for each in context:
            content += each
        return content

    content = "success!"

