import os
import sys

from grafico import *
import classify
from classify import *

from pyspark import SparkConf, SparkContext

conf = (SparkConf()
         .setMaster("local")
         .setAppName("Analise de Sentimentos")
         .set("spark.executor.memory", "1g"))
sc = SparkContext(conf = conf)


def analiseSentimentos(x):
    resultado = classify(x)
    if resultado=='positive': return 1
    return 0
    

def funcaoMain():
    if len(sys.argv)<2:
        return False
    hashtag = sys.argv[1]
    if len(hashtag)==0:
        hashtag = "#"
    arquivo = sc.textFile("./arquivos/{0}.txt".format(hashtag))
    geraGrafico(hashtag, arquivo.map(lambda x: (analiseSentimentos(x.split("|")[0]), 1) ).reduceByKey(lambda x,y: x+y).sortByKey(False).collect())

if __name__ == '__main__':
    funcaoMain()