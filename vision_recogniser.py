######################################################
# Before running this create a directory structure or 
# edit the base variable to point to newely created 'jump' directory
# there should be two sub-directories in the 'jump' directory
# 1) data 2) models     <---- mind the case, its sensitive. ;)
# Please report all the bugs to jumplabs. the codes are 
# written exclusively for jumplabs.
######################################################


import os
import random
from glob import glob
import cv2
import pandas as pd
import joblib
import pickle
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

cascPath = "/home/devendra/Desktop/haarcascade_frontalface_default.xml"
base = "/home/devendra/Desktop/jump/"
rtb = None


def convert_real(ls):

    return [ls_ele.real for ls_ele in ls]


def covNcorr(Mat):
    """
    This function is to calculate the covariance and the correlation matrix of the given matrix 'Mat'
    Calculation has been done in vectorised form using numpy module of python

    Parameter:
    (Type: numpy.array) Mat:---> Data matrix is required in the columns as attributes(features) and rows as records

    Return:
    (Type: numpy.array) CovMat:---> Covariance matrix of data matrix 'Mat'
    (Type: numpy.array) CorrMat:---> Correlation matrix of the data mtrix 'Mat'

    """

    # Converting Matrix to float type
    Mat = Mat.astype(np.float)

    # Taking shape of matrix
    r, c = Mat.shape

    # Making array to contain Std. Deviation of columns of the matrix
    Colstd = np.zeros(c).astype(np.float)

    # Making data as mean centralised
    for i in range(c):

        Mat[:, i] = (Mat[:, i] - np.mean(Mat[:, i]))

    # Finding the Std. Deviation of each column in vectorized operation
    for i in range(c):
        # This operation is only valid if the matrix is mean centralised.
        # Its valid in this case as the mean centralisation has been done in previous step.
        Colstd[i] = 1 / (r - 1) * np.sqrt(np.dot(np.transpose(Mat[:, i]), Mat[:, i]))

    # Containers/Variables to hold covariance and correlation of Mat
    CovMat = np.zeros([c, c]).astype(np.float)
    CorrMat = np.zeros([c, c]).astype(np.float)

    # Calculating covariance and correlation of data matrix 'Mat'
    for i in range(c):

        for j in range(c):
            # Covariance
            CovMat[i][j] = 1 / (r - 1) * np.dot(np.transpose(Mat[:, i]), Mat[:, j])

            # Correlation
            CorrMat[i][j] = 1 / (r - 1) * np.dot(np.transpose(Mat[:, i]), Mat[:, j]) / (Colstd[i] * Colstd[j])

    return CovMat, CorrMat


def PrincipalComponentAnalysis(Mat, IP=90, PCA_vectors=0, print_msg=False):
    '''
    This function is to find out the principal components of the given data.

    Parameters:
    (Type: numpy.array) Mat:---> Data matrix is required in the columns as attributes(features) and rows as records (without output labels)
    (Type: float) IP:---> IP is the threshold of the information that is should be preserved at minimum (Information Preserved). If value of PCA_vectors variable is non zero. then the IP value will get override.
    (Type: int) PCA_vectors:---> Number of vectors to have in the transformation basis. If it is 0 then the vectors will be in such manner that the information preserved is atleast till IP level


    Return:
    (Type: numpy.array) Ready_Transform_basis:---> This is the transformation matrix. it can be used to calculate the projection of the data matrix. It consists of most significant vectors as column entry.
    (Type: numpy.array) projected_data:---> This contains the projected matrix. ie. dot product of Mat and Ready_Transform_basis
    (Type: float) information_Retained:---> This gives the floating point number indicationg the information retained by the Ready_transforma_basis

    '''

    # function to calulate the covariance and the correlation of the matrix
    CovMat, CorrMat = covNcorr(Mat)

    # finding the eigenvalues and eigenvectors of covariance matrix
    e, v = np.linalg.eig(CovMat)

    if isinstance(e[0], complex):

        e = np.array(convert_real(e))
        v = np.array([convert_real(v_ele) for v_ele in v])

    # sorting using dataframes
    df = pd.DataFrame([e, v]).transpose()
    df.columns = (["EigenValue", "EigenVector"])
    dfsorted = df.sort_values(by="EigenValue", ascending=False)
    eigenvalues_sorted = np.array(dfsorted["EigenValue"])
    eigenvectors_sorted = np.array(dfsorted["EigenVector"])

    # calculating the information preserved and the principal components
    sum_eigenvalues = np.sum(eigenvalues_sorted)
    eigen_temp_sum = 0.0
    IP_calc = 0.0
    Transform_matrix = np.transpose(eigenvectors_sorted[0]).copy()
    i = 0
    flag = 1

    while flag:

        eigen_temp_sum = eigen_temp_sum + eigenvalues_sorted[i]
        IP_calc = eigen_temp_sum / sum_eigenvalues * 100

        if print_msg:

            print("Adding Component No.", i + 1)

        if i != 0:

            Transform_matrix = np.append(Transform_matrix, np.transpose(eigenvectors_sorted[i]))

        i = i + 1

        if print_msg:

            print("Information Retained = ", IP_calc)

        if PCA_vectors == 0:

            if IP <= IP_calc or IP_calc == 100:

                flag = 0

        else:

            if i >= PCA_vectors or IP_calc == 100:

                flag = 0

    Ready_Transform_basis = np.transpose(Transform_matrix.reshape(i, eigenvectors_sorted[0].shape[0])).copy()

    if print_msg:

        print("+++++++++++++++++++++++++++++++Transform_basis+++++++++++++++++++++++++")
        print(Ready_Transform_basis)
        print("Projected Data:")

    # calculating the projection matrix
    projected_data = np.dot(Mat, Ready_Transform_basis)

    if print_msg:

        print(projected_data)

    # information retained
    information_Retained = IP_calc

    return Ready_Transform_basis, projected_data, information_Retained


