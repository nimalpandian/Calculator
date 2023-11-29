import ipywidgets as widgets
from IPython.display import display
import math

class Calculator:
    def __init__(self):
        self.operator = ""
        self.memory = 0
        self.output = widgets.Output()
        self.create_gui()

    def click_button(self, value):
        self.operator = self.operator + str(value)
        with self.output:
            print(self.operator)

    def clear(self):
        self.operator = ""
        self.output.clear_output()

    def clear_entry(self):
        self.operator = self.operator.rsplit(' ', 1)[0]
        with self.output:
            print(self.operator)

    def delete_char(self):
        self.operator = self.operator[:-1]
        with self.output:
            print(self.operator)

    def change_sign(self):
        if self.operator and self.operator[0] == '-':
            self.operator = self.operator[1:]
        else:
            self.operator = '-' + self.operator
        with self.output:
            print(self.operator)

    def calculate_percentage(self):
        try:
            result = eval(self.operator)
            result /= 100
            self.operator = str(result)
            with self.output:
                print(result)
        except Exception as e:
            with self.output:
                print(f"Error: {str(e)}")

    def memory_plus(self):
        try:
            value = eval(self.operator)
            self.memory += value
        except Exception as e:
            with self.output:
                print(f"Error: {str(e)}")

    def memory_minus(self):
        try:
            value = eval(self.operator)
            self.memory -= value
        except Exception as e:
            with self.output:
                print(f"Error: {str(e)}")

    def memory_store(self):
        try:
            self.memory = eval(self.operator)
        except Exception as e:
            with self.output:
                print(f"Error: {str(e)}")

    def memory_read(self):
        with self.output:
            print(self.memory)

    def memory_clear(self):
        self.memory = 0
        with self.output:
            print("Memory Cleared")

    def evaluate(self):
        try:
            result = eval(self.operator)
            self.operator = str(result)
            with self.output:
                print(result)
        except Exception as e:
            with self.output:
                print(f"Error: {str(e)}")

    def sin_function(self):
        try:
            result = math.sin(math.radians(float(self.operator)))
            self.operator = str(result)
            with self.output:
                print(result)
        except Exception as e:
            with self.output:
                print(f"Error: {str(e)}")

    def reciprocal(self):
        try:
            value = eval(self.operator)
            result = 1 / value
            self.operator = str(result)
            with self.output:
                print(result)
        except Exception as e:
            with self.output:
                print(f"Error: {str(e)}")

    def square_root(self):
        try:
            value = eval(self.operator)
            result = math.sqrt(value)
            self.operator = str(result)
            with self.output:
                print(result)
        except Exception as e:
            with self.output:
                print(f"Error: {str(e)}")

    def power(self):
        self.operator = self.operator + "**"
        with self.output:
            print(self.operator)

    def euler_number(self):
        self.operator = str(math.e)
        with self.output:
            print(self.operator)

    def swap_registers(self):
        # Implement swap functionality
        pass

    def calculate_days_between(self):
        # Implement days between functionality
        pass

    def create_gui(self):
        button_layout = widgets.Layout(width='50px', height='50px')
        scientific_button_layout = widgets.Layout(width='70px', height='50px')

        buttons = [
            widgets.Button(description='7', layout=button_layout),
            widgets.Button(description='8', layout=button_layout),
            widgets.Button(description='9', layout=button_layout),
            widgets.Button(description='/', layout=button_layout),
            widgets.Button(description='4', layout=button_layout),
            widgets.Button(description='5', layout=button_layout),
            widgets.Button(description='6', layout=button_layout),
            widgets.Button(description='*', layout=button_layout),
            widgets.Button(description='1', layout=button_layout),
            widgets.Button(description='2', layout=button_layout),
            widgets.Button(description='3', layout=button_layout),
            widgets.Button(description='-', layout=button_layout),
            widgets.Button(description='0', layout=button_layout),
            widgets.Button(description='.', layout=button_layout),
            widgets.Button(description='=', layout=button_layout),
            widgets.Button(description='+', layout=button_layout),
            widgets.Button(description='C', layout=button_layout),
        ]

        scientific_buttons = [
            widgets.Button(description='1/x', layout=scientific_button_layout),
            widgets.Button(description='√', layout=scientific_button_layout),
            widgets.Button(description='π', layout=scientific_button_layout),
            widgets.Button(description='yx', layout=scientific_button_layout),
            widgets.Button(description='sin', layout=scientific_button_layout),
            widgets.Button(description='cos', layout=scientific_button_layout),
            widgets.Button(description='tan', layout=scientific_button_layout),
            widgets.Button(description='asin', layout=scientific_button_layout),
            widgets.Button(description='acos', layout=scientific_button_layout),
            widgets.Button(description='atan', layout=scientific_button_layout),
            widgets.Button(description='log', layout=scientific_button_layout),
            widgets.Button(description='ln', layout=scientific_button_layout),
            widgets.Button(description='e', layout=scientific_button_layout),
            widgets.Button(description='ex', layout=scientific_button_layout),
            widgets.Button(description='±', layout=scientific_button_layout),
            widgets.Button(description='%', layout=scientific_button_layout),
            widgets.Button(description='M+', layout=scientific_button_layout),
            widgets.Button(description='M-', layout=scientific_button_layout),
            widgets.Button(description='MS', layout=scientific_button_layout),
            widgets.Button(description='MR', layout=scientific_button_layout),
            widgets.Button(description='MC', layout=scientific_button_layout),
            widgets.Button(description='Enter', layout=scientific_button_layout),
            widgets.Button(description='=', layout=scientific_button_layout),
            # Additional scientific buttons can be added here
        ]

        for button in buttons:
            if button.description == '=':
                button.on_click(lambda x: self.evaluate())
            elif button.description == 'C':
                button.on_click(lambda x: self.clear())
            else:
                button.on_click(lambda x: self.click_button(x.description))

        scientific_buttons[0].on_click(lambda x: self.reciprocal())
        scientific_buttons[1].on_click(lambda x: self.square_root())
        scientific_buttons[2].on_click(lambda x: self.operator + str(math.pi))
        scientific_buttons[3].on_click(lambda x: self.power())
        scientific_buttons[4].on_click(lambda x: self.sin_function())
        # Add more scientific button callbacks as needed

        grid = widgets.GridBox(buttons, layout=widgets.Layout(grid_template_columns="repeat(4, 50px)"))
        scientific_grid = widgets.GridBox(scientific_buttons, layout=widgets.Layout(grid_template_columns="auto"))

        display(grid)
        display(scientific_grid)
        display(self.output)

# Create an instance of the Calculator class
calculator = Calculator()
