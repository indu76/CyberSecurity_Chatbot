from flask import Flask, request, jsonify
from flask_cors import CORS
from retriever import get_answer

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend to communicate with backend

@app.route('/chat', methods=['POST'])
def chat():
    """
    API endpoint that accepts a user message and returns chatbot response.
    Expected JSON: {"message": "user question here"}
    Returns JSON: {"response": "chatbot answer here"}
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Check if message exists in request
        if not data or 'message' not in data:
            return jsonify({"error": "Missing 'message' field in request"}), 400
        
        user_message = data['message']
        
        # Check if message is not empty
        if not user_message or not user_message.strip():
            return jsonify({"error": "Message cannot be empty"}), 400
        
        # Get answer from retriever
        answer = get_answer(user_message)
        
        # Return response as JSON
        return jsonify({"response": answer}), 200
        
    except Exception as e:
        # Handle any errors
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    # Run Flask app on localhost:5000
    app.run(debug=True, host='0.0.0.0', port=5000)
