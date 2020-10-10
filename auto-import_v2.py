
import os
from glob import glob
from pathlib import Path
result = list(Path(".").rglob("*.scss"))

# [filename, priority] 1-> the hightest priority
important_files = [['abstracts\_variables.scss',1],['abstracts\_mixins.scss',2],['abstracts\_functions.scss',3]]

# print(str(result[2]))

# print(result)
print("done");
tmp_simple_windows_path = 0
for simple_windows_path in result:
    for simple_important_file in important_files:
        if(str(simple_windows_path) == simple_important_file[0]):
            tmp_simple_windows_path = simple_windows_path
            result.remove(simple_windows_path);
            result.insert(simple_important_file[1], tmp_simple_windows_path);
            # print(result);



import_arr_path = []
for simple_import in result:
    simple_path = ''
    counter = len(simple_import._parts)
    if(simple_import._parts[0] != 'main.scss'):
        for simple_path_ele in simple_import._parts:
            if (counter == 1):
                simple_path = simple_path + simple_path_ele[1:-5]
            else:
                simple_path = simple_path + simple_path_ele + '/'
            counter = counter - 1
        double_quotes = '"'
        import_arr_path.append('@import ' + double_quotes +
                               simple_path + double_quotes+';')
# print(import_arr_path)

ready_import_text = ''

for simple_import_path in import_arr_path:
    ready_import_text = ready_import_text+simple_import_path+'\n'

print(ready_import_text)

f = open("main.scss", "w")
f.write(ready_import_text)
f.close()

os.system("pause")
