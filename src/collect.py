#!/usr/bin/env python

import markdown2
import pystache


title = 'flaky'

mdSrc = open('texts/'+title+'.md', 'rb').read()
content = markdown2.markdown(mdSrc).encode('ascii', 'ignore')
content = content.replace('[', '</p><center><div lang="latex">')
content = content.replace('<code>', '<code> \n')
content = content.replace(']', '</div></center><br><p>')

header = [pystache.render(each_line, {'title': title, 'full_title': content.split('\n')[0][4:-5]}) for each_line in open('templates/header.html', 'rb').readlines()]
footer = open('templates/footer.html', 'rb').readlines()




resultant_text = header + content.split('\n') + footer

out_file = open('../'+title+'.html', 'wb')
for each_line in resultant_text:
    out_file.write(each_line+'\n')
