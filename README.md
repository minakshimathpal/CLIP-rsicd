# CLIP-rsicd


## Evaluation Results

A subset of the image test set had file names that indicated that the image belonged to one of 30 image categories in the RSICD dataset. Evaluation was done by comparing the CLIP encoding of each image with CLIP encodings of each of 30 synthetic caption sentences of the form `"An aerial photograph of {category}"`, and the checking to see that the correct category was found within the first k ranked predictions, for k=1, 3, 5, and 10.

| Model-name                               | k=1   | k=3   | k=5   | k=10  |
| ---------------------------------------- | ----- | ----- | ----- | ----- |
| baseline                                 | 0.572 | 0.745 | 0.837 | 0.939 |
| bs128x8-lr1e-4-augs-ckpt-2               | 0.819 | 0.950 | 0.974 | 0.994 |
| bs128x8-lr1e-4-imgaugs-ckpt-9            | 0.811 | 0.943 | 0.964 | 0.990 |
| bs128x8-lr1e-4-imgaugs-ckpt-2            | 0.812 | 0.942 | 0.970 | 0.991 |
| bs128x8-lr1e-4-imgaugs-textaugs-ckpt-4   | *0.843* | 0.958 | *0.977* | 0.993 |
| bs128x8-lr5e-5-imgaugs-textaugs-ckpt-8   | 0.831 | *0.959* | *0.977* | *0.994* |
| bs128x8-lr5e-5-imgaugs-ckpt-4            | 0.746 | 0.906 | 0.956 | 0.989 |
| bs128x8-lr5e-5-imgaugs-textaugs-2-ckpt-4 | 0.811 | 0.945 | 0.972 | 0.993 |
| bs128x8-lr5e-5-imgaugs-textaugs-3-ckpt-5 | 0.823 | 0.946 | 0.971 | 0.992 |
| bs128x8-lr5e-5-wd02-ckpt-4               | 0.820 | 0.946 | 0.965 | 0.990 |

