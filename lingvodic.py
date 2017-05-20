import os
import _io
import sys
import csv
from time import sleep
import re

def main():

    datafolder = r'/home/tm/data/pycharm/lingvodic/'
    annotfolder = datafolder + r'annotations/'
    dictionfolder = datafolder + r'dictionaries_good/'
    annotfiles = os.listdir(annotfolder)
    dictionfiles = os.listdir(dictionfolder)
    annotout = r'allanot.csv'
    dictionout = r'alldiction.csv'

    #parse_dictionary_files
    with open(datafolder + dictionout, 'a') as csvfile:
        fieldnames = ['dictionary_file', 'dic_name', 'dic_index_lang', 'dic_contents_lang', 'keyword', 'translation']
        writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=fieldnames)
        if os.stat(datafolder + dictionout).st_size == 0:
            writer.writeheader()
        for f in dictionfiles:
            df = dictionfolder + f
            counter = 0
            dic_name = ''
            dic_index_lang = ''
            dic_contents_lang = ''
            keyword = ''
            try:
                with _io.open(df,'r',encoding='utf-16-le') as dictionary_file:
                    for line in dictionary_file:
                        counter +=1
                        if re.match(r'[ \t]', line):
                            writer.writerow({'dictionary_file': f, 'dic_name': str(dic_name), 'dic_index_lang': str(dic_index_lang), 'dic_contents_lang': str(dic_contents_lang), 'keyword': str(keyword), 'translation': str(line)})
                        elif '#NAME' in line and counter < 5:
                            dic_name = line.split('"')[1]
                        elif '#INDEX_LANGUAGE' in line and counter < 5:
                            dic_index_lang = line.split('"')[1]
                        elif '#CONTENTS_LANGUAGE' in line and counter < 5:
                            dic_contents_lang = line.split('"')[1]
                        else:
                            keyword = line
            except:
                pass

    #parse_annotation_files
    # with open(datafolder + annotout, 'a') as csvfile:
    #     fieldnames = ['annotation_file', 'annotation_text']
    #     writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=fieldnames)
    #     writer.writeheader()
    #     for f in annotfiles:
    #         af = annotfolder + f
    #         try:
    #             with _io.open(af, 'r', encoding='utf-16-le') as annotation_file:
    #                 content = annotation_file.readlines()
    #         except:
    #             content = 'annotation is corrupted'
    #         try:
    #             writer.writerow({'annotation_file': f, 'annotation_text': str(content)})
    #         except:
    #             writer.writerow({'annotation_file': f, 'annotation_text': 'annotation is corrupted'})


if __name__ == "__main__":
    sys.exit(int(main() or 0))