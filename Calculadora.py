import PySimpleGUI as psg

class Interface:
    def __init__(self):
        # Layout.
        layout = [
            [psg.Text('Calculadora')],
            [psg.Text('', key='mostrador', size = (10, 1), text_color="White", font=('Helvetica', 18))],
            [psg.Button('7'), psg.Button('8'), psg.Button('9')],
            [psg.Button('4'), psg.Button('5'), psg.Button('6')],
            [psg.Button('1'), psg.Button('2'), psg.Button('3')],
            [psg.Button('+'), psg.Button('0'), psg.Button('=')],
        ]

        # Janela.
        self.janela = psg.Window('Calculadora', layout, auto_size_buttons=False, default_button_element_size=(5,2),)
    
    def calcular(self):
        elementos = 0
        equacao = ''
        while True:
            self.event, self.values = self.janela.Read()
            if(self.event == psg.WIN_CLOSED):
                print
                break

            elif(self.event in '0123456789'):
                elementos = elementos + int(self.event)
                equacao = equacao + self.event
                self.janela['mostrador'].update(equacao)

            elif(self.event == '+'):
                equacao = equacao + self.event
                self.janela['mostrador'].update(equacao)

            elif(self.event == '='):
                self.janela['mostrador'].update(elementos)
            
calc = Interface()
calc.calcular()