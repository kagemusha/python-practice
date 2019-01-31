import os
from os import path
import glob
from shutil import copyfile

base_dir = "vw_simulator_model_files"
model_dir = path.join(base_dir, "models")
predictions_dir = path.join(base_dir, "predictions")
new_predictions_dir = path.join(base_dir, "new_predictions")

for dir in [model_dir, predictions_dir, new_predictions_dir]:
  if not path.isdir(dir):
    os.makedirs(dir)
print("isdir", base_dir, os.path.isdir(base_dir))
print("cwd", os.getcwd())

# prediction_files = glob.glob(base_dir+'/vw_simulator.model.csv.*')
# print("pfile count", len(prediction_files))
# for file_name in prediction_files:
#   parts = file_name.split('.')
#   new_file_name = f"original-preds-{parts[3]}.csv"
#   dst = path.join(predictions_dir, new_file_name)
#   copyfile(file_name, dst)

# model_files = glob.glob(base_dir+'/vw_simulator.model.*')
# print("pfile count", len(model_files))
# for file_name in model_files:
#   parts = file_name.split('.')
#   new_file_name = f"sim-{parts[3]}.vw"
#   dst = path.join(model_dir, new_file_name)
#   copyfile(file_name, dst)

# files = []
# for file in files:
  # rename