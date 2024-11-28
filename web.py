from pywebio.input import input as pw_input
from pywebio.output import put_text


import money
import phrarases
import consatns

put_text(phrarases.MSG_WELCOME.format(rest=consatns.restaurant_name))