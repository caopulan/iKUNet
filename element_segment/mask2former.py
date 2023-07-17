import requests
import torch
from PIL import Image
from transformers import AutoImageProcessor, Mask2FormerForUniversalSegmentation


class Mask2Former:
    def __init__(self):
        self.processor = AutoImageProcessor.from_pretrained("facebook/mask2former-swin-large-coco-instance")
        self.model = Mask2FormerForUniversalSegmentation.from_pretrained("facebook/mask2former-swin-large-coco-instance")

    def __call__(self, image, class_id=0, mask_threshold=0.1):
        inputs = self.processor(images=image, return_tensors="pt")

        with torch.no_grad():
            outputs = self.model(**inputs)

        result = self.processor.post_process_instance_segmentation(
            outputs,
            mask_threshold=mask_threshold,
            target_sizes=[image.size[::-1]]
        )[0]

        mask = torch.zeros(image.size[::-1])
        for segment in result["segments_info"]:
            if segment["label_id"] == class_id:
                mask = result["segmentation"] == segment["id"]
                break
        return mask


if __name__ == '__main__':
    mask2former = Mask2Former()

    for img_path in glob.glob("samples/demo1/*"):
        image = Image.open(img_path)
        result = mask2former(image)

