from flask import Flask, request, jsonify
from salesforce.SalesforceJobSeekerRecord import SalesforceJobSeekerRecord

app = Flask(__name__)

@app.route('/trigger', methods=['POST'])
def trigger():
    data = request.json
    
    print("📩 POSTデータを受信:", data)

    SalesforceJobSeekerRecord().update_resume(data)

    return jsonify({"status": "success", "received": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
