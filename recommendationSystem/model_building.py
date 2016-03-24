import pandas
import math
from sklearn import neighbors, datasets
from numpy.random import permutation
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_recall_fscore_support

def Nearest_Neighbour_classifier(train_input_data,train_output_data,test_input_data,test_output_data):
    neighbour_list = []
    accuracy_percent = []
    for neighbours in range(1,101,5):
        clf = neighbors.KNeighborsClassifier(neighbours, weights='uniform')
        clf.fit(train_input_data, train_output_data)
        predicted_output = clf.predict(test_input_data)
        if isinstance(predicted_output,list) ==False:
            predicted_output = predicted_output.tolist()
        if isinstance(test_output_data,list) ==False:
            test_output_data = test_output_data.tolist()
        error_list = []
        for i in range(len(test_output_data)):
            cur_univ_similarities =  similar_univs[similar_univs['univName'] == predicted_output[i]]
            cur_univ_similarity_list = cur_univ_similarities.values.tolist()
            cur_univ_similarity_list = [item for sublist in cur_univ_similarity_list for item in sublist]
            if test_output_data[i] in cur_univ_similarity_list[1:]:
                error_list.append(0)
            else:
                error_list.append(1)
        neighbour_list.append(neighbours)
        accuracy_percent.append(100 -((sum(error_list)/float(len(error_list))) * 100))
    neighbour_list = np.array(neighbour_list)
    accuracy_percent = np.array(accuracy_percent)
    plt.plot(neighbour_list,accuracy_percent)
    plt.xlabel('Number of nearest neighbors')
    plt.ylabel('Percent of accuracy')
    plt.title('Varation of accuracy with nearest neighbours')
    plt.grid(True)
    plt.savefig("knn1.png")
    plt.show()
    return predicted_output

def SVM_classifier(train_input_data,train_output_data,test_input_data,test_output_data):
    clf = svm.SVC()
    clf.fit(train_input_data,train_output_data)
    predicted_output = clf.predict(test_input_data)
    error_list = []
    predicted_output = predicted_output.tolist()
    test_output_data  = test_output_data.tolist()
    for i in range(len(test_output_data)):
        cur_univ_similarities =  similar_univs[similar_univs['univName'] == predicted_output[i]]
        cur_univ_similarity_list = cur_univ_similarities.values.tolist()
        cur_univ_similarity_list = [item for sublist in cur_univ_similarity_list for item in sublist]
        if test_output_data[i] in cur_univ_similarity_list[1:]:
            error_list.append(0)
        else:
            error_list.append(1)
    return predicted_output

def Random_Forest_classifier(train_input_data,train_output_data,test_input_data,test_output_data):
    tree_list = []
    accuracy_percent = []
    for trees in range(10,200,10):
        clf = RandomForestClassifier(trees)
        clf.fit(train_input_data,train_output_data)
        predicted_output = clf.predict(test_input_data)
        error_list = []
        if isinstance(predicted_output,list) ==False:
            predicted_output = predicted_output.tolist()
        if isinstance(test_output_data,list) ==False:
            test_output_data = test_output_data.tolist()
        for i in range(len(test_output_data)):
            cur_univ_similarities =  similar_univs[similar_univs['univName'] == predicted_output[i]]
            cur_univ_similarity_list = cur_univ_similarities.values.tolist()
            cur_univ_similarity_list = [item for sublist in cur_univ_similarity_list for item in sublist]
            if test_output_data[i] in cur_univ_similarity_list[1:]:
                error_list.append(0)
            else:
                error_list.append(1)
        tree_list.append(trees)
        accuracy_percent.append(100 -((sum(error_list)/float(len(error_list))) * 100))
    tree_list = np.array(tree_list)
    accuracy_percent = np.array(accuracy_percent)
    plt.plot(tree_list,accuracy_percent)
    plt.xlabel('Number of trees')
    plt.ylabel('Percent of accuracy')
    plt.title('Varation of accuracy with trees')
    plt.grid(True)
    plt.savefig("rf1.png")
    plt.show()
    return predicted_output


data = pandas.read_csv('processed_data.csv')
data = data.drop('Unnamed: 0',1)
data = data.drop('Unnamed: 0.1',1)

similar_univs = pandas.read_csv('similar_universities.csv')
random_indices = permutation(data.index)
test_cutoff = math.floor(len(data)/5)
test = data.loc[random_indices[1:test_cutoff]]
train = data.loc[random_indices[test_cutoff:]]
train_output_data = train['univName']
train_input_data = train
train_input_data = train_input_data.drop('univName',1)
test_output_data = test['univName']
test_input_data = test
test_input_data = test_input_data.drop('univName',1)

output = Random_Forest_classifier(train_input_data,train_output_data,test_input_data,test_output_data)
output = SVM_classifier(train_input_data,train_output_data,test_input_data,test_output_data)
output = Nearest_Neighbour_classifier(train_input_data,train_output_data,test_input_data,test_output_data)
