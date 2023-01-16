import os
import shutil

# place all your input images in ./my_images
src_dir = "./my_images"

if os.path.exists("./video"):
    shutil.rmtree("./video")
os.mkdir("./video")

if os.path.exists("./depth"):
    shutil.rmtree("./depth")
os.mkdir("./depth")

for image in os.listdir(src_dir):
  if os.path.exists("./image"):
    shutil.rmtree("./image")
  os.mkdir("./image")

  print("Starting image ", image)
  command1 = "cp " + src_dir+"/" + image + " ./image"
  os.system(command1)

  os.system("python main.py --config argument.yml")