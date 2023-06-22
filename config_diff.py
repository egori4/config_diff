import difflib
import os


if not os.path.exists('Report'):
	os.makedirs('Report')

if not os.path.exists('Config'):
	os.makedirs('Config')

config_path = "./Config/"
report_path = "./Report/"
file_name_prefix_length = 8

def diff(first_file, second_file):

    first_file_lines = open(config_path + first_file).readlines()
    second_file_lines = open(config_path + second_file).readlines()
    difference = difflib.HtmlDiff().make_file(first_file_lines, second_file_lines, first_file , second_file)
    difference_report = open(report_path + 'difference_report_'+first_file +'.html','w')
    difference_report.write(difference)
    difference_report.close()




files_list = os.listdir(config_path)

pairs_list = []

for file1 in files_list:
    first_file = file1
    
    for file2 in files_list:
        if file1 == file2:
            continue
        
        if file1[:file_name_prefix_length] == file2[:file_name_prefix_length]:
            if file1 not in pairs_list and file2 not in pairs_list:
                pairs_list.append(file1)
                pairs_list.append(file2)
                second_file =  file2
                diff(first_file,second_file)
    



