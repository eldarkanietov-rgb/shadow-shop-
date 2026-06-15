from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__, template_folder='.', static_folder='.', static_url_path='')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/news')
def news():
    return render_template('news.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_name = request.form.get('username')
        user_email = request.form.get('email')
        print(f"\n--- РЕГИСТРАЦИЯ: {user_name} ({user_email}) ---\n")
        return redirect(url_for('index'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)