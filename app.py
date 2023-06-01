from flask import Flask, render_template, request

app = Flask(__name__)

pushup_count = 0  # Jumlah push up awal

@app.route('/')
def home():
    return render_template('index.html', count=pushup_count)

@app.route('/increment', methods=['POST'])
def increment():
    global pushup_count
    pushup_count += 1
    return str(pushup_count)

if __name__ == '__main__':
    app.run(debug=True)