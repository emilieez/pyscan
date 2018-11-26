from imaplib import IMAP4_SSL, IMAP4
from os import mkdir, path, rename, remove
from base64 import b64encode, b64decode
from glob import glob
from zipfile import ZipFile
import email.header

class MailParser:
    """ Parses emails for files sent by the Scanner application
    """

    def __init__(self, email, password):
        """ Uses user input email and password to login to retrieve mesh files

        Arguments:
            email {string} -- user's email
            password {string} -- user's password
        """

        self.email = email
        self.password = b64encode(password.encode('ascii'))

        self.__assignHost(self.email)
        self.error = False

    def __assignHost(self, email_str):
        """ determines the host address based on the user email input

        Arguments:
            email_str {string} -- email pulled from the user input
        """
        try:
            email_str = self.email.split('@')
            if email_str[1] == 'outlook.com':
                self.host = 'imap-mail.' + email_str[1]
            elif email_str[1] == 'gmail.com':
                self.host = 'imap.' + email_str[1]
        except IndexError or TypeError:
            self.error = "Please use an Outlook email or Gmail"


    def __connectToServer(self):
        """ Connects to email server

        Returns:
            mailbox -- connection to email server database
        """

        try:
            print('Connecting to ' + self.host)
            return IMAP4_SSL(self.host)
        except AttributeError:
            self.error = "Unable to connect to Email service"

    def __login(self, mailbox):
        """ Uses login credentials to access email server

        Arguments:
            mailbox {mailbox} -- connection to email server database

        Returns:
            list -- list of all the emails in the inbox
        """

        try:
            mailbox.login(self.email, b64decode(self.password).decode('ascii'))
            print('Login Successful')
            return mailbox.list()
        except IMAP4.error or TypeError:
            self.error = 'Incorrect Email or Password'

    def downloadAttachments(self, email_message, list):
        """ downloads attachments from the users email

        Arguments:
            email_message {object} -- current email message

        Returns:
            filepath -- filepath of the saved objects
        """
        directory = path.join(path.dirname(path.realpath(__file__)), "scans")
        fileName = ""
        # downloading attachments

        for x in range(len(list)):
            for y in range(len(email_message)):
                for part in email_message[y].walk():
                    if part.get_content_maintype() == 'multipart':
                        continue
                    if part.get('Content-Disposition') is None:
                        continue
                    try:
                        mkdir(directory)
                    except:
                        pass
                        if part.get_content_type() == 'application/zip' and email_message[y].get('subject') == str(list[x]):
                            open(path.join(directory, '%s.zip' %
                                           str(list[x])), 'wb').write(part.get_payload(decode=True))
                            unzipfile = ZipFile(
                                path.join(directory, '%s.zip' % str(list[x])), 'r')
                            unzipfile.extractall(
                                directory)
                            unzipfile.close()
                            try:
                                num = int(glob(path.join(directory, '{0}(?).obj').format(
                                    str(list[x])))[-1].split('(')[1].split(')')[0]) + 1
                            except IndexError:
                                num = 0
                            rename(path.join(directory, 'Model.obj'),
                                   path.join(directory, '{0}({1}).obj'.format(str(list[x]), num)))
                            remove(path.join(directory,
                                             '%s.zip' % str(list[x])))
                            filelist = glob(path.join(directory, '*.mtl')) + \
                                glob(path.join(directory, '*.jpg'))
                            for i in filelist:
                                remove(i)

    def get_scan(self):
        list = []
        email_message = ''
        mailBox = self.__connectToServer()
        try:
            log_stat = self.__login(mailBox)
            try:
                mailBox.select()
                searchQuery = '(BODY "SDK")'
                result, data = mailBox.uid('search', None, searchQuery)
                ids = data[0]
                # list of uids
                id_list = ids.split()
                y = []
                i = len(id_list)
                for x in range(i):
                    latest_email_uid = id_list[x]

                    # fetch the email body (RFC822) for the given ID
                    result, email_data = mailBox.uid(
                        'fetch', latest_email_uid, '(RFC822)')
                    raw_email = email_data[0][1]
                    raw_email_string = raw_email.decode('utf-8')
                    email_message = email.message_from_string(raw_email_string)
                    subject = email.message_from_string(raw_email_string).get('subject')
                    y.insert(0,email_message)
                    list.insert(0,subject)
                # mailBox.close()
                # mailBox.logout()
                return [log_stat,list,y,mailBox]
            except IMAP4.error:
                self.error = "Unable to connect to Email service"
        except AttributeError:
            pass

    def logout(self, mailBox):
        mailBox.close()
        mailBox.logout()

if __name__ == '__main__':
    # credentials.py is a local file containing email credentials; hidden on GitHub by .gitignore
    import credentials as creds
    parser = MailParser(creds.OUTLOOK_EMAIL, creds.GMAIL_PASSWORD)
    i = parser.get_scan()
    parser.downloadAttachments(i[2], ['Cube_Test03_BoxSize_Small', 'Cube_Test02_BoxSize_Medium', 'Cube_Test_01_BoxSize_Large'])
    parser.logout(i[-1])
