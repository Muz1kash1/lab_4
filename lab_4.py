import email
import imaplib
import codecs
import base64
spam_folder = "&BCEEPwQwBDw-"
in_folder = "INBOX"
email_adress = "muz1kash1@mail.ru"
parce_password = "f5YXQqfpDNdfPw7nRAWb"
mail = imaplib.IMAP4_SSL('imap.mail.ru')

mail.login(email_adress,parce_password)
mail.list()

mail.select(in_folder)


result, data = mail.uid('search', None, "ALL")
print(result)

latest_email_uid = data[0].split()[-20]
result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
print(result)

raw_email = data[0][1]
#print(raw_email)

email_message_raw = email.message_from_bytes(raw_email)

#print(email_message_raw)

def get_first_text_block(email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()

text_block = get_first_text_block(email_message_raw)
try:
    decoded_data = base64.b64decode(text_block)
    print("поломалось здесь")
    decoded_data = decoded_data.decode("UTF-8")
except (UnicodeDecodeError):
    print("не та кодировка")
    
    
print(decoded_data)

mail.logout()


# opyat izm
def brand_new_parse():
    print("brand_new_parse_action")
def brand_new_coding():
    print("brand_new_encoding")