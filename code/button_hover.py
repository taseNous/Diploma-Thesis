# Function to change button color on hover
def on_enter(event):
    event.widget['background'] = 'lightblue'  # Change background color
    event.widget['foreground'] = 'black'  # Change text color

# Function to reset button color when hover ends
def on_leave(event):
    event.widget['background'] = '#61afef'  # Reset to default
    event.widget['foreground'] = 'black'

def on_enter_exit(event):
    event.widget['background'] = '#ff4d4d'  # More vibrant red
    event.widget['foreground'] = 'black'

def on_leave_exit(event):
    event.widget['background'] = '#ff6666'  # Original background color
    event.widget['foreground'] = 'black'

def on_enter_delete(event):
    event.widget['background'] = '#ff9999'  # More vibrant red
    event.widget['foreground'] = 'white'

def on_leave_delete(event):
    event.widget['background'] = 'red'  # Original background color
    event.widget['foreground'] = 'white'

def on_enter_instr(event):
    event.widget['background'] = '#b0b0b0'  # More vibrant red
    event.widget['foreground'] = 'black'

def on_leave_instr(event):
    event.widget['background'] = 'white'  # Original background color
    event.widget['foreground'] = 'black'

def on_enter_pipeline(event):
    event.widget['background'] = '#7B68EE'  # More vibrant red
    event.widget['foreground'] = 'black'

def on_leave_pipeline(event):
    event.widget['background'] = '#9370DB'  # Original background color
    event.widget['foreground'] = 'black'

def on_enter_execute(event):
    event.widget['background'] = '#4CAF50'  # More vibrant red
    event.widget['foreground'] = 'black'

def on_leave_execute(event):
    event.widget['background'] = '#66FF66'  # Original background color
    event.widget['foreground'] = 'black'