#Check if a local directory with the name 'thumbnails' exists else create one
import os
if not os.path.exists('./thumbnails'):
    os.makedirs('./thumbnails')
