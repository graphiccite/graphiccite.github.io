start = open("start.txt","r").read()
middle = open("url_file.txt","r").read()
end = open("end.txt","r").read()

f = open('altmetric_results.html','w')
f.write(str(start))
f.write(str(middle))
f.write(str(end))
f.close()
