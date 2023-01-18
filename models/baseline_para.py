import attr 

@attr.s
class BaselinePara:
    # normally need for all models
    backbone:str='resnet50'
    pre_trained:bool=True 
    backbone_dim:int=1024
    output_size:int=1

    # only for baseline with csv meta
    no_columns:int=None
    column_out_dim:int=500
    
    ckpt_path:str=None