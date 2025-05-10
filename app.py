from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from weather_agent import agent  # Import the agent created in weather_agent.py
from flask_cors import CORS


load_dotenv()

app = Flask(__name__)
CORS(app)
@app.route('/query', methods=['POST'])
def ask_weather_agent():
    try:
        data = request.get_json()
        query = data.get('query')
        if not query:
            return jsonify({'error': 'Query field is required'}), 400

        response = agent.query(query)
        return jsonify({'response': str(response)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
