from flask import *
import os
from database import *

admin = Blueprint('admin', __name__)

@admin.route('/adminhome', methods=['get', 'post'])
def adminhome():
    if not session.get("log_id") is None:
        return render_template('adminhome.html')
    else:
        return redirect(url_for('public.login'))

@admin.route('/adservices', methods=['get', 'post'])
def adservices():
    if session.get("log_id"):
        return render_template('adservices.html')  
    else:
        return redirect(url_for('public.login'))

@admin.route('/admanage_files', methods=['get', 'post'])
def admanage_files():
    if session.get("log_id"):
        files = os.listdir('files')  # Directory where files are stored
        return render_template('files.html', files=files)
    else:
        return redirect(url_for('public.login'))

@admin.route('/download/<filename>', methods=['get'])
def download_file(filename):
    if session.get("log_id"):
        return send_from_directory('files', filename, as_attachment=True)
    else:
        return redirect(url_for('public.login'))

@admin.route('/adviewusers', methods=['get', 'post'])
def adviewusers():
    if session.get("log_id"):
        return render_template('clientearnings.html')
    else:
        return redirect(url_for('public.login'))
         

@admin.route('/earnings_data', methods=['GET'])
def earnings_data():

    # Placeholder data
    data = [
        {'date': '2023-01-01', 'earnings': 100},
        {'date': '2023-02-01', 'earnings': 150},
        {'date': '2023-03-01', 'earnings': 200},
        {'date': '2023-04-01', 'earnings': 180},
        {'date': '2023-05-01', 'earnings': 300},
        {'date': '2023-06-01', 'earnings': 200},
        {'date': '2023-07-01', 'earnings': 750},
        {'date': '2023-08-01', 'earnings': 800},
        {'date': '2023-12-01', 'earnings': 100},
        {'date': '2024-01-01', 'earnings': 150},
        {'date': '2024-02-01', 'earnings': 200},
        {'date': '2024-03-01', 'earnings': 300},
        {'date': '2024-04-01', 'earnings': 300},
        {'date': '2024-05-01', 'earnings': 600},
    ]

    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')

    if start_date_str and end_date_str:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

        filtered_data = [entry for entry in data if start_date <= datetime.strptime(entry['date'], '%Y-%m-%d').date() <= end_date]
    else:
        filtered_data = data

    print("Returning earnings data:", filtered_data)  # Debug statement
    return jsonify(filtered_data)

@admin.route('/logout', methods=['get', 'post'])
def logout():
    session.clear()
    return redirect(url_for('public.login'))
