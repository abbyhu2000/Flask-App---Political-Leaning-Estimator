from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('base.html')

@app.route('/background_process', methods=['GET'])
def background_process():
    number_of_slider = 5
    slider_upated = []
    slider_original = [0, 0.75, 1, 0, 0.5]
    source = [1, 0.5, -0.5, -1, 0]
    pred = 0
    for i in range(number_of_slider):
        curr_slider = "slider"+str(i+1)+"value"
        #slider_upated.append(float(request.args.get(curr_slider)))
        curr_value = float(request.args.get(curr_slider))
        pred += (curr_value-slider_original[i])*source[i]
   

    print(pred)
    
    return jsonify({'prediction_value': pred})

if __name__ == "__main__":
    app.run(debug=True)