from diffusers import StableDiffusionPipeline
import torch

# Use a local Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2", torch_dtype=torch.float16)
pipe = pipe.to("cuda")  # Use GPU if available

def generate_image(prompt):
    image = pipe(prompt).images[0]
    image_path = "generated_image.png"
    image.save(image_path)
    return image_path