header = open('templates/header.html','rb').readlines()
content = open('../build/flaky.html','rb').readlines()
footer = open('templates/footer.html','rb').readlines()

resultant_text = header + content + footer

out_file=open('../flaky.html','wb')
out_file.writelines(resultant_text)
