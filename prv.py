import io
import pycurl
from kivy.app import App
from kivy.uix.button import Button
import stem.process
from stem.util import term

SOCKS_PORT = 7000

tor_country = '{ru}'

class gui(App):
    def build(self):
        return Button(text='Secure Connection')

gui().run()

#tor API section
"""
def query(url):
  
  output = io.BytesIO()

def print_bootstrap_lines(line):
  if "Bootstrapped " in line:
    print(term.format(line, term.Color.BLUE))


print(term.format("Starting Tor:\n", term.Attr.BOLD))

tor_process = stem.process.launch_tor_with_config(
  config = {
    'SocksPort': str(SOCKS_PORT),
    'ExitNodes': tor_country,
  },
  init_msg_handler = print_bootstrap_lines,
)

#tor_process.kill()  # stops tor
"""

