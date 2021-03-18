# ALWA
Implementation of'ALWA'

# Usage
a. Following [mmdetection](https://github.com/open-mmlab/mmdetection) for installing mmdetection

b. delete folders: mmdet and configs in mmdetection

c.copy the folders:mmdet and  configs in this repo to mmdetection

d.Prepare COCO or VOC dataset


# Training

CUDA_VISIBLE_DEVICES=0,1,2,3 PORT=29501 ./tools/dist_train.sh ./configs/alwa/voc/faster_rcnn_r50_fpn_1x_voc.py 4 --work-dir ' ./work_dirs/alwa/voc/rpn/1/' 

          //all config files for Faster R-CNN,Mask R-CNN,RetinaNet in ./configs/alwa

# Changing setting
If you want change the update iterations count C and choose ALWA_1 or ALWA_2 in ./mmdet/models/dense_heads/anchor_head.py

a. default  setting
    update iterations count C = 100; ALWA = ALWA_2
    
b. changing update iterations count C 
    Line 512 in ./mmdet/models/dense_heads/anchor_head.py
    
c. choose ALWA 
    Line 523 and Line 524 represents ALWA_1
    Line 527 and Line 528 represents ALWA_2
    
    For example, if you want choose ALWA_1, you should comment Line 527 and Line 528, and uncomment Line 523 and Line 524.
