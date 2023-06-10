from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    # Define the image URL and background color
    image_url = 'https://i.pravatar.cc/300'
    current_date = datetime.now()
    month = current_date.strftime('%B')
    day = current_date.strftime('%d')

    formatted_month = ''
    if month == '01':
        formatted_month = 'January'
    elif month == '02':
        formatted_month = 'February'
    elif month == '03':
        formatted_month = 'March'
    elif month == '04':
        formatted_month = 'April'
    elif month == '05':
        formatted_month = 'May'
    elif month == '06':
        formatted_month = 'June'
    elif month == '07':
        formatted_month = 'July'
    elif month == '08':
        formatted_month = 'August'
    elif month == '09':
        formatted_month = 'September'
    elif month == '10':
        formatted_month = 'October'
    elif month == '11':
        formatted_month = 'November'
    elif month == '12':
        formatted_month = 'December'

    formatted_day = day
    if day.endswith('1') and not day.endswith('11'):
        formatted_day += 'st'
    elif day.endswith('2') and not day.endswith('12'):
        formatted_day += 'nd'
    elif day.endswith('3') and not day.endswith('13'):
        formatted_day += 'rd'
    else:
        formatted_day += 'th'

    formatted_date = f'{formatted_day} {month} {current_date.strftime("%Y")}'
    external_url='https://picsum.photos/'
    return render_template('index.html',image_url=image_url, current_date=formatted_date,external_url=external_url)
if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
