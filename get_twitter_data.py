# coding: utf-8
import tweepy
import datetime

def get_twitter_data(keywortf,dfile):
    
    #Python��API�𗘗p���邽�߂̃L�[�A�A�N�Z�X�g�[�N��
    Consumer_key = 'Ysx6a4A3cik7S7Eytu1UHUjXC'
    Consumer_secret = '50sN4jfa61ALkVxMHO6hcm7uDwP6f4UtFnYRhl67ul8Q5UEycA'
    Access_token = '860123973371150336-ia1floQCNDtn02F8z6vgIGadQ6pSSW0'
    Access_secret = '50HyVNKDv8qoFt21ZtoDdNvybE7g60Od6LTmGd2T8XjFU'

    #�F��
    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(Access_token, Access_secret)
    
    api = tweepy.API(auth, wait_on_rate_limit = True)

    #�����L�[���[�h�ݒ� 
    q = keyword
    
    #�Ԃ₫���i�[���郊�X�g
    tweets_data =[]
    
    #�J�[�\�����g�p���ăf�[�^�擾
    for tweet in tweepy.Cursor(api.search, q=q, count=100,tweet_mode='extended').items():
    
    #�Ԃ₫���Ԃ�UTC�̂��߁AJST�ɕϊ�  ���f�o�b�N�p�̃R�[�h
    #jsttime = tweet.created_at + datetime.timedelta(hours=9)
    #print(jsttime)

    #�Ԃ₫�e�L�X�g�iFULL) ���擾
        tweets_data.append(tweet.full_text + '\n')

    #�o�̓t�@�C����
    fname = r"'"+ dfile + "'"
    fname = fname.replace("'","")

    #�t�@�C���o�� 
    with open(fname, "w",encoding="utf-8") as f:
        f.writelines(tweets_data)
    
if __name__ == '__main__':
    #�����L�[���[�h�����  �����c�C�[�g�����O����ꍇ �u�L�[���[�h -RT �v�Ɠ���
    print ('====== Enter Serch KeyWord   =====')
    keyword = input('>  ')
        
    #�o�̓t�@�C���������(���΃p�X or ��΃p�X)        
    print ('====== Enter Tweet Data file =====')
    dfile = input('>  ')
        
    get_twitter_data(keyword,dfile)
    
