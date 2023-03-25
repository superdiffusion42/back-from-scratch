import os
from diffusers import StableDiffusionPipeline, LMSDiscreteScheduler
import torch
from torch import autocast
import base64
from io import BytesIO

def loadPretrainedModelFromHuggingFace():
    # TODO Is there a better way than having a global variable ?
    global model
    HF_AUTH_TOKEN = getEnvironmentVariableOrThrow("HF_AUTH_TOKEN")
    HF_PRETRAINED_MODEL_VERSION = getEnvironmentVariableOrThrow("HF_PRETRAINED_MODEL_VERSION")

    model = StableDiffusionPipeline.from_pretrained(HF_PRETRAINED_MODEL_VERSION, scheduler=generateScheduler(), use_auth_token=HF_AUTH_TOKEN).to("cuda")

# TODO Document what is a scheduler
def generateScheduler():
    return LMSDiscreteScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear")

def getEnvironmentVariableOrThrow(variableName: str)-> str:
    var = os.getenv(variableName)
    if var is None:
        raise Exception(f'{variableName} environment variable is not defined aborting')

    return var

# This fails with a OOM error
def generate(model_inputs:dict) -> dict:
    global model

    # Parse out your arguments
    prompt = model_inputs.get('prompt', None)
    height = model_inputs.get('height', 256)
    width = model_inputs.get('width', 256)
    num_inference_steps = model_inputs.get('num_inference_steps', 5)
    guidance_scale = model_inputs.get('guidance_scale', 7.5)
    input_seed = model_inputs.get("seed",None)

    #If "seed" is not sent, we won't specify a seed in the call
    generator = None
    if input_seed != None:
        generator = torch.Generator("cuda").manual_seed(input_seed)

    if prompt == None:
        return {'message': "No prompt provided"}

    # Run the model
    with autocast("cuda"):
        result = model(prompt,height=height,width=width,num_inference_steps=num_inference_steps,guidance_scale=guidance_scale,generator=generator)
        image = result.images[0]

    buffered = BytesIO()
    image.save(buffered,format="JPEG")
    image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

    # Return the results as a dictionary
    return {'image_base64': image_base64}