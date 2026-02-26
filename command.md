
#
dir *.py

python -c "import sys; print(sys.path)"

pip uninstall -y numpy
pip install numpy==1.26.4 --force-reinstall --no-cache-dir

python -c "import numpy; print(numpy.__version__)"
pip show scipy





# issue

2026-02-25 22:57:54.993259: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2026-02-25 22:57:56.542747: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.

#
set TF_CPP_MIN_LOG_LEVEL=2 && python .\train_pretrain.py

$env:TF_CPP_MIN_LOG_LEVEL = "2"

(base) PS C:\Users\hongf\miniconda3\envs\minimind-master> conda activate my_project_env
(my_project_env) PS C:\Users\hongf\miniconda3\envs\minimind-master> $env:TF_CPP_MIN_LOG_LEVEL = "2"


$env:TF_CPP_MIN_LOG_LEVEL = "3";
日志级别说明 ：

- 0: 显示所有日志（默认）
- 1: 只显示信息性日志和更严重的日志
- 2: 只显示警告和错误
- 3: 只显示错误
#



#
nvidia-smi
conda activate my_project_env


#
等效批大小 = batch_size × accumulation_steps × num_gpus