from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
from visualize import solve_sudoku_from_image
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['image']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        solved_image_path = solve_sudoku_from_image(file_path)
        return send_from_directory(app.config['UPLOAD_FOLDER'], 'sudoku_solution.jpg', as_attachment=True)
    return render_template('index.html')

@app.route('/solve_sudoku', methods=['POST'])
def solve_sudoku():
    file = request.files['image']
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    solved_image_path = solve_sudoku_from_image(file_path)
    return '/static/uploads/sudoku_solution.jpg'

if __name__ == '__main__':
    app.run(debug=True)