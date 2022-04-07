import logging 

# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.basicConfig(filename='app.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

from flask import Flask, request, jsonify

from helpers import get_net_usage, OFFSET


app = Flask(__name__)

@app.route('/get-usage')
def index():
    try:
        rc, tr, ttl = get_net_usage("GB")
        data = {
            "recieved": rc + OFFSET["recieved"],
            "transferred": tr + OFFSET["transferred"],
            "total": ttl + OFFSET["total"]
        }
        return jsonify(data)
        
    except Exception as e:
        logging.exception(e)
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=2277)