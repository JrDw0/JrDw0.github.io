#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
with open('love.txt','r',encoding='utf-8') as f:
    result = re.findall('(?:\:)(.+)',f.read())

for i in result:
    print('''  <div class="love">
    <div class="love_horizontal">
      <div class="love_vertical">
        <div class="love_word">%s</div>
      </div>
    </div>
  </div>'''%(i))

