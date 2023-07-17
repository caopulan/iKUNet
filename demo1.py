import torch
import tqdm
from element_segment.mask2former import Mask2Former
import imageio
import glob
from PIL import Image


if __name__ == '__main__':
    mask2former = Mask2Former()

    # reader = imageio.get_reader('demo1.flv')
    # for image in reader:
    for img_path in tqdm.tqdm(glob.glob("samples/demo1/*.png")):
        image = Image.open(img_path)

        result = mask2former(image)
        # save result
        result = result.to(torch.int8) * 255
        im = Image.fromarray(result.numpy().astype("uint8"))
        im.save(img_path.replace("demo1", "demo1_mask"))

        print()# save class=0 instance map