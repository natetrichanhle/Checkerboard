from flask import Flask, render_template  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def route():
    return render_template('index.html', x = 8, y= 8, color1 = 'red', color2 = 'black')

@app.route('/<int:y>')
def change(y):
    return render_template('index.html', x = 8, y=y, color1 = 'red', color2 = 'black')

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def checkerboard(x,y,color1,color2):
    return render_template('index.html', x = x, y = y, color1 = color1, color2 = color2)

@app.errorhandler(404)
def error(error):
    return f'Page not found'

if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