def path_corrector(path):

    path = path.replace(" ", "_")

    return path


def getNewClass(name="Anonymous", gender="No Mention", age=0, relation_with_family="NA"):

    id = name + "_" + gender + "_" + str(age) + "_" + relation_with_family + "_" + str(random.randint(1, 10000)) + str(
        random.randint(500, 50000))
    id = path_corrector(id)
    folder = base + "data/" + id
    os.mkdir(folder)
    image_index_file_handle = open(folder + "/index.jump", "a")
    data_file_handle = open(folder + "/data.jump", "a")
    data_file_handle.write("Data about the individual\n")
    faceCascade = cv2.CascadeClassifier(cascPath)
    video_capture = cv2.VideoCapture(1)
    count = 0

    while True:

        count += 1
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(128, 128),
        )

        for (x, y, w, h) in faces:

            record = gray[y:y + h, x:x + w]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 255, 100), 1)
            cv2.imwrite(folder + "/" + "img" + str(count) + ".jpg", record)
            image_index_file_handle.write(folder + "/" + "img" + str(count) + ".jpg\n")

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):

            break

    video_capture.release()
    image_index_file_handle.close()
    data_file_handle.close()
    cv2.destroyAllWindows()


def training_data_prep():

    _labels = list()
    _images = list()
    class_roots = glob(base + "data/" + "*/")
    labels = [dataclass + "data.jump" for dataclass in class_roots]
    classes = [dataclass + "index.jump" for dataclass in class_roots]
    label_id = 0
    label_dictionary = {}

    for (_class, _label) in zip(classes, labels):

        print("Opening directory:", _class)

        try:

            records_access_handle = open(_class, "r")
            # This can _label can point to empty file. Caution

        except Exception as e:

            print("[X] Problem in opening the index.jump for ", _class, "---> Exception:", e)

        while True:

            try:

                address = records_access_handle.readline()

                if address == "":

                    break

                address = address.split("\n")[0]
                print("Accessing image: ", address)
                img = cv2.imread(address, 0)
                img = cv2.resize(img, (64, 64))
                cv2.waitKey(20)

                if len(img) != 0:

                    cv2.imshow("Training Sequence", img)
                    _labels.append(label_id)
                    label_dictionary[label_id] = _label
                    _images.append(np.array(img))
                    print("+++++>>>>>>>")

            except Exception as e:

                print("[X] Image is not read for address ", address, "---> Exception:", e)

        records_access_handle.close()
        label_id += 1

    cv2.destroyAllWindows()

    return _images, _labels, label_dictionary


def prediction_from_stream():

    path = base + "models/" + "LBPH.YAML"
    faceCascade = cv2.CascadeClassifier(cascPath)
    model = cv2.face.createEigenFaceRecognizer()
    model.load(path)
    cam = cv2.VideoCapture(1)

    while True:

        ret, img1 = cam.read()
        img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            img,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(64, 64),
        )

        for (x, y, w, h) in faces:

            # try:
            record = img[y:y + h, x:x + w]
            img = cv2.resize(record, (256, 256))
            pre_labels, accuracy = model.predict(img)
            # pre_address = [labels_dictionary[pre_labels]]
            print("Accuracy: ", 100 - accuracy, "Label: ", model.getLabelInfo(pre_labels))
            cv2.rectangle(img1, (x - 5, y - 5), (x + w + 5, y + h + 5), (50, 255, 100), 1)
            cv2.putText(img1, model.getLabelInfo(pre_labels), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (0, 0, 255), 1,
                        cv2.LINE_AA)
        # except:
        # print("[x] Prediction error")
        cv2.imshow("recog", img1)
        cv2.waitKey(30)


