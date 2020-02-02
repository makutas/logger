import os
import datetime


class Logger:

    def __init__(self, logDir):
        self.logDir = os.path.abspath(logDir) #log failo direktorija, kuri eina kaip paramas
        self.log_file = None #log failo pavadinimas
        self.log_file_date = None #log failo sukurimo data

    def __open_log_file(self):
        if not os.path.exists(self.logDir): #tikrinam ar direktorija yra
            os.mkdir(self.logDir) #jei nera - sukuriam path
        self.log_file_date = str(datetime.datetime.now().date()) #dabartine data i string formata kad galima butu su "+"
        self.log_file = open(os.path.join(self.logDir, self.log_file_date + '-log.txt'), 'a+')
        #os.path.join() funkcija sujungia abspath(kas yra logDir vieta)
        # ir sukuria faila is datos ir _log.txt / a nes append i nuaja eilute
    def log(self, log_text):
        if self.log_file == None:
            self.__open_log_file()
        self.log_file.write(f'Log date: {datetime.datetime.now()} | Log name: {__class__.__name__} | Logged: {log_text} \n')

    def close_lof_file(self):
        self.log_file.close()
a = 5
b = 10

logger = Logger('./Logs')
logger.log(f'Mano isoriniai kintamieji yra {a} ir {b}')
logger.close_lof_file()