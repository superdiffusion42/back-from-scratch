import os

def loadPretrainedModelFromHuggingFace():
    # TODO Is there a better way than having a global variable ?
    #global model
    HF_AUTH_TOKEN = getEnvironmentVariableOrThrow("HF_AUTH_TOKEN")
    HF_PRETRAINED_MODEL_VERSION = getEnvironmentVariableOrThrow("HF_PRETRAINED_MODEL_VERSION")

    #model = StableDiffusionPipeline.from_pretrained(HF_PRETRAINED_MODEL_VERSION, scheduler=generateScheduler(), use_auth_token=HF_AUTH_TOKEN).to("cuda")

# TODO Document what is a scheduler
#def generateScheduler():
#    return LMSDiscreteScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear")

def getEnvironmentVariableOrThrow(variableName: str)-> str:
    var = os.getenv(variableName)
    if var is None:
        raise Exception(f'{variableName} environment variable is not defined aborting')

    return var