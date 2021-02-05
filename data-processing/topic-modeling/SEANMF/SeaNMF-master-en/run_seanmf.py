import os
from tqdm import trange

os.system("python data_process.py")

for i in trange(5,55,5):
    command = f"python train.py --n_topics {i} > output{i}t.txt && python vis_topic.py >> output{i}t.txt"
    os.system()
    # print(command)
