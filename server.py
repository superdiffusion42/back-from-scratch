from dotenv import load_dotenv
from sanic import Sanic
from sanic.response import text

import prompt as prompt

load_dotenv()

prompt.loadPretrainedModelFromHuggingFace()

api = Sanic("test_api")

@api.get("/health")
async def health(request):
    return text("OK")

@api.post("/generate")
async def generate(request):
    try:
        model_inputs = response.json.loads(request.json)
    except:
        model_inputs = request.json

    output = prompt.generate(model_inputs)

    return response.json(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)