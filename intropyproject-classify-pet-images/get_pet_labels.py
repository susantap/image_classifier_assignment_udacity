#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
#
# PROGRAMMER: Susanta pattanayak
# DATE CREATED:  02/08/2019
# REVISED DATE: 02/27/2019
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir, path
from PIL import Image


# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
#
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """

    # Get the filename from the image directory
    filename_list = listdir(image_dir)
    results_dic = dict()

    # Iterate through the filename to generate the pet label
    for f_id in range(0, len(filename_list), 1):

        # validate the image file. and if Valid then continue or just ignore that file

        if validate_image_file(image_dir, filename_list[f_id]):
            file_name = path.splitext(filename_list[f_id])[0]

            if filename_list[f_id] not in results_dic:
                pet_label = ""

                #  format the pet labels so that they are in all lower case letters
                #     and with leading and trailing whitespace characters stripped from them.
                #     (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')

                for word in file_name.lower().split("_"):
                    if word.isalpha():
                        pet_label += word + ' '

                pet_label = pet_label.strip()
                results_dic[filename_list[f_id]] = [pet_label]

    return results_dic


def validate_image_file(image_dir, file_name):
    """
    Function to validate the image and print the Error results if any
    :param image_dir: image directory input
    :param file_name: image filename
    :return: Returns if the image file is valid

    """
    # filename parser should detect and fully ignore any filename starting with '.'
    # Notes: I could have used an if-else. But preferred 'continue'
    is_valid = True
    image_file_path = path.join(image_dir, file_name)
    if file_name.startswith("."):
        print("\n\nERROR: File {} is not a valid file name as it starts with  '.'".format(file_name))
        is_valid = False
        return is_valid
    # Check if the file has the right extension
    try:
        file_image = Image.open(image_file_path)
        file_image.verify()
        return is_valid

    except OSError as e:
        # Print the invalid image details
        print('Exception: {} ERROR: File {} is not a valid image \n'.format(e, file_name))
        is_valid = False
        return is_valid
