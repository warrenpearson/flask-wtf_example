from flask import Flask, render_template, request, flash
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        print "it's a post"
        if form.validate() == False:
            print 'not valid'
            flash('All fields are required.', 'error')
            return render_template('contact.html', form=form)
        else:
            print 'success'
            return render_template('success.html')
    elif request.method == 'GET':
        print "it's a get"
        return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
