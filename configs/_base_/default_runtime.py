checkpoint_config = dict(interval=12)
# yapf:disable
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ])
# yapf:enable
dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
#load_from = '/ghome/yuwx/mmdetection/pretrain/cascasde_rcnn/rpn_r50_fpn_2x_20181010-88a4a471.pth'
resume_from = None
workflow = [('train', 1)]
