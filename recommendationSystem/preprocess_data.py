import collections
import pandas
from collections import defaultdict

def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

def feature_extraction_categorical_variable(data2,feature):
    feature_list = data2[feature].astype(basestring)
    student_id_for_feature = defaultdict(list)
    for i in range(len(feature_list)):
        feature_list[i] = str(feature_list[i])
        feature_list[i] = feature_list[i].strip()
        feature_list[i] = feature_list[i].replace('-', '')
        feature_list[i] = feature_list[i].replace('.', '')
        feature_list[i] = feature_list[i].partition('/')[0]
        feature_list[i] = feature_list[i].partition('(')[0]
        feature_list[i] = feature_list[i].replace(' ','')
        feature_list[i] = feature_list[i].lower()

    max_len = 0
    max_feature_name = ""
    unique_feature = []
    for i in range(len(feature_list)):
        for j in range(i+1,len(feature_list)):
            if (feature_list[i] in feature_list[j]):
                if (max_len < len(feature_list[j])):
                    max_len = len(feature_list[j])
                    max_feature_name = feature_list[j]
        if max_len == 0:
            unique_feature.append(feature_list[i])
            student_id_for_feature[feature_list[i]].append(i)
        elif max_len > 0:
            student_id_for_feature[max_feature_name].append(i)
        max_len = 0

    for i in range(len(unique_feature)):
        student_list_for_cur_feature = [0] * len(data2)
        for j in student_id_for_feature[unique_feature[i]]:
            student_list_for_cur_feature[j] = 1
        data2[unique_feature[i]] = student_list_for_cur_feature
        pass

    return data2

def normalize_gpa(data2,cgpa,totalcgpa):
    cgpa = data2[cgpa].tolist()
    totalcgpa = data2[totalcgpa].tolist()
    for i in range(len(cgpa)):
        if totalcgpa[i] != 0:
            cgpa[i] = cgpa[i] / totalcgpa[i]
        else:
            cgpa[i] = 0
    data2['cgpa'] = cgpa
    return data2

def convert_quant_score(quant_score):
    quant_list = []
    quant_score = quant_score.tolist()
    for old_quant in quant_score:
        if old_quant <= 170:
            quant_list.append(old_quant)
            continue
        flag=0
        new_quant=0
        for l in open("scoreconversion"):
            l=str(l)
            one,two,three=l.strip().split(" ")
            Old,nquant=one.split("\t")
            Old=int(Old)
            if Old==old_quant:
                new_quant=nquant
                flag+=1
            if flag==2:
                break
        quant_list.append(new_quant)
    return quant_list

def convert_verbal_score(verbal_score):
    verbal_list = []
    verbal_score = verbal_score.tolist()
    for old_verbal in verbal_score:
        if old_verbal <= 170:
            verbal_list.append(old_verbal)
            continue
        flag=0
        new_verbal=0
        for l in open("scoreconversion"):
            l=str(l)
            one,two,three=l.strip().split(" ")
            Old,nquant=one.split("\t")
            verbalp,nverbal=two.split("\t")
            Old=int(Old)
            nverbal=int(nverbal)
            if Old==old_verbal:
                new_verbal=nverbal
                flag+=1
            if flag==2:
                break
        verbal_list.append(new_verbal)
    return verbal_list


data = pandas.read_csv('original_data.csv')

data = data.drop('gmatA',1)
data = data.drop('gmatQ',1)
data = data.drop('gmatV',1)
data = data.drop('specialization',1)
data = data.drop('department',1)
data = data.drop('program',1)
data = data.drop('toeflEssay',1)
data = data.drop('userProfileLink',1)
data = data.drop('topperCgpa',1)
data = data.drop('termAndYear',1)
data = data.drop('userName',1)
data = data.drop('toeflScore',1)

data = data[data['admit'] > 0]
data = data.drop('admit',1)
university_list = list(set(data['univName'].tolist()))
for i in range(len(university_list)):
    if(len(data[data['univName'] == university_list[i]]) < 100):
        data = data[data['univName'] != university_list[i]]

data = data.dropna()

data['greQ'] = convert_quant_score(data['greQ'])
data['greV'] = convert_verbal_score(data['greV'])


data = feature_extraction_categorical_variable(data,'ugCollege')
data2 = data.drop('ugCollege',1)

data = feature_extraction_categorical_variable(data,'major')
data = data.drop('major',1)

data2 = normalize_gpa(data2,'cgpa','cgpaScale')

data2 = data2.drop('industryExp',1)
data2 = data2.drop('internExp',1)
data2 = data2.drop('confPubs',1)
data2 = data2.drop('cgpaScale',1)
data2 = data2.drop('toeflScore',1)
data2 = data2.drop('journalPubs',1)

data2.to_csv('processed_data.csv')




