from FastSAM.fastsam import FastSAM, FastSAMPrompt
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor
import supervision as sv
import roboflow
from roboflow import Roboflow
import os
import torch

model = FastSAM('./weights/FastSAM.pt')
DEVICE = 'cuda:0' if torch.cuda.is_available() else 'cpu'

folder = 'images/carne/'

# get every image in the folder
Images = []
for filename in os.listdir(folder):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):  # add or modify image file extensions as needed
        Images.append(filename)

for idx, img_name in enumerate(Images):
    path = os.path.join(folder, img_name)
    everything_results = model(path, device=DEVICE, retina_masks=True, imgsz=512, conf=0.80, iou=0.9)
    prompt_process = FastSAMPrompt(path, everything_results, device=DEVICE)
    ann = prompt_process.everything_prompt()
    output_filename = f'output_{idx}.jpg'
    output_path = os.path.join('./output/', output_filename)
    prompt_process.plot(annotations=ann, output_path=output_path)