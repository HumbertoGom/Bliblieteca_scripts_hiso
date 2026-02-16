class log:
    def _log(self,msg):
        raise NotImplementedError('Implemente o método log')

class Logfilemixin(log):
    def _log(self,msg):
        print(msg)

class logprintmixin(log):
    def _log(self,msg):
        print(f'{msg} {self.__class__.__name__}')
l= log()
l._log('qlq coisa')