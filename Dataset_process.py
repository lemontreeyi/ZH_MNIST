import os
import shutil
root_dir = "Raw_Dataset"
img_list = os.listdir(root_dir)
total_len = len(img_list)

train_dir = "Data/train_data"
valid_dir = "Data/valid_data"
test_dir = "Data/test_data"
for i in range(0, total_len, 15):
    for j in range(2):
        old_path = os.path.join(root_dir, img_list[i+j])
        if i < 10500:
            new_path = os.path.join(train_dir, f"{j+9}")
        elif 10500 <= i < 13500:
            new_path = os.path.join(valid_dir, f"{j+9}")
        else:
            new_path = os.path.join(test_dir, f"{j+9}")
        shutil.move(old_path, new_path)
    for j in range(9):
        old_path = os.path.join(root_dir, img_list[i+j+6])
        if i < 10500:
            new_path = os.path.join(train_dir, f"{j}")
        elif 10500 <= i < 13500:
            new_path = os.path.join(valid_dir, f"{j}")
        else:
            new_path = os.path.join(test_dir, f"{j}")
        shutil.move(old_path, new_path)
