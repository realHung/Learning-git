#XXXXXXXXXXXXXXXXXXXXXXXXX COPY LAB6 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
filenames = ["Beagle_01141.jpg", "Beagle_01125.jpg", "skunk_029.jpg" ]
pet_labels = ["beagle", "beagle", "skunk"]
classifier_labels = ["walker hound, walker foxhound", "beagle",
                    "skunk, polecat, wood pussy"]
pet_label_is_dog = [1, 1, 0]
classifier_label_is_dog = [1, 1, 0]
# tao mot bien result_dic 
results_dic = dict()
# so sanh trung khop thi gan
for idx in range (0, len(filenames), 1):
# neu chua co trong result_dic thi them vao result_dic
    if filenames[idx] not in results_dic:
        results_dic[filenames[idx]] = [ pet_labels[idx], classifier_labels[idx] ]
        found = classifier_labels[idx].find(pet_labels[idx])
#lay cac nhan cua bo phan loai tim trong pet_labels neu co thi dem 1 nguoc lai giu nguyen
    if found >= 0:
        results_dic[filenames[idx]] += [ 1 ]
    else:
        results_dic[filenames[idx]] += [ 0 ]
#neu ket qua trug khop nhan pet và phan loai nhan pet
#in ra ket qua " pet_label_is_dog=1"
#in ra ket qua " classifier_label_is_dog=1" nguoc lai bang 0
for idx in range (0, len(filenames), 1):
    results_dic[filenames[idx]].append(pet_label_is_dog[idx])
    results_dic[filenames[idx]].append(classifier_label_is_dog[idx])
for key in results_dic:
    print("\nFilename=", key, "\npet_image Label=", results_dic[key][0],
          "\nClassifier Label=", results_dic[key][1], "\nmatch=",results_dic[key][2],
          "\nImage is dog=", results_dic[key][3],"\nClassifier is dog=", results_dic[key][4])
#tao result_stats_dic
results_stats_dic = dict()
#Khoi tao cac gia tri
results_stats_dic['n_dogs_img'] = 0
results_stats_dic['n_match'] = 0
results_stats_dic['n_correct_dogs'] = 0
results_stats_dic['n_correct_notdogs'] = 0
results_stats_dic['n_correct_breed'] = 0
# tinh tong so luong
results_stats_dic['n_images'] = len(results_dic)
for key in results_dic:
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1
        pass
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1

        if results_dic[key][4] == 1:
            results_stats_dic['n_correct_dogs'] += 1
        else:
            pass
            pass
# tinh so buc anh khong phai anh cho
results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] - results_stats_dic['n_dogs_img'])
results_stats_dic['n_correct_notdogs'] = (results_stats_dic['n_dogs_img'] - results_stats_dic['n_correct_dogs'])
#ti le phan tram trung và khong trung
results_stats_dic['pct_match'] = 0.0
results_stats_dic['pct_correct_dogs'] = 0.0
results_stats_dic['pct_correct_notdogs'] = 0.0
results_stats_dic['pct_correct_breed'] = 0.0
# phan tram hinh cho trung khop voi nhan cho chinh xac
results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] /results_stats_dic['n_dogs_img'])*100.0
#phan tram hinh cho khong trung khop voi nhan cho
if results_stats_dic['n_notdogs_img'] > 0:
     results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] /results_stats_dic['n_notdogs_img'])*100.0
else:
     results_stats_dic['pct_correct_notdogs'] = 0.0
#pham tran  trung khop chinh xac
results_stats_dic['pct_match'] = (results_stats_dic['n_match'] /results_stats_dic['n_images'])*100.0
print("\nNumber of image=",results_stats_dic['n_images'] ,"\nNumber of match=",results_stats_dic['n_match'] ,
      "\nNumber of dog=",results_stats_dic['n_dogs_img'],
      "\nNumber of not dog=",results_stats_dic['n_notdogs_img'] ,
      "\nNumber of correct dogs=",results_stats_dic['n_correct_dogs'],
      "\nNumber of correct not dogs=",results_stats_dic['n_correct_notdogs'],
      "\nPercent of match=",results_stats_dic['pct_match'],
      "\nPercent of correct no dog=",results_stats_dic['pct_correct_notdogs'],
      "\nPercent of correct dog=",results_stats_dic['pct_correct_dogs'])
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX END LAB6 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# In ra ket qua thong ke cac thong so
print("\n Results Summary for CNN Model Architecture : VGG")
print("%25s: %3d" % ('Number Images',results_stats_dic['n_images']))
print("%25s: %3d" % ('Number Dog Images',results_stats_dic['n_dogs_img']))
print("%25s: %3d" % ('Number Not-Dog Images',results_stats_dic['n_notdogs_img']),'\n')

# in ra ket qua tong
for key in results_stats_dic:
    if key[0] == 'p':
       print("%25s: %5.1f" % (key,results_stats_dic[key]))
# IF print_incorrect_dogs == True AND there were images incorrectly
# classified as dogs or vice versa - print out these cases
if ((results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'])!= results_stats_dic['n_images']):
        print("\n INCORRECT Dog/NOT Dog Assignments: ")
        # process through results dict,printing incorrectly classified dogs
        for key in results_dic:
             # Pet Image Label is a Dog - Classified as NOT-A-DOG -OR-
             # Pet Image Label is NOT-a-Dog - Classified as a-DOG
             if sum(results_dic[key][3:]) == 1:
                  print("Real: %-26s   Classifier: %-30s" % (results_dic[key][0],results_dic[key][1]))
# IF print_incorrect_breed == True AND there were dogs whose breeds
# were incorrectly classified - print out these cases
if (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']):
        print("\nINCORRECT Dog Breed Assignment:")

        # process through results dict, printing incorrectly classified breeds
        for key in results_dic:
        # Pet Image Label is-a-Dog, classified as-a-dog but is WRONG breed
            if ( sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0 ):
              print("Real: %-26s   Classifier: %-30s" % (results_dic[key][0],results_dic[key][1]))
