#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#
# PROGRAMMER: Susanta pattanayak
# DATE CREATED:  02/08/2019
# REVISED DATE: 02/25/2019
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
#


def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifier labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """
    dognames_dic = dict()
    with open(dogfile) as dog_file:
        for line in dog_file:
            line = line.strip()
            if line not in dognames_dic:
                dognames_dic[line] = 1
            else:
                print("Warning: the dog name: {} already exists in the dognames_dic".format(line))

    for key, val in results_dic.items():
        pet_image_label_isdog = 0
        pet_classifier_label_isdog = 0

        for k in dognames_dic.keys():

            ls = list(map(str.strip, k.split(',')))

            if val[0] in ls:
                pet_image_label_isdog = 1
            # this is the tricky part, any match required
            for cl_item in val[1].split(","):
                if cl_item.strip() in ls:
                    pet_classifier_label_isdog = 1
                    break

            # if val[1] in k.split(","):
            #    pet_classifier_label_isdog = 1
            if pet_image_label_isdog == 1 and pet_classifier_label_isdog == 1:
                break

        val.extend([pet_image_label_isdog, pet_classifier_label_isdog])

    # Commented test function to iterate through the results_dic to print out pet and classified labels

    """
    for key, val in results_dic.items():
        print("key: ", key, " pet image label: ", val[0],
              " classifier label: ", val[1],
              " match btw pet_label and classifies: ", val[2], " pet image is-a dog:  ", val[3],
              " Classifier classifies image as-a dog: ", val[4], "\n")
    """


None
