import codecs
with codecs.open("events.html", "r",'utf-8') as fin:
    with codecs.open("events2.html", "w",'utf-8') as fout:
        for line in fin:
            fout.write(line.replace("&lt;","<").replace("&gt;",">"))

fout.close()
