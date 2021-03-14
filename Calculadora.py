import PySimpleGUI as psg

class App:
    def __init__(self):
        # Layout.
        layout = [
            [psg.Text('Calculadora')],
            [psg.Input('0', key='display', size = (15, 1), text_color="Black", font=('Helvetica', 20))],
            [psg.Button('7'), psg.Button('8'), psg.Button('9'), psg.Button('C')],
            [psg.Button('4'), psg.Button('5'), psg.Button('6'), psg.Button('/')],
            [psg.Button('1'), psg.Button('2'), psg.Button('3'), psg.Button('*')],
            [psg.Button('0'), psg.Button('-'), psg.Button('+'), psg.Button('=')],
        ]
        self.result = 0
        self.oper = ''
        self.equacao = ''

        # Janela.
        self.janela = psg.Window('Calculadora', layout=layout, margins=(0,0), auto_size_buttons=False, return_keyboard_events=False, default_button_element_size=(5,2))
                     
    def iniciar(self):
        while True:
            self.event, self.values = self.janela.read()

            if self.event == psg.WIN_CLOSED:
                break
                
            elif self.event in ('0123456789'):
                self.equacao += self.event
                self.janela['display'].update(self.equacao)

            elif self.event in ('+-*/'):
                self.oper = self.event
                self.result = self.values['display']
                self.equacao += self.event
                self.janela['display'].update(self.equacao)
            
            elif self.event in ('='):
                self.result = self.operacao()
                self.equacao = str(self.result)
                self.janela['display'].update(self.result)
                self.result = 0
                self.oper = ''

    def operacao(self):
        if self.oper == '+':
            return float(self.result) + float(self.values['display'][self.values['display'].find('+') + 1])
        if self.oper == '-':
            return float(self.result) - float(self.values['display'][self.values['display'].find('-') + 1])
        if self.oper == '*':
            return float(self.result) * float(self.values['display'][self.values['display'].find('*') + 1])
        if self.oper == '/':
            return float(self.result) / float(self.values['display'][self.values['display'].find('/') + 1])

calculadora = App()
calculadora.iniciar()