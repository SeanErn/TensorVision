import os
import pathlib
import importlib.util
import subprocess
from colorama import Fore

if not pathlib.Path('./libcudnn7_7.4.1.5-1+cuda10.0_amd64.deb').exists():
    print(Fore.CYAN+'[INSTALL] Installing nvidia-cudnn...')
    os.system('wget https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v7.4.1.5/prod/10.0_20181108/Ubuntu18_04-x64/libcudnn7_7.4.1.5-1%2Bcuda10.0_amd64.deb')
    os.system('sudo dpkg -i libcudnn7_7.4.1.5-1+cuda10.0_amd64.deb')

if not pathlib.Path('./ssd_mobilenet_v2_quantized/model.ckpt.index').exists():
    print(Fore.CYAN+'[INSTALL] Installing pretrained checkpoint...')
    os.system('wget http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_quantized_300x300_coco_2019_01_03.tar.gz')
    os.system('tar -xvf ssd_mobilenet_v2_quantized_300x300_coco_2019_01_03.tar.gz')
    os.system('rm ssd_mobilenet_v2_quantized_300x300_coco_2019_01_03.tar.gz')
    os.system('rm ssd_mobilenet_v2_quantized_300x300_coco_2019_01_03/pipeline.config')
    os.system('mv ssd_mobilenet_v2_quantized_300x300_coco_2019_01_03/* models/ssd_mobilenet_v2_quantized')
    os.system('rm -r ssd_mobilenet_v2_quantized_300x300_coco_2019_01_03')


# If paths are not exported, export them
if not pathlib.Path(str(os.path.expanduser('~'))+'/.bashrc').read_text().find('export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib') != -1:
    current_dir = os.getcwd()
    os.chdir('..')
    os.system('pip install tensorflow_gpu==1.14')
    os.chdir(current_dir)
    print(Fore.CYAN+'[INSTALL] Exporting CUDA paths...')
    os.system('CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))')
    os.system('export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib')
    os.system('mkdir -p $CONDA_PREFIX/etc/conda/activate.d')
    os.system('''echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh''')
    os.system('''echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh''')
else:
    print(Fore.YELLOW+'[INFO] CUDA paths already exported, skipping...')

# If the directory modelsLib allready exists, delete it
if pathlib.Path('modelsLib').exists():
    print(Fore.CYAN+'[INSTALL] Deleting old modelsLib directory...')
    os.system('rm -r modelsLib')
else:
    print(Fore.YELLOW+'[INFO] modelsLib directory already deleted, skipping...')

# Clone the tensorflow models repository if it doesn't already exist
if "modelsLib" in pathlib.Path.cwd().parts:
    while "modelsLib" in pathlib.Path.cwd().parts:
        os.chdir('..')
elif not pathlib.Path('modelsLib').exists():
    os.system('git clone --depth 1 https://github.com/tensorflow/models modelsLib')
else:
    print(Fore.YELLOW+'[INFO] Tensorflow models already exists, skipping...')

# Install the object detection API
os.chdir('modelsLib/research')
os.system('protoc object_detection/protos/*.proto --python_out=.')

# If setup.py is not present, copy it from the tensorflow object detection API
if not pathlib.Path('setup.py').exists():
    os.system('cp object_detection/packages/tf1/setup.py .')
else:
    print(Fore.YELLOW+'[INFO] Setup.py already exists, skipping...')

# directory slim/deployment is missing in models/research, run the build install script
print(Fore.YELLOW+'[INFO] Installing object detection API...')
print(Fore.WHITE+'[INFO] This may take a while...')
os.system('python -m pip install .')
print(Fore.GREEN+'[SUCCESS] Object detection API installed successfully!')

# Run the build test script
# print(Fore.LIGHTBLUE_EX+'[TEST] Running build test script...')
# os.system('python object_detection/builders/model_builder_tf2_test.py')

print(Fore.GREEN+'[SUCCESS] Installed Correctly!'+Fore.WHITE)

