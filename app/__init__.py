from flask import Flask
from app.controllers.nlp_controller import NLPController

app = Flask(__name__)
app.config.from_object('app.config.Config')

nlp_controller = NLPController()

@app.route('/api/nlp/gpt', methods=['POST'])
def gpt_nlp():
    return nlp_controller.gpt_nlp()

if __name__ == '__main__':
    app.run()
