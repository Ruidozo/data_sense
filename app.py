from analytics.analytics_list import get_analytics_list
from analytics.analytics_store import store_analytics
from charts import ChartFactoryRegistry
from config.json_params import get_json_params
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from user.user_state import (generate_chart_for_user, get_user_charts,
                             get_user_state)

app = Flask(__name__)
CORS(app)


@app.route('/config', methods=['GET'])
def config():
    return send_from_directory('static', 'config.html')


@app.route('/json-params', methods=['GET'])
def json_params():
    return jsonify(get_json_params())


@app.route('/user', methods=['POST'])
def user():
    data = request.get_json()
    if not data or 'activityId' not in data or 'userId' not in data:
        return jsonify({"status": "error", "message": "activityId e userId são obrigatórios"}), 400
    return jsonify(get_user_state(data['activityId'], data['userId']))


@app.route('/analytics-list', methods=['GET'])
def analytics_list():
    return jsonify(get_analytics_list())


@app.route('/analytics', methods=['POST'])
def analytics():
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "Nenhum dado recebido"}), 400
    return jsonify(store_analytics(data))


@app.route('/generate-chart', methods=['POST'])
def generate_chart():
    data = request.get_json()
    if not data or 'activityId' not in data or 'userId' not in data or 'chartType' not in data:
        return jsonify({"status": "error", "message": "activityId, userId e chartType são obrigatórios"}), 400
    return jsonify(generate_chart_for_user(data['activityId'], data['userId'], data['chartType'], data.get('data', {})))


@app.route('/user-charts/<activity_id>/<user_id>', methods=['GET'])
def user_charts(activity_id, user_id):
    charts = get_user_charts(activity_id, user_id)
    return jsonify({"activityId": activity_id, "userId": user_id, "totalCharts": len(charts), "charts": charts})


@app.route('/chart-types', methods=['GET'])
def chart_types():
    return jsonify({"availableTypes": ChartFactoryRegistry().get_available_types()})


@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "name": "DataSense Activity Provider",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "config": "/config",
            "json_params": "/json-params",
            "user": "/user",
            "analytics_list": "/analytics-list",
            "analytics": "/analytics"
        }
    })


if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=False)
