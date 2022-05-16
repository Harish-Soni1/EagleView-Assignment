import os

from helper import convert_labels

DIR = "./txt_annotation_new"
filePath = r"./annotations/bbox-annotations.json"

Img_annot = None

with open (filePath, 'r') as file:
    jsonData = eval(file.read())
    for image in jsonData['images']:
        fileName = image['file_name']
        imageId = image['id']
        with open (os.path.join(DIR, fileName.replace('.jpg', '.txt')), 'w+') as txtFile:
            for annot in jsonData['annotations']:
                if annot['image_id'] == imageId:
                    categoryId = str(annot['category_id']-1)
                    annot['bbox'] = convert_labels(image, annot['bbox'])
                    box = " ".join([str(b) for b in annot['bbox']])
                    txtFile.write(f"{categoryId} {box}")
                    txtFile.write("\n")
        
        txtFile.close()

        print(f"{image['file_name']} processing is done ............!")

file.close()

