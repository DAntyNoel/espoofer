def read_mail(file = 'mail.txt'):
	import os
	# './canvas_notification.html'
	with open(file, 'r') as f:
		str = f.read()
		f.close()

	return str.encode()

def load_password():
    with open('password.txt', 'r') as f:
        password = f.read()
    return password.encode() 


config = {
	"attacker_site": b"sjtu.edu.cn", # attack.com
	"legitimate_site_address": b'canvas@sjtu.edu.cn', # From header address displayed to the end-user
	"victim_address": b"dantynoel@88.com", # RCPT TO and message.To header address, 
	"case_id": b"client_2", #  You can find all case_id using -l option.

	# The following fields are optional
	"server_mode":{
		"recv_mail_server": "", # If no value, espoofer will query the victim_address to get the mail server ip
		"recv_mail_server_port": 25,
		"starttls": False,
	},
	"client_mode": {
		"sending_server": ("mail.sjtu.edu.cn", 25),
		"username": b"dantynoel@sjtu.edu.cn",
		"password": b"Ars1027ars",
	},

	# Optional. You can leave them empty or customize the email message header or body here
	"subject_header": b"",  # Subject: Test espoofer\r\n
	"to_header": b"", # To: <alice@example.com>\r\n
	"body": b"", # Test Body.

	# Optional. Set the raw email message you want to sent. It's usually used for replay attacks
	"raw_email": b"", 
}




