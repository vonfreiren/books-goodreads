import yagmail
from auxiliar import personal_information


def notify(subject, message, filepath):

    yag = yagmail.SMTP(personal_information.sender_email, oauth2_file='/Users/javier/PycharmProjects/books-goodreads/credentials/oauth.json')
    yag.send(to=personal_information.to_email, subject=subject, contents=message, attachments=filepath, cc=personal_information.cc_email)

