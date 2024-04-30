from .base_settings import *
import os

# import base_settings
# base_settings.
if os.environ["mod"] == "production":
    from .prod_settings import *

else:
    from .local_settings import *
