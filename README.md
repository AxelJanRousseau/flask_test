# Flask server for Dag Van de Wetenschappen

This repo contains code for a minimal setup to generate a story and image for children at the dag van de wetenschappen science fair.
I am aware this code is janky, and a flask server is overkill / not needed for this simple task. However, Python is what i know, and what I wanted to stick to. 

## Instructions:
1. Download code
2. Install Python and dependencies: ```pip install --upgrade Flask openai python-dotenv```
3. create .env file containing your API key: ```OPENAI_API_KEY="your_key_here"```
4. Run ```flask --app main.py run ``` and navigate to http://127.0.0.1:5000/
