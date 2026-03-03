
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


#
python eval_llm.py --weight pretrain
python eval_llm.py --weight full_sft # 或 pretrain/dpo/ppo/grpo...

python ./train_pretrain.py --use_wandb    ##
python ./train_full_sft.py --use_wandb

#SFT
python trainer/train_full_sft.py --data_path ../dataset/your_custom_data.jsonl --batch_size 16 --learning_rate 1e-5 --epochs 5






#config 1:

parameter = 50.480M
dim=512
num_hidden_layers: int = 16,
num_attention_heads: int = 16,  
num_key_value_heads: int = 8,    
vocab_size: int = 6400,

work=2
batch_size", type=int, default=32
max_seq_len', default=51


Epoch:[1/3](100/44160), loss: 6.6085, logits_loss: 6.6085, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 1106.000min
Epoch:[1/3](200/44160), loss: 5.8245, logits_loss: 5.8245, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 1060.000min


#config 2:

parameter = 50.480M
dim=512
num_hidden_layers: int = 16,
num_attention_heads: int = 16,  
num_key_value_heads: int = 8,    
vocab_size: int = 6400,

work=1   # change from 2 to 1
batch_size", type=int, default=32
max_seq_len', default=51

Epoch:[1/3](20/44160), loss: 7.2791, logits_loss: 7.2791, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 1141.000min
Epoch:[1/3](40/44160), loss: 6.9888, logits_loss: 6.9888, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 1052.000min



#config 3:

parameter = 50.480M => 26.88M 
#  5533MiB /   8188MiB
dim=512
num_hidden_layers: int = 8,    # change to 8
num_attention_heads: int = 16,  
num_key_value_heads: int = 8,    
vocab_size: int = 6400,

work=1   # change from 2 to 1
batch_size", type=int, default=32
max_seq_len', default=51

Epoch:[1/3](20/44160), loss: 7.2546, logits_loss: 7.2546, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 418.000min
Epoch:[1/3](40/44160), loss: 6.9594, logits_loss: 6.9594, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 318.000min
Epoch:[1/3](60/44160), loss: 6.8529, logits_loss: 6.8529, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 284.000min
Epoch:[1/3](80/44160), loss: 6.7437, logits_loss: 6.7437, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 267.000min
Epoch:[1/3](100/44160), loss: 6.5440, logits_loss: 6.5440, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 257.000min
Epoch:[1/3](120/44160), loss: 6.2923, logits_loss: 6.2923, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 250.000min
Epoch:[1/3](140/44160), loss: 5.9950, logits_loss: 5.9950, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 245.000min



#config 4:

parameter =26.88M  =>38.68M
#  7333MiB /   8188MiB
dim=512
num_hidden_layers: int = 12,    # 8 change to 12
num_attention_heads: int = 16,  
num_key_value_heads: int = 8,    
vocab_size: int = 6400,

work=1  
batch_size", type=int, default=32
max_seq_len', default=51

, epoch_time: 498.000min
Epoch:[1/3](40/44160), loss: 7.0272, logits_loss: 7.0272, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 407.000min
Epoch:[1/3](60/44160), loss: 6.8696, logits_loss: 6.8696, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 376.000min
Epoch:[1/3](80/44160), loss: 6.7924, logits_loss: 6.7924, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 360.000min
Epoch:[1/3](100/44160), loss: 6.6271, logits_loss: 6.6271, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 351.000min
Epoch:[1/3](120/44160), loss: 6.4100, logits_loss: 6.4100, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 344.000min
Epoch:[1/3](140/44160), loss: 6.2476, logits_loss: 6.2476, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 339.000min
Epoch:[1/3](160/44160), loss: 5.9299, logits_loss: 5.9299, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 335.000min
Epoch:[1/3](180/44160), loss: 5.7301, logits_loss: 5.7301, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 332.000min
Epoch:[1/3](200/44160), loss: 5.7127, logits_loss: 5.7127, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 330.000min



#config 5:

parameter 38.68M ->3.182M
Trainable Params: 3.182M
3171MiB /   8188MiB
dim=512 ->128     # change to 128
num_hidden_layers: int = 12,   
num_attention_heads: int = 16,  
num_key_value_heads: int = 8,    
vocab_size: int = 6400,

work=1  
batch_size", type=int, default=32
max_seq_len', default=512

