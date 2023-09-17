from flask import Flask, request, jsonify
import requests


app = Flask('converter')


@app.route('/api/rates', methods=['GET'])
def convert_currency():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    value = request.args.get('value')

    payload = {}
    url = f'https://api.apilayer.com/exchangerates_data/convert?from={from_currency}&to={to_currency}&amount={value}'
    headers = {
        "apikey": "sT5AE0VSKZecIhO28TnRzqa57F5c3pmZ"
    }

    try:
        response = requests.request("GET", url, headers=headers, data = payload)

        if response.status_code == 200:
            result = response.json()
            result_value = result["result"]
            formatted_result = "{:.2f}".format(result_value)
            print(f'"result": {formatted_result}')
            return jsonify({"result": result})
        else:
            return jsonify({"error": "Ошибка при получении данных о курсе валют"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)


