import glob
import shutil
import zipfile
import csv
import os


sourceFile = '../source/*'
while True:
    fileFound = glob.glob(sourceFile)
    if len(fileFound) > 0:
        for files in fileFound:

            if files.split('\\')[1].split('.')[1] == 'txt':
                shutil.copy(fileFound[0], '.')
                os.remove(fileFound[0])

                text = []
                fileName = './'+files.split('\\')[1]
                with open(fileName, 'r') as file:
                    lin = csv.reader(file)
                    for key, line in enumerate(lin):
                        text.append(line)
                file.close()

                firstText = text[0:10]
                secondText = text[0:20]
                thirdText = text[0:30]

                filesorce = fileFound[0].split('\\')[1].split('.')

                for i in range(1, 4):
                    setFileName = filesorce[0] + \
                        '_' + str(i) + '.' + filesorce[1]
                    with open(setFileName, 'w', encoding='utf-8') as file:
                        if i == 1:
                            file.write(str(firstText))
                        elif i == 2:
                            file.write(str(secondText))
                        elif i == 3:
                            file.write(str(thirdText))
                    file.close()

                comFileName = []
                comFilePathMain = './*'
                comFile = glob.glob(comFilePathMain)

                for i in range(len(comFile)):
                    if comFile[i].split('\\')[1].split('.')[1] == 'txt':
                        comFileName.append(comFile[i].split('\\')[1])

                with zipfile.ZipFile('final.zip', 'w') as zipFiles:
                    for file in comFileName:
                        zipFiles.write(
                            file, compress_type=zipfile.ZIP_DEFLATED)
                zipFiles.close()

                destination_path = '../destination/'
                zip_file = glob.glob('./*')

                for file in range(len(zip_file)):
                    if zip_file[file].split('\\')[1] == 'final.zip':
                        with zipfile.ZipFile('./final.zip', 'r') as zip_ref:
                            zip_ref.extractall(destination_path)

                delete_file_source_path = './*'
                delete_file_source = glob.glob(delete_file_source_path)

                for i in range(len(delete_file_source)):
                    if delete_file_source[i].split('\\')[1].split('.')[1] == 'txt':
                        os.remove(delete_file_source[i].split('\\')[1])

            if files.split('\\')[1].split('.')[1] == 'py':
                run_file_name = files.split('\\')[1]
                shutil.copy(fileFound[0], '.')
                os.system(f'python {run_file_name}')
                os.remove(fileFound[0])
                os.remove(run_file_name)
