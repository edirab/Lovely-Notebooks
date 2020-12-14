## Ограничение потребления памяти

### Для v2:


```python
import tensorflow as tf

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
    except RuntimeError as e:
        print(e)
```


### Для v1:

```python
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.2)
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))
```


### Ещё какой-то вариант

```python
tf.config.gpu.set_per_process_memory_fraction(0.75)
tf.config.gpu.set_per_process_memory_growth(True)
```


## Запуск Tensorboard и Jupyter Notebook

    %load_ext tensorboard
    %tensorboard --logdir logs