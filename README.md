# AI_Project
**#Genetic Algorithm**

**Genetic Algorithm for Feature Selection**
This program implements a genetic algorithm for feature selection using cosine similarity as the fitness function. The algorithm evolves a population of binary feature vectors over multiple generations to maximize classification accuracy on a validation dataset.

**How to Run the Program**

**Data Preparation:**
Prepare your training and validation datasets in CSV format.
Ensure that the training and validation labels are provided in separate files.
In this project Datasets are: 

 **Training DataSets:**
  File train.csv 
  File label_train.csv 
  
  **Validation DataSets:**
  File validate.csv 
  File Label_validate.csv
  
**Program Execution:**
Place the program file (genetic_algorithm.py) in the same directory as your datasets.
Open the terminal or command prompt.
Navigate to the directory containing the program and datasets.
![image](https://github.com/SreeSus-1/AI_Project/assets/164704978/aa0137fd-67f4-46d1-8f29-635bfd3b200c)

**Run the program using the command:**
      python genetic_algorithm.py train.csv label_train.csv validate.csv Label_validate.csv


Replace train.csv, label_train.csv, validate.csv, and Label_validate.csv with the filenames of your training data, training labels, validation data, and validation labels respectively.
Adjust Parameters (Optional):
You can adjust the following parameters in the program according to your requirements:
num_features: Number of features in the dataset.
population_size: Size of the population for each generation.
max_generations: Maximum number of generations for the genetic algorithm.
mutation_rate: Probability of mutation during reproduction.


**Program Output**:
After running the program, it will display the following information:

        Number of classes in training and validation labels.
        Final optimized feature vector accuracy on the validation dataset.
        Number of qualified feature vectors and their indices.
        A line graph showing the fitness score over generations.

Number of classes in training labels: 7
Number of classes in validation labels: 7

Final optimized feature vector accuracy: 2.78%
Number of qualified feature vectors: 693
Qualified feature vectors: [   3    6    9   11   12   13   14   15   17   19   21   22   23   27
   28   30   32   33   34   36   38   39   41   44   46   49   50   54
   56   60   62   63   66   68   71   72   73   75   77   85   86   88
   89   90   91   92   93   96   98   99  106  113  118  120  122  123
  124  128  129  131  133  136  141  142  143  145  146  147  148  149
  154  155  159  161  162  163  165  167  168  169  171  173  174  177
  178  180  182  183  186  189  192  193  195  197  198  201  205  206
  212  218  219  220  224  227  231  232  233  236  237  238  241  244
  247  248  250  253  258  260  261  262  269  277  278  280  282  284
  286  287  288  289  290  291  293  294  295  296  297  299  300  301
  303  306  309  311  313  314  315  318  320  322  323  324  325  327
  328  334  336  338  342  345  349  352  353  355  358  360  362  364
  365  367  370  376  378  379  380  382  383  384  389  390  391  394
  397  398  401  402  404  407  409  410  412  414  416  417  420  421
  422  424  427  428  431  434  435  436  437  439  440  442  443  444
  445  446  447  451  453  454  456  457  458  463  465  469  470  471
  476  477  478  480  481  483  485  487  488  492  496  497  498  499
  500  502  503  505  506  510  511  513  516  518  521  529  532  533
  534  535  536  538  541  543  545  553  554  556  559  561  565  567
  569  570  571  573  578  579  582  585  586  588  589  592  594  595
  600  601  604  605  607  610  611  612  615  616  619  620  627  629
  630  634  637  640  644  646  647  648  654  656  659  661  662  663
  664  667  678  679  680  682  683  685  686  690  691  692  693  695
  696  706  707  709  710  711  719  721  726  727  728  730  734  736
  738  739  742  744  745  746  748  755  763  765  766  767  768  769
  771  773  774  775  776  779  780  782  783  785  789  793  795  796
  797  799  800  801  804  807  808  809  814  815  821  823  824  825
  827  829  830  831  832  833  834  836  837  841  844  845  846  847
  848  849  850  852  853  854  855  857  861  863  865  866  868  869
  871  872  874  877  880  881  882  885  887  888  891  892  896  897
  899  900  901  902  903  904  905  906  910  911  912  914  915  916
  917  920  922  923  924  925  931  934  936  939  940  941  944  945
  947  949  951  953  954  955  956  958  959  962  963  964  965  967
  968  970  974  975  976  977  984  986  991  993  994  998 1000 1002
 1003 1006 1008 1011 1013 1014 1015 1018 1019 1020 1022 1023 1026 1027
 1030 1034 1036 1037 1039 1043 1045 1047 1056 1058 1063 1065 1066 1067
 1069 1074 1075 1080 1081 1083 1086 1087 1090 1092 1098 1099 1100 1102
 1103 1105 1107 1108 1109 1112 1115 1119 1120 1121 1126 1127 1129 1130
 1131 1132 1133 1135 1137 1139 1140 1144 1145 1147 1150 1151 1153 1154
 1155 1156 1157 1158 1159 1160 1162 1166 1167 1168 1169 1170 1172 1175
 1176 1177 1186 1191 1193 1195 1199 1201 1207 1212 1213 1215 1217 1218
 1221 1223 1224 1226 1227 1229 1230 1231 1234 1237 1238 1242 1245 1247
 1248 1249 1250 1251 1252 1253 1255 1256 1258 1259 1260 1262 1266 1267
 1268 1270 1273 1280 1285 1286 1289 1290 1293 1294 1297 1298 1299 1300
 1303 1304 1308 1310 1314 1316 1317 1321 1322 1323 1325 1326 1329 1333
 1337 1338 1339 1340 1342 1343 1344 1345 1346 1348 1350 1351 1352 1353
 1354 1357 1359 1360 1361 1363 1364 1365 1367 1371 1373 1376 1377 1378
 1379 1381 1383 1384 1385 1386 1387 1390 1391 1394 1395 1396 1397 1398
 1400 1401 1402 1404 1405 1406 1407 1410 1411 1412 1413 1417 1419 1422
 1423 1425 1427 1428 1430 1431 1432]

**Graph:******

![image](https://github.com/SreeSus-1/AI_Project/assets/164704978/8fbb0c05-df53-4d4c-be6f-acad39d83658)


**Requirements**:
  Python 3.x
  NumPy
  pandas
  Matplotlib
  scikit-learn
Ensure that you have the required Python packages installed before running the program.
