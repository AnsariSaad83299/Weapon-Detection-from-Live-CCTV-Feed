from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="" #place ur api key
)

result = CLIENT.infer('test-image.png', model_id="wpn_pintol_di_kita/1")

print(result)