Epoch:[1/3](20/44160), loss: 8.2200, logits_loss: 8.2200, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 288.000min
Epoch:[1/3](40/44160), loss: 7.7669, logits_loss: 7.7669, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 182.000min
Epoch:[1/3](60/44160), loss: 7.4776, logits_loss: 7.4776, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 146.000min
Epoch:[1/3](80/44160), loss: 7.1893, logits_loss: 7.1893, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 127.000min
Epoch:[1/3](100/44160), loss: 7.1044, logits_loss: 7.1044, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 116.000min
Epoch:[1/3](120/44160), loss: 7.0003, logits_loss: 7.0003, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 109.000min
Epoch:[1/3](140/44160), loss: 6.9544, logits_loss: 6.9544, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 103.000min
Epoch:[1/3](160/44160), loss: 6.9601, logits_loss: 6.9601, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 99.000min
Epoch:[1/3](180/44160), loss: 6.9328, logits_loss: 6.9328, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 96.000min
Epoch:[1/3](200/44160), loss: 6.7884, logits_loss: 6.7884, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 94.000min
Epoch:[1/3](220/44160), loss: 6.7182, logits_loss: 6.7182, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 92.000min
Epoch:[1/3](240/44160), loss: 6.7010, logits_loss: 6.7010, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 90.000min
Epoch:[1/3](260/44160), loss: 6.6726, logits_loss: 6.6726, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 88.000min
Epoch:[1/3](280/44160), loss: 6.6385, logits_loss: 6.6385, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 87.000min
Epoch:[1/3](300/44160), loss: 6.4727, logits_loss: 6.4727, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 86.000min
Epoch:[1/3](320/44160), loss: 6.4671, logits_loss: 6.4671, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 85.000min
Epoch:[1/3](340/44160), loss: 6.3226, logits_loss: 6.3226, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 84.000min
Epoch:[1/3](360/44160), loss: 6.2852, logits_loss: 6.2852, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 83.000min
Epoch:[1/3](380/44160), loss: 6.2733, logits_loss: 6.2733, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 83.000min
Epoch:[1/3](400/44160), loss: 6.1699, logits_loss: 6.1699, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 82.000min
Epoch:[1/3](420/44160), loss: 6.1915, logits_loss: 6.1915, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 82.000min
Epoch:[1/3](440/44160), loss: 6.0733, logits_loss: 6.0733, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 81.000min
Epoch:[1/3](460/44160), loss: 6.0535, logits_loss: 6.0535, aux_loss: 0.0000, learning_rate: 0.00019999, epoch_time: 81.000min
Epoch:[1/3](480/44160), loss: 5.9596, logits_loss: 5.9596, aux_loss: 0.0000, learning_rate: 0.00019999, epoch_time: 80.000min
Epoch:[1/3](500/44160), loss: 5.8709, logits_loss: 5.8709, aux_loss: 0.0000, learning_rate: 0.00019999, epoch_time: 80.000min
Epoch:[1/3](520/44160), loss: 5.8539, logits_loss: 5.8539, aux_loss: 0.0000, learning_rate: 0.00019999, epoch_time: 80.000min
Epoch:[1/3](540/44160), loss: 5.7029, logits_loss: 5.7029, aux_loss: 0.0000, learning_rate: 0.00019999, epoch_time: 79.000min
Epoch:[1/3](560/44160), loss: 5.8692, logits_loss: 5.8692, aux_loss: 0.0000, learning_rate: 0.00019999, epoch_time: 78.000min


#
#config 6:

parameter 
Trainable Params: 10.492M
4727MiB /   8188MiB
dim=256                        # change to 256
num_hidden_layers: int = 12,   
num_attention_heads: int = 16,  
num_key_value_heads: int = 8,    
vocab_size: int = 6400,

work=1  
batch_size", type=int, default=32
max_seq_len', default=512


Epoch:[1/3](20/44160), loss: 7.6995, logits_loss: 7.6995, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 330.000min
Epoch:[1/3](40/44160), loss: 7.1775, logits_loss: 7.1775, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 232.000min
Epoch:[1/3](60/44160), loss: 7.0518, logits_loss: 7.0518, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 198.000min
Epoch:[1/3](80/44160), loss: 6.9415, logits_loss: 6.9415, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 181.000min
Epoch:[1/3](100/44160), loss: 6.8250, logits_loss: 6.8250, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 171.000min
Epoch:[1/3](120/44160), loss: 6.7786, logits_loss: 6.7786, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 164.000min
Epoch:[1/3](140/44160), loss: 6.7306, logits_loss: 6.7306, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 159.000min
Epoch:[1/3](160/44160), loss: 6.6151, logits_loss: 6.6151, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 155.000min



#
#config 7:
parameter 
Trainable Params: 16.394M
6623MiB /   8188MiB

dim=256                         
num_hidden_layers: int = 20,     # change from 12 to 20
num_attention_heads: int = 16,  
num_key_value_heads: int = 8,    
vocab_size: int = 6400,

work=1  
batch_size", type=int, default=32
max_seq_len', default=512

