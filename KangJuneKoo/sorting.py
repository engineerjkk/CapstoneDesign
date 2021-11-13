#선 조건 : 용량이 0KB TXT 파일은 직접 삭제해주어야 합니다.



import os
import shutil

Source_path = './DataSet/'
#Destination_path ='./DataSet/'

#숫자 정렬시키기
file_path = Source_path
file_names = os.listdir(file_path)
print(file_names)

i = 1

for name in file_names:
    if 'jpg' or 'png' in name:
        src = os.path.join(file_path, name)
        dst = str(i) + '.jpg'
        dst = os.path.join(file_path, dst)
        os.rename(src, dst)
        i += 1
print("Finished")