from collections import Counter
import glob
import re
from operator import itemgetter
from math import exp, expm1

def bm_25():

    unigram_dict = dict()
    query_dict = dict()
    doc_length_dict = dict()
    avdl = 0

    # input file name having unigram inverted index
    uni_file = input("Enter the name of unigram file (with .txt): ")

    # creating dictionary from unigram text file
    unigram_dict = dict_from_index(uni_file, unigram_dict)

    # input file name having queries (in dictionary form)
    query_file = input("Enter the name of file having queries (with .txt): ")

    # creating dictionary from queries files
    query_dict = dict_from_queries(query_file, query_dict)

    #  Creating dictionary for document length:
    doc_length_dict = dict_of_doc_length(unigram_dict, doc_length_dict)

    # calculating average document length:
    avdl = average_doc_length(doc_length_dict)

    # inverted list for query terms:
    k10 = ""
    val = ""
    for i in query_dict:
        query_terms_dict = dict()                  # Dictionary having Document ID and their scores
        qf_dict = dict()                           # Dictionary to keep track of query terms frequency
        score = 0
        final_score = 0
        dl = 0
        K = 0
        for j in query_dict[i].split(' '):
            if j in unigram_dict:
                il = len(unigram_dict[j])
                st1 = unigram_dict[j][1:il-1]
                k10 = re.findall(r'\[(.*?)\]', st1)
                if j in qf_dict:
                    qf_dict[j] = qf_dict[j] + 1
                if j not in qf_dict:
                    qf_dict[j] = 1
                for e in k10:
                    l1 = re.split(",(?=(?:[^']*\'[^']*\')*[^']*$)",e)
                    val = l1[1].strip()
                    key,val1 = l1[0], int(val)                             # key value for document length dictionary
                    key1 = key[1:len(key)-1]
                    dl = doc_length_dict[key1]                             # document length
                    fi = val1                                              # term frequency in the given document
                    ni = len(k10)                                          # number of documents having the query term
                    K = (1.2 * (0.25 + (0.75 * (dl/avdl))))                # K parameter calculation
                    score = ((0.25 * (1000 - (ni + 0.5)))/(ni + 0.5)) * ((2.2 * fi)/(K + fi)) * ((101 * qf_dict[j])/(100 + qf_dict[j]))  # Formula
                    final_score = math.log2(score)
                    if key1 in query_terms_dict:
                        query_terms_dict[key1] = query_terms_dict[key1] + final_score
                    else:
                        query_terms_dict[key1] = final_score



        # writing BM25 scores corresponding to Documents in new query files:
        write_scores(i, query_dict, query_terms_dict)



def dict_from_index(uni_file, unigram_dict):
    with open(uni_file, "r", encoding = 'UTF-8') as f:
        for line in f:
            line = line.strip()
            items = line.split(':')
            k,v = items[0], items[1]
            unigram_dict[k] = v
    return unigram_dict


def dict_from_queries(query_file, query_dict):
    with open(query_file, "r", encoding = 'UTF-8') as f:
        for line in f:
            (key, val) = line.split(':')
            val = val[:-1]
            query_dict[int(key)] = val
    return query_dict


def dict_of_doc_length(unigram_dict, doc_length_dict):
    st = ""
    fname = ""
    k = ""
    v1 = 0
    for i in unigram_dict:
        ilen = len(unigram_dict[i])
        st = unigram_dict[i][1:ilen-1]
        k = re.findall(r'\[(.*?)\]', st)
        for e in k:
            l = re.split(",(?=(?:[^']*\'[^']*\')*[^']*$)",e)
            v = l[1].strip()
            k,v1 = l[0], int(v)
            k1 = k[1:len(k)-1]
            if k1 in doc_length_dict:
                doc_length_dict[k1] = doc_length_dict[k1] + v1
            else:
                doc_length_dict[k1] = v1
    return doc_length_dict


def average_doc_length(doc_length_dict):
    avdl = 0
    c_length = 0
    for u in doc_length_dict:
        c_length = c_length + doc_length_dict[u]
    avdl = c_length/1000
    return avdl


def write_scores(i, query_dict, query_terms_dict):
    d = ""
    d = sorted (query_terms_dict.items(), key = itemgetter(1), reverse = True)
    loc = "C:/Users/ashuk/" + query_dict[i] + ".txt"
    with open(loc, "a") as f:
        count = 1
        for fkey,fvalue in d[:100]:
                f.write('%s %s %s %s %s %s\n' % (query_dict[i],"Q0",fkey,count,fvalue, "system_name"))
                count = count+1


bm_25()