Epoch:[1/3](20/44160), loss: 7.6592, logits_loss: 7.6592, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 407.000min
Epoch:[1/3](40/44160), loss: 7.1939, logits_loss: 7.1939, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 308.000min
Epoch:[1/3](60/44160), loss: 7.0736, logits_loss: 7.0736, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 275.000min
Epoch:[1/3](80/44160), loss: 6.9790, logits_loss: 6.9790, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 258.000min
Epoch:[1/3](100/44160), loss: 6.8234, logits_loss: 6.8234, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 247.000min
Epoch:[1/3](120/44160), loss: 6.8337, logits_loss: 6.8337, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 240.000min
Epoch:[1/3](140/44160), loss: 6.7659, logits_loss: 6.7659, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 236.000min
Epoch:[1/3](160/44160), loss: 6.6862, logits_loss: 6.6862, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 232.000min
Epoch:[1/3](180/44160), loss: 6.5465, logits_loss: 6.5465, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 229.000min
Epoch:[1/3](200/44160), loss: 6.4517, logits_loss: 6.4517, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 226.000min
Epoch:[1/3](220/44160), loss: 6.2557, logits_loss: 6.2557, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 224.000min
Epoch:[1/3](240/44160), loss: 6.0709, logits_loss: 6.0709, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 222.000min



#
#config 8:
parameter 
Trainable Params: 19.346M
7571MiB /   8188MiB

dim=256                         
num_hidden_layers: int = 24,     # change from 20 to 24
num_attention_heads: int = 16,  
num_key_value_heads: int = 8,    
vocab_size: int = 6400,

work=1  
batch_size", type=int, default=32
max_seq_len', default=512

Epoch:[1/3](100/44160), loss: 6.8739, logits_loss: 6.8739, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 288.000min
Epoch:[1/3](200/44160), loss: 6.3618, logits_loss: 6.3618, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 265.000min


#config -8
python ./train_pretrain.py --use_wandb    #  --use_wandb

#config 8:
parameter 
Trainable Params: 19.346M
7571MiB /   8188MiB |

dim=256                         
num_hidden_layers: int = 24,     # 
num_attention_heads: int = 16,  
num_key_value_heads: int = 8,    
vocab_size: int = 6400,

work=1  
batch_size", type=int, default=32
max_seq_len', default=512


或批处理文件.
swanlab: Tracking run with swanlab version 0.7.6
swanlab: Run data will be saved locally in
C:\Users\hongf\miniconda3\envs\minimind-master\trainer\swanlog\run-20260302_090601-chhz6rc8xsqaydwc8x9zt      
swanlab: 👋 Hi LTE_SAE,welcome to swanlab!
swanlab: Syncing run MiniMind-Pretrain-Epoch-3-BatchSize-32-LearningRate-0.0002 to the cloud
swanlab: 🏠 View project at https://swanlab.cn/@LTE_SAE/MiniMind-Pretrain
swanlab: 🚀 View run at https://swanlab.cn/@LTE_SAE/MiniMind-Pretrain/runs/chhz6rc8xsqaydwc8x9zt
Model Params: 19.35M
Trainable Params: 19.346M
2026-03-02 09:06:07.945738: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2026-03-02 09:06:09.052275: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
Epoch:[1/3](100/44160), loss: 6.8739, logits_loss: 6.8739, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 288.000min
Epoch:[1/3](200/44160), loss: 6.3616, logits_loss: 6.3616, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 265.000min
Epoch:[1/3](300/44160), loss: 5.8719, logits_loss: 5.8719, aux_loss: 0.0000, learning_rate: 0.00020000, epoch_time: 258.000min



#



￼
￼
￼
大模型训练后得到的参数，包括哪些部分

大模型训练后得到的参数主要包括以下部分：
1. 词嵌入层参数
embed_tokens.weight：词嵌入矩阵，大小为 [vocab_size, hidden_size]
vocab_size：词汇表大小（默认6400）
hidden_size：隐藏层维度（默认256）
注意：此权重与输出层共享
2. 模型层参数
每个 MiniMindBlock 包含以下参数：
输入层归一化：input_layernorm.weight
注意力机制：
q_proj.weight：查询投影权重
k_proj.weight：键投影权重
v_proj.weight：值投影权重
o_proj.weight：输出投影权重
注意力后归一化：post_attention_layernorm.weight
前馈网络（FeedForward）：
gate_proj.weight：门控投影权重
up_proj.weight：上投影权重
down_proj.weight：下投影权重
MoE 相关参数（如果使用）：
多个专家网络的参数
门控网络权重：gate.weight
3. 输出层参数
lm_head.weight：语言模型头权重，与词嵌入层共享
4. 归一化层参数
norm.weight：最终输出归一化权重
5. 其他参数
位置编码：虽然位置编码是预计算的（freqs_cos 和 freqs_sin），但它们不是可训练参数
参数规模
以默认配置为例：
隐藏层维度：256
隐藏层数量：24
注意力头数：16
词汇表大小：6400
总参数量约为 74.08M，其中大部分是词嵌入层、注意力机制和前馈网络的参数。
这些参数共同构成了模型的知识表示，通过预训练和微调不断优化，使模型能够理解和生成自然语言.