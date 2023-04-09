python demo.py --config-file ../configs/ade20k/semantic-segmentation/semask_swin/msfapn_maskformer2_semask_swin_large_IN21k_384_bs16_160k_res640.yaml \
  --input ./top_potsdam_7_13_143.jpg \
  --output ./results \
  --opts MODEL.WEIGHTS ../checkpoint/semask_large_mask2former_msfapn_ade20k.pth
  