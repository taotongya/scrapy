import os

mulv = os.path.join(os.path.dirname(__file__),'images')
if not os.path.exists(mulv):
    print('创建成功')
else:

    print('文件已存在')