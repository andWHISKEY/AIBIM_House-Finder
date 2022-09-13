# AIBIM_House-Finder

---

## AIBIM-House Finder

- Code and instructions for our paper: SCIE Journal Under Review (2022-April)

## Introduction

![introduction.png](HouseF!inder%201d293f7c69984622922542941cdd32ac/introduction.png)

House finder's database is 10,000 image-based house floor plans. We collected image data through crawling of published data on real estate websites. We developed an Annotaion Tool (AIBIM-Detector) and produced training data to dection the space. We have developed AIBIM-Bubble Maker that automatically extracts spatial relationship graphs. Through this, the spatial relation database was extracted with Excel. The database can be used for spatial generation and spatial recommendations.

### AIBIM-Detector

[[https://dadl.knu.ac.kr/forum/view/699814](https://dadl.knu.ac.kr/forum/view/699814)](HouseF!inder%201d293f7c69984622922542941cdd32ac/Archi-Detector(English).mp4)

[https://dadl.knu.ac.kr/forum/view/699814](https://dadl.knu.ac.kr/forum/view/699814)

### AIBIM-Bubble Maker

[[https://dadl.knu.ac.kr/forum/view/699809](https://dadl.knu.ac.kr/forum/view/699809)](HouseF!inder%201d293f7c69984622922542941cdd32ac/Archi-Bubble_Maker(English).mp4)

[https://dadl.knu.ac.kr/forum/view/699809](https://dadl.knu.ac.kr/forum/view/699809)

## ****Citation****

```jsx
@onproceeding{
	author={Park, H. J. and Suh, H. G. and Kim, J. and Choo, S. Y.},
	doi={},
	journal={},
	year={2022},
}
```

## Contact

If you have any question, feel free to contact me at gpwls3143@gmail.com

School of Architecture, Kyungpook National University, Daegu 41566, Republic of Korea

## ****Acknowledgement****

This work is supported by the Korea Agency for Infrastructure Technology Advancement(KAIA) grant funded by the Ministry of Land, Infrastructure and Transport

## ****Prerequisites****

- python==3.8
- pytorch (본인 CUDA version에 맞게)
    
    [PyTorch](https://pytorch.org/get-started/locally/)
    
- pytorch geometric( 본인 pytorch version과 CUDA version에 맞게)
    
    [Installation - pytorch_geometric documentation](https://pytorch-geometric.readthedocs.io/en/latest/notes/installation.html)
    
- numpy
- pandas
- networkx
- argparse
- sklearn

## Execution

```python
main.bat
```