def models_prep():

    imgs, labels, labels_dictionary = training_data_prep()
    print("Input imges: ", len(imgs))
    print("lebels of imges: ", len(labels))

    X = np.array(imgs)
    a, b, c = X.shape
    X = np.resize(X, (a, b * c))
    y = np.array(labels)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    n_components = 80
    rtb, pd, ir = PrincipalComponentAnalysis(X_train, PCA_vectors=n_components, print_msg=True)
    X_train_pca = pd

    with open(base + "models/rtb.jump", 'wb') as fp:

        pickle.dump(rtb, fp)

    # pca_rtb = open(base + "models/rtb.jump", 'w')
    # pca_rtb.write(rtb)
    # pca_rtb.close()

    X_test_pca = np.dot(X_test, rtb)

    ##
    ## Multilayered Perceptron training:
    ##
    try:

        clf = MLPClassifier(hidden_layer_sizes=(1024,), batch_size=256, verbose=True, early_stopping=True)
        clf.fit(X_train_pca, y_train)
        y_pred = clf.predict(X_test_pca)
        print(classification_report(y_test, y_pred, target_names=labels_dictionary.values()))

        joblib.dump(clf, base + "models/MLPClassifier.sav")

    except Exception as e:

        print("Multilayer perceptron training error reported: [x]error-->", e)

    ##
    ## Support vector classifier
    ##
    try:

        clf = SVC()
        clf.fit(X_train_pca, y_train)
        y_pred = clf.predict(X_test_pca)
        print(classification_report(y_test, y_pred, target_names=labels_dictionary.values()))

        joblib.dump(clf, base + "models/SVClassfier.sav")

    except Exception as e:

        print("Support vector classifier training error reported: [x]error-->", e)
    ##
    ## RandomForestClassifier
    ##
    try:

        clf = RandomForestClassifier()
        clf.fit(X_train_pca, y_train)
        y_pred = clf.predict(X_test_pca)
        print(classification_report(y_test, y_pred, target_names=labels_dictionary.values()))

        joblib.dump(clf, base + "models/RandomForestClassifier.sav")

    except Exception as e:

        print("RandomForestClassifier training error reported: [x]error-->", e)

    ##
    ## GradientBoostingClassifier
    ##
    try:

        clf = GradientBoostingClassifier()
        clf.fit(X_train_pca, y_train)
        y_pred = clf.predict(X_test_pca)
        print(classification_report(y_test, y_pred, target_names=labels_dictionary.values()))

        joblib.dump(clf, base + "models/GradientBoostingClassifier.sav")

    except Exception as e:

        print("GradientBoostingClassifier training error reported: [x]error-->", e)

    ##
    ## KNeighborsClassifier
    ##
    try:

        clf = KNeighborsClassifier()
        clf.fit(X_train_pca, y_train)
        y_pred = clf.predict(X_test_pca)
        print(classification_report(y_test, y_pred, target_names=labels_dictionary.values()))

        joblib.dump(clf, base + "models/KNeighborsClassifier.sav")

    except Exception as e:

        print("KNeighborsClassifier training error reported: [x]error-->", e)

    ##
    ## GaussianNB
    ##
    try:

        clf = GaussianNB()
        clf.fit(X_train_pca, y_train)
        y_pred = clf.predict(X_test_pca)
        print(classification_report(y_test, y_pred, target_names=labels_dictionary.values()))

        joblib.dump(clf, base + "models/GaussianNB.sav")

    except Exception as e:

        print("GaussianNB training error reported: [x]error-->", e)


def prediction_by_master(img):
    pass


def data_reader(address):
    pass


#
 #
#
 #     Testing block
#
 #
#

if __name__ == "__main__":

    res = 'n'

    while res == 'y':
        name = input("Name of person: ")
        getNewClass(name)
        res = input("Want to add more people ? give 'y' for yes.")

    res2 = input("Want to start training? [y,n]: ")
    if res2 == 'y':
        models_prep()

    ############# Incomplete for prediction ################
    ########################################################

    res3 = input("Want predictions? [y/n]: ")
    if res3 == 'y':
        prediction_from_stream()

    #######################################################
