import io
import pycurl
import pygame #this is for UI later on down the line
import stem.process
from stem.util import term

SOCKS_PORT = 7000

tor_country = '{ru}'

def main():
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    logo = pygame.image.load("logo01.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("PrivacyTool")
    sebutton = pygame.image.load("secconnect.png")
    screen.blit(sebutton, (240,340))
    sebutton.set_colorkey((255,255,255))
    running = True
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

if __name__=="__main__":
    main()
    
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

