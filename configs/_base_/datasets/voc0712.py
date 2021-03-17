# dataset settings
dataset_type = 'VOCDataset'
data_root = '/gdata/yuwx/Xray/VOCdevkit/'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)

albu_train_transforms = [
    # dict(
    #     type='HorizontalFlip',
    #     p=0.5),
    # dict(
    #     type='VerticalFlip',
    #     p=0.5),
    dict(type='RandomRotate90', always_apply=False, p=0.5)
    #dict(
    #    type='ShiftScaleRotate',
    #    shift_limit=0.0625,
    #    scale_limit=0.0,
    #    rotate_limit=180,
    #    interpolation=1,
    #    p=0.5),
    # dict(
    #     type='RandomBrightnessContrast',
    #     brightness_limit=[0.1, 0.3],
    #     contrast_limit=[0.1, 0.3],
    #     p=0.2),
    # dict(
    #     type='OneOf',
    #     transforms=[
    #         dict(
    #             type='RGBShift',
    #             r_shift_limit=10,
    #             g_shift_limit=10,
    #             b_shift_limit=10,
    #             p=1.0),
    #         dict(
    #             type='HueSaturationValue',
    #             hue_shift_limit=20,
    #             sat_shift_limit=30,
    #             val_shift_limit=20,
    #             p=1.0)
    #     ],
    #     p=0.1),
    # # dict(type='JpegCompression', quality_lower=85, quality_upper=95, p=0.2),
    #
    # dict(type='ChannelShuffle', p=0.1),
    # dict(
    #     type='OneOf',
    #     transforms=[
    #         dict(type='Blur', blur_limit=3, p=1.0),
    #         dict(type='MedianBlur', blur_limit=3, p=1.0)
    #     ],
    #     p=0.1),
]



train_pipeline = [
    dict(type='LoadImageFromFile',to_float32=True),
    dict(type='LoadAnnotations', with_bbox=True),
    #dict(type='MixUp',p=0.5, lambd=0.5),
    #dict(type='Resize', img_scale=(1333, 800), keep_ratio=True),
    dict(type='Resize', img_scale=[(1333, 800),(1000,600)], keep_ratio=True),
    #dict(type='Resize', img_scale=[(4096,600),(4096,1000)], keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    #dict(type='RandomVFlip', flip_ratio=0.5),
    
    #dict(type='PhotoMetricDistortion'),    ##mmdetection data Augment
    #dict(type='Corrupt',corruption='gaussian_noise'),
    #dict(type='RandomCrop',crop_size=[1100,700]),

    #dict(                                 ##ablument data Augment
    #    type='Albu',
    #    transforms=albu_train_transforms,
    #    bbox_params=dict(
    #        type='BboxParams',
    #        format='pascal_voc',
    #        label_fields=['gt_labels'],
    #        min_visibility=0.0,
    #        filter_lost_elements=True),
    #    keymap={
    #        'img': 'image',
    #        'gt_bboxes': 'bboxes'
    #    },
    #    update_pad_shape=False,
    #    skip_img_without_anno=True),

    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(1333, 800),
        #img_scale=[(4096, 800),(4096,600),(4096,1000)],
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            #dict(type='RandomVFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=4,
    workers_per_gpu=2,
    train=dict(
        type='RepeatDataset',
        times=3,
        dataset=dict(
            type=dataset_type,
            #ann_file=[
            #    data_root + 'VOC2007/ImageSets/Main/trainval.txt',
            #    data_root + 'VOC2012/ImageSets/Main/trainval.txt'
            #],
            #img_prefix=[data_root + 'VOC2007/', data_root + 'VOC2012/'],
            ann_file = [data_root + 'VOC2007/ImageSets/Main/train.txt'],
            img_prefix=[data_root + 'VOC2007/'],
            pipeline=train_pipeline)),
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'VOC2007/ImageSets/Main/val.txt',
        img_prefix=data_root + 'VOC2007/',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        ann_file=data_root + 'VOC2007/ImageSets/Main/test.txt',
        img_prefix=data_root + 'VOC2007/',
        pipeline=test_pipeline))
evaluation = dict(interval=24, metric='mAP')
