# coding:utf-8
import MeCab
import matplotlib.pyplot as plt
import csv
import collections

def analyze_tweet(dfile,ofile):
    
    #読み込みファイル名
    fname = r"'"+ dfile + "'"
    fname = fname.replace("'","")
    
    #Mecabを使用して形態素解析
    mecab = MeCab.Tagger("-Ochasen")
    
    #単語を格納するリスト(名詞、動詞、形容詞、副詞)
    words=[]
    
    #ファイル読み込み
    with open(fname, 'r',encoding='utf-8') as f:
        reader = f.readline()
        
        while reader:
            #Mecabで形態素解析
            node = mecab.parseToNode(reader)
            
            while node:
                word_type = node.feature.split(",")[0]
                
                #取得する単語は、"名詞","動詞","形容詞","副詞"
                if word_type in ["名詞","動詞","形容詞","副詞"]:
                    words.append(node.surface)
                
                node = node.next       
            reader = f.readline()
    w = collections.Counter(words)
    words_count=w.most_common()
    #print(words_count)

    word_co_list=[]

    for w in words_count:
        word_co_list.append(list(w))
        
    #出力ファイル名

    with open(ofile,mode='w',encoding='utf-8') as f:
        for w in words_count:
            for s in w:
                f.write(str(s))
            f.write('\n')

    #ストップワードの設定
    #stop_words = ['http']
if __name__ == '__main__':
    print ('====== Enter Tweet Data file =====')
    dfile = input('> ')
    
    print('===== Enter Output Data file name =====')
    ofile = input('> ')
    analyze_tweet(dfile,ofile)



