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
