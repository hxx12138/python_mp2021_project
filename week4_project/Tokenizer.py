import jieba

class Tokenizer:
    def __init__(self, chars, coding = 'c', PAD = 0):
        # 输入将要需要操作的文本（一个字符串的列表），
        #这里需要完成词典的构建（即汉字到正整数的唯一映射的确定）。注意构建词典一是要根据
        #coding来选择按词构建（coding='w')，还是按字构建，默认按字构建；PAD默认为0。
        #global match_dict,sentence_list,mode
        self.match_dict = {'[PAD]': PAD}
        self.sentence_list = chars
        self.mode = coding
        code = 1
        if coding == 'c':
            for sentence in chars:
                for word in sentence:
                    if word not in self.match_dict:
                        self.match_dict[word] = code
                        code += 1
        elif coding == 'w':
            for sentence in chars:
                words = jieba.lcut(sentence)
                for word in words:
                    if word not in self.match_dict:
                        self.match_dict[word] = code
                        code += 1
        #print(match_dict)
    def tokenize(self, sentence):
        #输入一句话，返回分词(字）后的字符列表(list_of_chars)。
        if self.mode == 'c':
            list_of_chars = list(sentence)
        else:
            list_of_chars = jieba.lcut(sentence)
        #print(list_of_chars)
        return list_of_chars
    def encode(self, list_of_chars):
        #输入字符(字或者词）的字符列表，返回转换后的数字列表(tokens)
        tokens = []
        for word in list_of_chars:
            tokens.append(self.match_dict[word])
        return tokens
    def trim(self, tokens, seq_len):
        #输入数字列表tokens，整理数字列表的长度。不足seq_len的
        #部分用PAD补足，超过的部分截断。
        if len(tokens) >= seq_len:
            tokens = tokens[:seq_len]
        else:
            end = [0 for i in range(seq_len-len(tokens))]
            tokens.extend(end)
        return tokens
    def decode(self, tokens):
        #将模型输出的数字列表翻译回句子。如果有PAD，输出'[PAD]'。
        sentence = ''
        for i in tokens:
            for key in self.match_dict:
                if self.match_dict[key] == i:
                    sentence+=key
        return sentence
    def get(self, seq_len):
        #返回所有文本（chars)的长度为seq_len的tokens。
        for sentence in self.sentence_list:
            if len(sentence) == seq_len:
                self.encode(self.tokenize(sentence))


if __name__ == '__main__':
    with open(r'jd_comments.txt','r',encoding='utf-8') as f:
        text_line = f.read()
        text_list = text_line.split('\n')
    t1 = Tokenizer(text_list, coding='c', PAD = 0 )
    list_of_chars = t1.tokenize(text_list[0])
    print(list_of_chars)
    tokens = t1.encode(list_of_chars)
    print(tokens)
    tokens = t1.trim(tokens, 10)
    print(tokens)
    sentence = t1.decode(tokens)
    print(sentence)
    tokens = t1.get(10)
    print(tokens)


