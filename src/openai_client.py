import openai

from tenacity import (
    retry,
    stop_after_attempt,
    retry_if_not_exception_type,
    stop_after_delay,
    wait_exponential
)

class OpenAIClient:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    @retry(
        wait=wait_exponential(min=1, max=10), 
        stop=(stop_after_attempt(5) | stop_after_delay(30)),
        retry=retry_if_not_exception_type(openai.error.InvalidRequestError))
    def create_image(self, prompt: str):
        response = openai.Image.create(prompt=prompt)
        image_url = response['data'][0]['url']
        return image_url

