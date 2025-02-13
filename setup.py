# -*- coding: utf-8 -*-
# @Time    : 18-9-28 下午1:16
# @Author  : duyongan
# @FileName: setup.py
# @Software: PyCharm

from distutils.core import setup

setup(
    name='text_process',
    version='2.3.6',
    packages=['text_process'],
    author='Haydon',
    author_email='13261051171@163.com',
    description='easy utils for process text',
    package_data = {'text_process': ['*']},
    install_requires=['nltk','jieba','simple_pickle','numpy'],
    long_description="""
    # 环境：python3    
    # 安装：pip install text_process    
    # 使用示例：   
    
    from text_process import text_utils   
    text=""   
    # 中文分句：   
    text_utils.text2sencents_zh(text)    
    # 英文分句：   
    text_utils.text2sencents_eh(text)   
    # 英文分词（词组、单词、且已去停用词）    
    text_utils.text2sencents_eh(text)    
    # 中文分词（已去停用词）    
    text_utils.text_process_zh_single(text)    
    # 中文分词（词组 已去停用词）     
    text_utils.text_process_zh_not_single(text)     
    # 中文关键字(不包括词组)    
    text_utils.getKeywords_zh_single(text)    
    # 中文关键字(包括词组)     
    text_utils.getKeywords_zh_not_single(text)    
    # 英文关键字（包括词组）    
    text_utils.getKeywords_en(text)    
    # 文本相似度比较    
    compare_botor=text_utils.compare_bot()     
    text2=""     
    compare_bot.compare_two_txt_accuracy(text,text2)     
    #或者（适合少量数据）     
    text_utils.compare_two_txt_accuracy(text,text2)    
    # 中文摘要    
    text_utils.getAbstract_zh(title,text)     
    # 英文摘要     
    text_utils.getAbstract_en(title,text)     
    """
)