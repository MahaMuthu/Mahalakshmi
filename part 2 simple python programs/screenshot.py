# Program to take screenshot

import pyscreenshot
from pyscreenshot.childproc import childprocess_backend_version
from pyscreenshot.imcodec import codec
from PIL import Image

# To capture the screen
image = pyscreenshot.grab()

# To display the captured screenshot
image.show()

# To save the screenshot
image.save("screen.png")
