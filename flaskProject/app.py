from flask import Flask, redirect, url_for, render_template
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home_func():  # put application's code here
    return render_template('CV.html')

@app.route('/Catalog')
def Catalog_func():  # put application's code here
    return render_template('Catalog.html')

@app.route('/assignment8')
def assignment8_func():  # put application's code here
   # found = True

    #if found:
        return render_template('assignment8.html',
                               profile={'name': 'Noy', 'second_name': 'Sekal'},
                               university='BGU',
                               degrees=['BA', 'Mc'],
                               hobbies=('art', 'dance', 'music', 'dogs', 'web'))
    #else:
     #   return render_template('assignment8.html')


if __name__ == '__main__':
    app.run()
