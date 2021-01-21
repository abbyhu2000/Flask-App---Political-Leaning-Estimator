from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('base.html')

@app.route('/background_process', methods=['POST', 'GET'])
def background_process():
    slider1value = float(request.args.get('slider1value'))
    slider2value = float(request.args.get('slider2value'))
    slider3value = float(request.args.get('slider3value'))
    slider4value = float(request.args.get('slider4value'))
    slider5value = float(request.args.get('slider5value'))
    slider1original = float(request.args.get('slider1original'))
    slider2original = float(request.args.get('slider2original'))
    slider3original = float(request.args.get('slider3original'))
    slider4original = float(request.args.get('slider4original'))
    slider5original = float(request.args.get('slider5original'))
    source1 = float(request.args.get('source1'))
    source2 = float(request.args.get('source2'))
    source3 = float(request.args.get('source3'))
    source4 = float(request.args.get('source4'))
    source5 = float(request.args.get('source5'))
    print(request.args)
    pred = (slider1value-slider1original)*source1+(slider2value-slider2original)*source2+(slider3value-slider3original)*source3+(slider4value-slider4original)*source4+(slider5value-slider5original)*source5

    print(pred)
    
    return jsonify({'prediction_value': pred})

if __name__ == "__main__":
    app.run(debug=True)