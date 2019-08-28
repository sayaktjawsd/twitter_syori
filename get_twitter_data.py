# coding: utf-8
import tweepy
import datetime

def get_twitter_data(keywortf,dfile):
    
    #Consumer key、アクセストークン
    Consumer_key = 'Ysx6a4A3cik7S7Eytu1UHUjXC'
    Consumer_secret = '50sN4jfa61ALkVxMHO6hcm7uDwP6f4UtFnYRhl67ul8Q5UEycA'
    Access_token = '860123973371150336-ia1floQCNDtn02F8z6vgIGadQ6pSSW0'
    Access_secret = '50HyVNKDv8qoFt21ZtoDdNvybE7g60Od6LTmGd2T8XjFU'

    #認証
    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(Access_token, Access_secret)
    
    api = tweepy.API(auth, wait_on_rate_limit = True)

    #検索キーワード
    q = keyword
    
    #ツイートを格納するリスト
    tweets_data =[]
    
    #カーソルを使用してデータを取得
    for tweet in tweepy.Cursor(api.search, q=q, count=100,tweet_mode='extended').items():

    #テキストを取得
        tweets_data.append(tweet.full_text + '\n')

    #出力ファイル名
    fname = r"'"+ dfile + "'"
    fname = fname.replace("'","")

    #出力
    with open(fname, "w",encoding="utf-8") as f:
        f.writelines(tweets_data)
    
if __name__ == '__main__':
    #検索キーワード入力(キーワード -RTでリツイート除外)
    print ('====== Enter Serch KeyWord   =====')
    keyword = input('>  ')
        
    #出力ファイル名入力
    print ('====== Enter Tweet Data file =====')
    dfile = input('>  ')
        
    get_twitter_data(keyword,dfile)
    
