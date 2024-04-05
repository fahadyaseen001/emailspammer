from flask import Flask, request, jsonify
import smtplib


app = Flask(__name__)


@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.json
    email = data.get('email')

    if not email:
        return jsonify({'success': False, 'message': 'Email address not provided'}), 400

    toaddrs = email
    fromaddrs = 'sam404967@gmail.com'
    message = 'Hi MaxCodez, I am amazing!'

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtpserver:
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login('sam404967@gmail.com', 'oasb yxrv mkva tkxk')
            for i in range(2):
             smtpserver.sendmail(fromaddrs, toaddrs, message)
             print(i)
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

    return jsonify({'success': True}), 200

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
