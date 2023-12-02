import pandas as pd
from sklearn.model_selection import train_test_split
import shutil
import os
import cv2

DATA_PATH = './datasets/data'

df = pd.read_table(os.path.join(DATA_PATH, 'annotations.tsv'))
x = df['filename'].to_numpy()
y = df[['x_from', 'y_from', 'width', 'height']].to_numpy()
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2, random_state=42)

try:
    os.makedirs(os.path.join(DATA_PATH, 'barcodes/images/train'))
    os.makedirs(os.path.join(DATA_PATH, 'barcodes/images/val'))
    os.makedirs(os.path.join(DATA_PATH, 'barcodes/labels/train'))
    os.makedirs(os.path.join(DATA_PATH, 'barcodes/labels/val'))
except Exception:
    pass

for idx in range(len(x_train)):
    shutil.copy(os.path.join(DATA_PATH, x_train[idx]), os.path.join(DATA_PATH, f"barcodes/images/train/{x_train[idx].split('/')[1]}"))
    image = cv2.imread(os.path.join(DATA_PATH, f"barcodes/images/train/{x_train[idx].split('/')[1]}"))
    with open(os.path.join(DATA_PATH, f"barcodes/labels/train/{x_train[idx].split('/')[1][:-3]}txt"), "w") as file:
        x_center = (y_train[idx][0] + y_train[idx][2] / 2) / image.shape[1]
        y_center = (y_train[idx][1] + y_train[idx][3] / 2) / image.shape[0]
        width_norm = y_train[idx][2] / image.shape[1]
        height_norm = y_train[idx][3] / image.shape[0]
        file.write(f"0 {x_center} {y_center} {width_norm} {height_norm}")

for idx in range(len(x_val)):
    shutil.copy(os.path.join(DATA_PATH, x_val[idx]), os.path.join(DATA_PATH, f"barcodes/images/val/{x_val[idx].split('/')[1]}"))
    image = cv2.imread(os.path.join(DATA_PATH, f"barcodes/images/val/{x_val[idx].split('/')[1]}"))
    with open(os.path.join(DATA_PATH, f"barcodes/labels/val/{x_val[idx].split('/')[1][:-3]}txt"), "w") as file:
        x_center = (y_val[idx][0] + y_val[idx][2] / 2) / image.shape[1]
        y_center = (y_val[idx][1] + y_val[idx][3] / 2) / image.shape[0]
        width_norm = y_val[idx][2] / image.shape[1]
        height_norm = y_val[idx][3] / image.shape[0]
        file.write(f"0 {x_center} {y_center} {width_norm} {height_norm}")