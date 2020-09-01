import os
from . import app

if __name__ == '__main__':
    app.run(port=int(os.environ['PORT']))
