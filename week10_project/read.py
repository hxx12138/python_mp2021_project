with open('news_sohusite_xml.dat','rb') as f:
    sentences = f.readlines()
    print(len(sentences))
    count = 0
    for sentence in sentences:
        #print(str(sentence, encoding='gb18030'))
        count+=1
        if count > 100:
            break
