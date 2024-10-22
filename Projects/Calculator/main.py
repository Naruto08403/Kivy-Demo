from kivymd.app import MDApp
from kivy.lang import Builder


class CalculatorApp(MDApp):
    done = False # tag to let us know the user press equals
    def build(self):
        return Builder.load_file('cal.kv')
    
    def clicked(self,text):
        expression = self.root.ids.textbox.text
        if text =='.' and '.' in expression:
            return
        
        if text in '+-x/':
            if  expression.endswith(('+','-','x','/')):
                expression = expression[:-1]
                self.root.ids.textbox.text = expression+text   
            
            else:
                self.root.ids.textbox.text += text 
            
            if self.done:
                self.done = False
            return
 
        
        if text == '=':
            # make sure to replace the x to * for multiplication
            answer = eval(expression.replace('x','*'))
            self.root.ids.textbox.text = str(answer)
            self.done = True
            return
        
        # if the user just press equals and press any number again
        if self.done:
            self.root.ids.textbox.text = '0'
        
        #if the textbox's text is 0
        if self.root.ids.textbox.text == '0':
            self.root.ids.textbox.text = ''

        self.root.ids.textbox.text += text


if __name__ == '__main__':
    CalculatorApp().run()