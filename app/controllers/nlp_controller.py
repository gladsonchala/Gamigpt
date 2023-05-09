from flask import request, jsonify
from app.models.gpt_model import GPTModel

class NLPController:
    def __init__(self):
        self.gpt_model = GPTModel()

    def gpt_nlp(self):
        data = request.get_json()
        text = data.get('text')

        if not text:
            return jsonify({'error': 'Missing text parameter'}), 400

        result = self.gpt_model.predict(text)

        return jsonify({'result': result}), 200
