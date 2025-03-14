from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management

@app.route('/')
def home():
    # Redirect to the agreement page if the user hasn't agreed
    if not session.get("agreed"):
        return redirect(url_for('user_agreement'))
    return render_template('index.html')  # Main page

@app.route('/user-agreement', methods=['GET', 'POST'])
def user_agreement():
    if request.method == 'POST':
        if request.form.get("agree") == "yes":
            session["agreed"] = True  # Store agreement in session
            return redirect(url_for('home'))  # Redirect to main page
        else:
            return redirect(url_for('access_denied'))  # Redirect if disagreed

    return render_template('agreement.html')  # Render agreement page

@app.route('/access-denied')
def access_denied():
    return render_template('access_denied.html')  # Show access denied page

@app.route('/logout')
def logout():
    session.pop("agreed", None)  # Clear session data
    return redirect(url_for('user_agreement'))

if __name__ == '__main__':
    app.run(debug=True)
