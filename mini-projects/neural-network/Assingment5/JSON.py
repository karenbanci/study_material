import json
import collections
import numpy as np
from CompleteNeuralNetworkFinal import NNData, FFBPNetwork


class MultiTypeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, collections.deque):
            return {"__deque__": list(o)}

        if isinstance(o, np.ndarray):
            return {"__ndarray__": o.tolist()}

        if isinstance(o, set):
            return {"__set__": list(o)}

        if isinstance(o, NNData):
            # Python knows how to encode a dictionary
            return {"__NNData__": o.__dict__}

        super().default(o)


def multiple_type_decoder(o):
    if "__deque__" in o:
        return collections.deque(o["__deque__"])

    if "__ndarray__" in o:
        return np.array(o["__ndarray__"])

    if "__NDarray__" in o:
        return np.array(o["__NDarray__"])

    if "__set__" in o:
        return set(o["__set__"])

    if "__NNData__" in o:
        item = o["__NNData__"]
        ret_obj = NNData()
        ret_obj._features = item["_features"]
        ret_obj._labels = item["_labels"]
        ret_obj._train_indices = item["_train_indices"]
        ret_obj._test_indices = item["_test_indices"]
        ret_obj._train_pool = item["_train_pool"]
        ret_obj._test_pool = item["_test_pool"]
        ret_obj._train_factor = item["_train_factor"]
        return ret_obj
    return o


""" XOR DATA """
print("------ XOR DATA")
xor_data = NNData(features=[
        [0, 0], [1, 0], [0, 1], [1, 1],
        [0, 0], [1, 0], [0, 1], [1, 1],
        [0, 0], [1, 0], [0, 1], [1, 1],
        [0, 0], [1, 0], [0, 1], [1, 1],
        [0, 0], [1, 0], [0, 1], [1, 1]],
           labels=[
               [0], [1], [1], [0],
               [0], [1], [1], [0],
               [0], [1], [1], [0],
               [0], [1], [1], [0],
               [0], [1], [1], [0]],
           train_factor=.8)

xor_data_encoded = json.dumps(xor_data, cls=MultiTypeEncoder)
xor_data_decoded = json.loads(xor_data_encoded,
                              object_hook=multiple_type_decoder)
print("xor_data_encoded", xor_data_encoded)
print("\nxor_data_decoded", xor_data_decoded, "\n")

xor_network = FFBPNetwork(2, 1)
xor_network.add_hidden_layer(5)
xor_network.train(xor_data_decoded, 10001, order=NNData.Order.RANDOM)
xor_network.test(xor_data_decoded)

""" SIN DATA """
print("\n------ SIN DATA")
with open("sin_data.json", "r") as f:
    sin_decoded = json.load(f, object_hook=multiple_type_decoder)

print("\nsin_decoded", sin_decoded, "\n")

sin_network = FFBPNetwork(1, 1)
sin_network.add_hidden_layer(3)
sin_network.train(sin_decoded, 10001, order=NNData.Order.RANDOM)
sin_network.test(sin_decoded)

"""
/Users/karenbanci/opt/anaconda3/bin/python /Users/karenbanci/code/Foothill/
Project CS_3B_Winter_2023/CS_3B_Winter_2023/Assingment5/JSON.py 

------ XOR DATA
xor_data_encoded {"__NNData__": {"_features": {"__ndarray__": [[0.0, 0.0], 
[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.0, 0.0], [1.0, 0.0], [0.0, 1.0], 
[1.0, 1.0], [0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.0, 0.0], 
[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.0, 0.0], [1.0, 0.0], [0.0, 1.0], 
[1.0, 1.0]]}, "_labels": {"__ndarray__": [[0.0], [1.0], [1.0], [0.0], [0.0], 
[1.0], [1.0], [0.0], [0.0], [1.0], [1.0], [0.0], [0.0], [1.0], [1.0], [0.0],
 [0.0], [1.0], [1.0], [0.0]]}, "_train_factor": 0.8, "_train_indices": 
 [10, 17, 18, 9, 15, 2, 11, 19, 8, 7, 12, 6, 0, 4, 5, 1], 
 "_test_indices": [14, 3, 16, 13], "_train_pool": 
 {"__deque__": [10, 17, 18, 9, 15, 2, 11, 19, 8, 7, 12, 6, 0, 4, 5, 1]}, 
 "_test_pool": {"__deque__": [14, 3, 16, 13]}}}

xor_data_decoded <CompleteNeuralNetworkFinal.NNData object at 0x7f90c811fd30> 

Feature: [1. 0.], Label: [1.]
Output:  0.7682139073138488
Feature: [0. 0.], Label: [0.]
Output:  0.6937821034368076
Feature: [0. 1.], Label: [1.]
Output:  0.7565072601056317
Feature: [1. 1.], Label: [0.]
Output:  0.8172559889066148
Feature: [0. 0.], Label: [0.]
Output:  0.6902525468330808
Feature: [1. 1.], Label: [0.]
Output:  0.8128820619051157
Feature: [1. 0.], Label: [1.]
Output:  0.76083572942746
Feature: [0. 0.], Label: [0.]
Output:  0.6866224474745406
Feature: [1. 0.], Label: [1.]
Output:  0.7595499515503406
Feature: [0. 1.], Label: [1.]
Output:  0.7494330065375209
Feature: [1. 1.], Label: [0.]
Output:  0.8106868452123528
Feature: [0. 1.], Label: [1.]
Output:  0.7476725595461906
Feature: [0. 1.], Label: [1.]
Output:  0.7485631971955711
Feature: [0. 0.], Label: [0.]
Output:  0.6853431800609779
Feature: [1. 0.], Label: [1.]
Output:  0.7582100534385843
Feature: [1. 1.], Label: [0.]
Output:  0.8085632158504646
Epoch: 0 RMSE = 0.49727517028530055
Epoch: 100 RMSE = 0.50157807073587
Epoch: 200 RMSE = 0.5014906109168084
Epoch: 300 RMSE = 0.5013205502457629
Epoch: 400 RMSE = 0.5011289454345136
Epoch: 500 RMSE = 0.5010011831016882
Epoch: 600 RMSE = 0.5007366405806354
Epoch: 700 RMSE = 0.5005953990232099
Epoch: 800 RMSE = 0.5000748575161031
Epoch: 900 RMSE = 0.49926605530919055
Feature: [0. 0.], Label: [0.]
Output:  0.4499324723453632
Feature: [1. 1.], Label: [0.]
Output:  0.5464869458742692
Feature: [1. 0.], Label: [1.]
Output:  0.518726764384905
Feature: [0. 1.], Label: [1.]
Output:  0.4845036075585157
Feature: [0. 0.], Label: [0.]
Output:  0.44998889084506855
Feature: [0. 1.], Label: [1.]
Output:  0.48562818064567925
Feature: [0. 1.], Label: [1.]
Output:  0.4889439040287003
Feature: [1. 1.], Label: [0.]
Output:  0.5538872712999756
Feature: [0. 1.], Label: [1.]
Output:  0.4883065835337672
Feature: [1. 1.], Label: [0.]
Output:  0.553116499322439
Feature: [0. 0.], Label: [0.]
Output:  0.4497966905645596
Feature: [1. 0.], Label: [1.]
Output:  0.5221179016876738
Feature: [1. 0.], Label: [1.]
Output:  0.5248904771405549
Feature: [1. 1.], Label: [0.]
Output:  0.5526944747274393
Feature: [0. 0.], Label: [0.]
Output:  0.4494839498060491
Feature: [1. 0.], Label: [1.]
Output:  0.5218552127494113
Epoch: 1000 RMSE = 0.4981509101909973
Epoch: 1100 RMSE = 0.49587611753156313
Epoch: 1200 RMSE = 0.4920056550628436
Epoch: 1300 RMSE = 0.486383811909551
Epoch: 1400 RMSE = 0.47803002980234843
Epoch: 1500 RMSE = 0.4667185543270771
Epoch: 1600 RMSE = 0.453228566335649
Epoch: 1700 RMSE = 0.43857495807399005
Epoch: 1800 RMSE = 0.42347770790209893
Epoch: 1900 RMSE = 0.40728196186086485
Feature: [1. 0.], Label: [1.]
Output:  0.6279492800285912
Feature: [1. 1.], Label: [0.]
Output:  0.4905842712827592
Feature: [0. 0.], Label: [0.]
Output:  0.2950140633689476
Feature: [1. 0.], Label: [1.]
Output:  0.6251517271870397
Feature: [0. 1.], Label: [1.]
Output:  0.5982153575940111
Feature: [1. 0.], Label: [1.]
Output:  0.6311630097432909
Feature: [0. 1.], Label: [1.]
Output:  0.6042805514101958
Feature: [1. 1.], Label: [0.]
Output:  0.49790473323219697
Feature: [0. 0.], Label: [0.]
Output:  0.2982598728278061
Feature: [1. 1.], Label: [0.]
Output:  0.4902808704556957
Feature: [0. 0.], Label: [0.]
Output:  0.2948494319015632
Feature: [1. 0.], Label: [1.]
Output:  0.6250648079280955
Feature: [0. 0.], Label: [0.]
Output:  0.295668261934178
Feature: [1. 1.], Label: [0.]
Output:  0.48480106517938887
Feature: [0. 1.], Label: [1.]
Output:  0.592131479499034
Feature: [0. 1.], Label: [1.]
Output:  0.595718212279845
Epoch: 2000 RMSE = 0.390480509032027
Epoch: 2100 RMSE = 0.37244753486862664
Epoch: 2200 RMSE = 0.3520511847739106
Epoch: 2300 RMSE = 0.32903293948141554
Epoch: 2400 RMSE = 0.3048018067177331
Epoch: 2500 RMSE = 0.27956415016374575
Epoch: 2600 RMSE = 0.2553446258268686
Epoch: 2700 RMSE = 0.2335055943497469
Epoch: 2800 RMSE = 0.21420704962372336
Epoch: 2900 RMSE = 0.19755199472387147
Feature: [0. 0.], Label: [0.]
Output:  0.16498012203039955
Feature: [1. 0.], Label: [1.]
Output:  0.8117355032988436
Feature: [0. 1.], Label: [1.]
Output:  0.8188937084868129
Feature: [0. 1.], Label: [1.]
Output:  0.8195216036002234
Feature: [0. 0.], Label: [0.]
Output:  0.16572329663785154
Feature: [0. 1.], Label: [1.]
Output:  0.8198841735151519
Feature: [1. 1.], Label: [0.]
Output:  0.20003290842301127
Feature: [0. 1.], Label: [1.]
Output:  0.8197261724653574
Feature: [1. 0.], Label: [1.]
Output:  0.813001666017855
Feature: [1. 0.], Label: [1.]
Output:  0.8138028856685497
Feature: [1. 1.], Label: [0.]
Output:  0.20117854789820788
Feature: [1. 1.], Label: [0.]
Output:  0.19996281582300532
Feature: [1. 1.], Label: [0.]
Output:  0.19876521015611878
Feature: [0. 0.], Label: [0.]
Output:  0.16488323879716332
Feature: [0. 0.], Label: [0.]
Output:  0.16468794097340417
Feature: [1. 0.], Label: [1.]
Output:  0.8113035014756041
Epoch: 3000 RMSE = 0.18327155413817275
Epoch: 3100 RMSE = 0.17107535972781515
Epoch: 3200 RMSE = 0.16056396125935643
Epoch: 3300 RMSE = 0.15144842251597498
Epoch: 3400 RMSE = 0.14350814083831537
Epoch: 3500 RMSE = 0.13653242668256735
Epoch: 3600 RMSE = 0.13036374649911284
Epoch: 3700 RMSE = 0.12486721687569444
Epoch: 3800 RMSE = 0.11993771084227121
Epoch: 3900 RMSE = 0.11550117375222041
Feature: [0. 0.], Label: [0.]
Output:  0.11865356828664911
Feature: [0. 0.], Label: [0.]
Output:  0.11857249322490862
Feature: [1. 0.], Label: [1.]
Output:  0.8855270453135302
Feature: [1. 1.], Label: [0.]
Output:  0.10569125614388561
Feature: [0. 1.], Label: [1.]
Output:  0.8927770932995727
Feature: [0. 1.], Label: [1.]
Output:  0.892919794575511
Feature: [1. 0.], Label: [1.]
Output:  0.8857502026033041
Feature: [1. 0.], Label: [1.]
Output:  0.8859674319618727
Feature: [1. 1.], Label: [0.]
Output:  0.10615596227100912
Feature: [1. 0.], Label: [1.]
Output:  0.8860010247810876
Feature: [1. 1.], Label: [0.]
Output:  0.10612302332167388
Feature: [0. 1.], Label: [1.]
Output:  0.893062318366713
Feature: [0. 0.], Label: [0.]
Output:  0.11882651456166643
Feature: [1. 1.], Label: [0.]
Output:  0.10591309079091393
Feature: [0. 0.], Label: [0.]
Output:  0.11862916274886848
Feature: [0. 1.], Label: [1.]
Output:  0.8928882928261668
Epoch: 4000 RMSE = 0.11147949172636358
Epoch: 4100 RMSE = 0.10780697489756928
Epoch: 4200 RMSE = 0.10445614453670939
Epoch: 4300 RMSE = 0.10137147726454573
Epoch: 4400 RMSE = 0.09852197158972988
Epoch: 4500 RMSE = 0.09589313111628922
Epoch: 4600 RMSE = 0.09344177023173325
Epoch: 4700 RMSE = 0.09115915012395664
Epoch: 4800 RMSE = 0.0890298481528227
Epoch: 4900 RMSE = 0.08703232857113406
Feature: [0. 0.], Label: [0.]
Output:  0.0975379877816043
Feature: [0. 1.], Label: [1.]
Output:  0.9191737942216858
Feature: [0. 1.], Label: [1.]
Output:  0.9192357752747469
Feature: [0. 0.], Label: [0.]
Output:  0.09756284815750797
Feature: [1. 1.], Label: [0.]
Output:  0.07493935746353492
Feature: [0. 0.], Label: [0.]
Output:  0.09746517558333574
Feature: [1. 0.], Label: [1.]
Output:  0.9125734136382827
Feature: [0. 0.], Label: [0.]
Output:  0.09747592348009791
Feature: [1. 1.], Label: [0.]
Output:  0.07480730214999085
Feature: [1. 0.], Label: [1.]
Output:  0.9125384290880494
Feature: [1. 1.], Label: [0.]
Output:  0.0748066224770907
Feature: [1. 0.], Label: [1.]
Output:  0.9125680804016468
Feature: [0. 1.], Label: [1.]
Output:  0.919126328696311
Feature: [1. 1.], Label: [0.]
Output:  0.07486786132704151
Feature: [0. 1.], Label: [1.]
Output:  0.9191310468520738
Feature: [1. 0.], Label: [1.]
Output:  0.9126783752185605
Epoch: 5000 RMSE = 0.08515236468930294
Epoch: 5100 RMSE = 0.08338916924864176
Epoch: 5200 RMSE = 0.08172021186883419
Epoch: 5300 RMSE = 0.08014717390540682
Epoch: 5400 RMSE = 0.0786550543183464
Epoch: 5500 RMSE = 0.07723649309687922
Epoch: 5600 RMSE = 0.07588963231798232
Epoch: 5700 RMSE = 0.07460815075235908
Epoch: 5800 RMSE = 0.07338909069648718
Epoch: 5900 RMSE = 0.0722221350577694
Feature: [0. 0.], Label: [0.]
Output:  0.08479565728368957
Feature: [1. 1.], Label: [0.]
Output:  0.0595349861137029
Feature: [1. 1.], Label: [0.]
Output:  0.05948951682320646
Feature: [1. 0.], Label: [1.]
Output:  0.9269722534282951
Feature: [1. 1.], Label: [0.]
Output:  0.05949309913904024
Feature: [1. 0.], Label: [1.]
Output:  0.9269942309469668
Feature: [0. 0.], Label: [0.]
Output:  0.08475082560154988
Feature: [0. 1.], Label: [1.]
Output:  0.9328123047024602
Feature: [0. 1.], Label: [1.]
Output:  0.9328479823026088
Feature: [1. 0.], Label: [1.]
Output:  0.9270602937102586
Feature: [0. 0.], Label: [0.]
Output:  0.0847985748181519
Feature: [1. 1.], Label: [0.]
Output:  0.05953328691672841
Feature: [0. 1.], Label: [1.]
Output:  0.9328507263598103
Feature: [1. 0.], Label: [1.]
Output:  0.9270631822505866
Feature: [0. 0.], Label: [0.]
Output:  0.08479606768174228
Feature: [0. 1.], Label: [1.]
Output:  0.9328838985577184
Epoch: 6000 RMSE = 0.07110669638244418
Epoch: 6100 RMSE = 0.07004236986983649
Epoch: 6200 RMSE = 0.0690200460652539
Epoch: 6300 RMSE = 0.06804047819998008
Epoch: 6400 RMSE = 0.0670970366150736
Epoch: 6500 RMSE = 0.06619448893943383
Epoch: 6600 RMSE = 0.06532114531586905
Epoch: 6700 RMSE = 0.06448137717854478
Epoch: 6800 RMSE = 0.06367421092293066
Epoch: 6900 RMSE = 0.06289354103768646
Feature: [1. 1.], Label: [0.]
Output:  0.050269368770929
Feature: [0. 1.], Label: [1.]
Output:  0.9415084787333072
Feature: [1. 1.], Label: [0.]
Output:  0.05026338756890305
Feature: [0. 1.], Label: [1.]
Output:  0.9415130319716415
Feature: [0. 1.], Label: [1.]
Output:  0.9415365577387571
Feature: [0. 0.], Label: [0.]
Output:  0.07600342882920462
Feature: [1. 1.], Label: [0.]
Output:  0.050251585544287845
Feature: [0. 1.], Label: [1.]
Output:  0.9415218058502418
Feature: [0. 0.], Label: [0.]
Output:  0.07597641089430647
Feature: [1. 0.], Label: [1.]
Output:  0.9361422384275652
Feature: [0. 0.], Label: [0.]
Output:  0.07597822344606427
Feature: [1. 0.], Label: [1.]
Output:  0.9361543361294966
Feature: [1. 0.], Label: [1.]
Output:  0.9361964017010901
Feature: [0. 0.], Label: [0.]
Output:  0.07600520523130128
Feature: [1. 0.], Label: [1.]
Output:  0.9362084000502285
Feature: [1. 1.], Label: [0.]
Output:  0.050290230373762984
Epoch: 7000 RMSE = 0.06214103687852697
Epoch: 7100 RMSE = 0.06141329555189415
Epoch: 7200 RMSE = 0.060710079070625325
Epoch: 7300 RMSE = 0.06002754928816669
Epoch: 7400 RMSE = 0.05936889009393915
Epoch: 7500 RMSE = 0.05872829267641827
Epoch: 7600 RMSE = 0.058109852492823896
Epoch: 7700 RMSE = 0.057509119792691216
Epoch: 7800 RMSE = 0.05692645970558109
Epoch: 7900 RMSE = 0.05635752954220125
Feature: [0. 0.], Label: [0.]
Output:  0.069442377907795
Feature: [1. 0.], Label: [1.]
Output:  0.9426517054502648
Feature: [1. 0.], Label: [1.]
Output:  0.9426825573379105
Feature: [0. 0.], Label: [0.]
Output:  0.06946187060334211
Feature: [1. 1.], Label: [0.]
Output:  0.04400570083438148
Feature: [1. 1.], Label: [0.]
Output:  0.04398653972172524
Feature: [1. 1.], Label: [0.]
Output:  0.04396740283052191
Feature: [0. 0.], Label: [0.]
Output:  0.06940463738501777
Feature: [0. 0.], Label: [0.]
Output:  0.06938654420678142
Feature: [0. 1.], Label: [1.]
Output:  0.9474969553491084
Feature: [1. 0.], Label: [1.]
Output:  0.9426033543202978
Feature: [0. 1.], Label: [1.]
Output:  0.9475258683661756
Feature: [0. 1.], Label: [1.]
Output:  0.9475428389350731
Feature: [1. 1.], Label: [0.]
Output:  0.04397683729209607
Feature: [0. 1.], Label: [1.]
Output:  0.9475467396813694
Feature: [1. 0.], Label: [1.]
Output:  0.9426493898615714
Epoch: 8000 RMSE = 0.05580828134249313
Epoch: 8100 RMSE = 0.055272782458717175
Epoch: 8200 RMSE = 0.05475021336298982
Epoch: 8300 RMSE = 0.05424400184762077
Epoch: 8400 RMSE = 0.053749227515416026
Epoch: 8500 RMSE = 0.05326848379108396
Epoch: 8600 RMSE = 0.05279985595881435
Epoch: 8700 RMSE = 0.052342540345250765
Epoch: 8800 RMSE = 0.05189699483468806
Epoch: 8900 RMSE = 0.05146143879631585
Feature: [0. 0.], Label: [0.]
Output:  0.06428968116378507
Feature: [0. 0.], Label: [0.]
Output:  0.06427514194967598
Feature: [1. 1.], Label: [0.]
Output:  0.03941614198217479
Feature: [1. 0.], Label: [1.]
Output:  0.947479912336167
Feature: [0. 1.], Label: [1.]
Output:  0.9520618116349809
Feature: [0. 0.], Label: [0.]
Output:  0.06427404825180487
Feature: [1. 1.], Label: [0.]
Output:  0.03941523637989199
Feature: [0. 0.], Label: [0.]
Output:  0.06424976977989004
Feature: [0. 1.], Label: [1.]
Output:  0.9520424811239645
Feature: [0. 1.], Label: [1.]
Output:  0.9520554203321057
Feature: [1. 1.], Label: [0.]
Output:  0.03940873489350411
Feature: [0. 1.], Label: [1.]
Output:  0.9520587611980603
Feature: [1. 0.], Label: [1.]
Output:  0.9474748514753548
Feature: [1. 0.], Label: [1.]
Output:  0.9474987586278005
Feature: [1. 0.], Label: [1.]
Output:  0.9475226341902717
Feature: [1. 1.], Label: [0.]
Output:  0.03945829672689071
Epoch: 9000 RMSE = 0.05103702626305701
Epoch: 9100 RMSE = 0.05062267133104803
Epoch: 9200 RMSE = 0.05021639063541119
Epoch: 9300 RMSE = 0.049819939184000184
Epoch: 9400 RMSE = 0.04943416590911856
Epoch: 9500 RMSE = 0.049055425327582204
Epoch: 9600 RMSE = 0.048684963055792486
Epoch: 9700 RMSE = 0.0483221545708343
Epoch: 9800 RMSE = 0.04796749293899805
Epoch: 9900 RMSE = 0.04761893119414877
Feature: [0. 1.], Label: [1.]
Output:  0.9556289226750028
Feature: [1. 0.], Label: [1.]
Output:  0.9513724358119005
Feature: [0. 0.], Label: [0.]
Output:  0.06012293467331141
Feature: [1. 1.], Label: [0.]
Output:  0.03600065493354662
Feature: [1. 1.], Label: [0.]
Output:  0.0359899167448543
Feature: [0. 0.], Label: [0.]
Output:  0.060095658359145966
Feature: [1. 0.], Label: [1.]
Output:  0.9513420052217773
Feature: [0. 0.], Label: [0.]
Output:  0.06009557994727735
Feature: [0. 1.], Label: [1.]
Output:  0.9556110823844144
Feature: [1. 1.], Label: [0.]
Output:  0.03597642562505828
Feature: [0. 1.], Label: [1.]
Output:  0.9556139331688105
Feature: [1. 0.], Label: [1.]
Output:  0.9513494064538949
Feature: [0. 0.], Label: [0.]
Output:  0.060101425412583766
Feature: [1. 0.], Label: [1.]
Output:  0.9513538294700183
Feature: [0. 1.], Label: [1.]
Output:  0.9556292721970426
Feature: [1. 1.], Label: [0.]
Output:  0.03599840585226165
Epoch: 10000 RMSE = 0.04728000713532363
Training finished.
 Final Training RMSE = 0.04728000713532363 

----- starting test
input_value: 0.0
input_value: 1.0
output_value: 0.9556321046774798
expected_value: 1.0
input_value: 1.0
input_value: 1.0
output_value: 0.03598766960447576
expected_value: 0.0
input_value: 0.0
input_value: 0.0
output_value: 0.06010047319219599
expected_value: 0.0
input_value: 1.0
input_value: 0.0
output_value: 0.9513693898817472
expected_value: 1.0
Final Testing RMSE = 0.04727166205936117

------ SIN DATA

sin_decoded <CompleteNeuralNetworkFinal.NNData object at 0x7f90a8327940> 

Feature: [0.08], Label: [0.07991469]
Output:  0.6560799557350748
Feature: [0.54], Label: [0.51413599]
Output:  0.7137400565735786
Feature: [1.1], Label: [0.89120736]
Output:  0.7760354380779749
Feature: [0.53], Label: [0.50553334]
Output:  0.7123499139397372
Feature: [1.45], Label: [0.99271299]
Output:  0.8096445813454202
Feature: [0.15], Label: [0.14943813]
Output:  0.6639951990586678
Feature: [1.46], Label: [0.99386836]
Output:  0.8099522382586195
Feature: [0.87], Label: [0.76432894]
Output:  0.7510204802306703
Feature: [0.47], Label: [0.45288629]
Output:  0.7042552381838435
Feature: [1.48], Label: [0.99588084]
Output:  0.8116301490029427
Feature: [0.69], Label: [0.63653718]
Output:  0.7304579233629376
Feature: [0.97], Label: [0.82488571]
Output:  0.7615787634146809
Feature: [0.34], Label: [0.33348709]
Output:  0.6877326541196225
Feature: [1.2], Label: [0.93203909]
Output:  0.7847715502509491
Feature: [0.39], Label: [0.38018842]
Output:  0.6936197832185171
Feature: [0.21], Label: [0.2084599]
Output:  0.6699027594338846
Feature: [0.61], Label: [0.57286746]
Output:  0.7190141799824524
Feature: [0.01], Label: [0.00999983]
Output:  0.6420393672492304
Feature: [0.8], Label: [0.71735609]
Output:  0.7395607583828117
Feature: [0.66], Label: [0.61311685]
Output:  0.7233579682525669
Feature: [0.56], Label: [0.5311862]
Output:  0.711216278902505
Feature: [0.82], Label: [0.73114583]
Output:  0.7412022842042393
Feature: [1.36], Label: [0.9778646]
Output:  0.7971155381724236
Feature: [0.17], Label: [0.16918235]
Output:  0.6618577930396666
Feature: [0.48], Label: [0.46177918]
Output:  0.7004159004581374
Feature: [0.49], Label: [0.47062589]
Output:  0.7011637479920723
Feature: [0.44], Label: [0.42593947]
Output:  0.6945121347073996
Feature: [0.9], Label: [0.78332691]
Output:  0.7479944289952262
Feature: [0.24], Label: [0.23770263]
Output:  0.668595265149288
Feature: [0.41], Label: [0.39860933]
Output:  0.6894122902387017
Feature: [0.83], Label: [0.73793137]
Output:  0.7388322327863197
Epoch: 0 RMSE = 0.23005360720420162
Epoch: 100 RMSE = 0.19818049444841918
Epoch: 200 RMSE = 0.19452838672287953
Epoch: 300 RMSE = 0.18417571074788072
Epoch: 400 RMSE = 0.1602183195378059
Epoch: 500 RMSE = 0.13206279215658343
Epoch: 600 RMSE = 0.10899482635804388
Epoch: 700 RMSE = 0.0909409472530219
Epoch: 800 RMSE = 0.07695146593021267
Epoch: 900 RMSE = 0.06559512417036634
Feature: [0.08], Label: [0.07991469]
Output:  0.191438389133158
Feature: [1.48], Label: [0.99588084]
Output:  0.873504124638317
Feature: [0.15], Label: [0.14943813]
Output:  0.2347420999449839
Feature: [0.21], Label: [0.2084599]
Output:  0.27609478935876214
Feature: [1.1], Label: [0.89120736]
Output:  0.8025881026216741
Feature: [0.17], Label: [0.16918235]
Output:  0.24805541819147583
Feature: [0.53], Label: [0.50553334]
Output:  0.5241615117167373
Feature: [0.56], Label: [0.5311862]
Output:  0.5459873899811021
Feature: [1.2], Label: [0.93203909]
Output:  0.8266191931202211
Feature: [0.9], Label: [0.78332691]
Output:  0.7366307888038259
Feature: [0.01], Label: [0.00999983]
Output:  0.15405631115413662
Feature: [0.83], Label: [0.73793137]
Output:  0.7062630405768728
Feature: [0.61], Label: [0.57286746]
Output:  0.5810375543004098
Feature: [0.69], Label: [0.63653718]
Output:  0.6320146166334373
Feature: [0.41], Label: [0.39860933]
Output:  0.43140596839762957
Feature: [0.48], Label: [0.46177918]
Output:  0.4863380638486097
Feature: [1.45], Label: [0.99271299]
Output:  0.8695603129567627
Feature: [0.66], Label: [0.61311685]
Output:  0.6136304931833039
Feature: [0.97], Label: [0.82488571]
Output:  0.7629898908836873
Feature: [0.87], Label: [0.76432894]
Output:  0.7243304478851718
Feature: [0.54], Label: [0.51413599]
Output:  0.5319168147311523
Feature: [1.36], Label: [0.9778646]
Output:  0.8566214191069702
Feature: [0.39], Label: [0.38018842]
Output:  0.41580074980707715
Feature: [0.34], Label: [0.33348709]
Output:  0.3757682250487181
Feature: [1.46], Label: [0.99386836]
Output:  0.8710867659205954
Feature: [0.24], Label: [0.23770263]
Output:  0.29826557444521223
Feature: [0.49], Label: [0.47062589]
Output:  0.49433156909452236
Feature: [0.82], Label: [0.73114583]
Output:  0.7018022863101174
Feature: [0.44], Label: [0.42593947]
Output:  0.45539951500902637
Feature: [0.47], Label: [0.45288629]
Output:  0.47881379835089327
Feature: [0.8], Label: [0.71735609]
Output:  0.692071565344306
Epoch: 1000 RMSE = 0.056296578545792106
Epoch: 1100 RMSE = 0.04882651710176568
Epoch: 1200 RMSE = 0.04272460189756932
Epoch: 1300 RMSE = 0.037591499571943514
Epoch: 1400 RMSE = 0.03335529705201501
Epoch: 1500 RMSE = 0.029827715659198503
Epoch: 1600 RMSE = 0.02716409687527384
Epoch: 1700 RMSE = 0.025354480709023425
Epoch: 1800 RMSE = 0.024103747172194993
Epoch: 1900 RMSE = 0.023455618931076463
Feature: [0.66], Label: [0.61311685]
Output:  0.632423755638864
Feature: [0.41], Label: [0.39860933]
Output:  0.39331583330273856
Feature: [1.1], Label: [0.89120736]
Output:  0.8546085952037468
Feature: [0.08], Label: [0.07991469]
Output:  0.12130310136442261
Feature: [1.46], Label: [0.99386836]
Output:  0.9179776954759648
Feature: [0.56], Label: [0.5311862]
Output:  0.5441714703050405
Feature: [0.61], Label: [0.57286746]
Output:  0.5900136265051253
Feature: [0.44], Label: [0.42593947]
Output:  0.4241640401667669
Feature: [0.17], Label: [0.16918235]
Output:  0.17672297589386302
Feature: [0.97], Label: [0.82488571]
Output:  0.812700882075233
Feature: [1.45], Label: [0.99271299]
Output:  0.9168629212535828
Feature: [0.24], Label: [0.23770263]
Output:  0.23096504315530642
Feature: [1.48], Label: [0.99588084]
Output:  0.9201690568174578
Feature: [0.01], Label: [0.00999983]
Output:  0.0888424174682379
Feature: [0.82], Label: [0.73114583]
Output:  0.7424202394308848
Feature: [0.8], Label: [0.71735609]
Output:  0.7307800070462752
Feature: [0.53], Label: [0.50553334]
Output:  0.5151777824220624
Feature: [0.87], Label: [0.76432894]
Output:  0.7689311226003457
Feature: [0.49], Label: [0.47062589]
Output:  0.47526408344356424
Feature: [0.9], Label: [0.78332691]
Output:  0.7832915876986094
Feature: [0.48], Label: [0.46177918]
Output:  0.46511046968396774
Feature: [0.54], Label: [0.51413599]
Output:  0.5248586389724446
Feature: [1.2], Label: [0.93203909]
Output:  0.8782750922542542
Feature: [1.36], Label: [0.9778646]
Output:  0.9055833985438934
Feature: [0.39], Label: [0.38018842]
Output:  0.37294780323326143
Feature: [0.15], Label: [0.14943813]
Output:  0.16304211325963963
Feature: [0.21], Label: [0.2084599]
Output:  0.20658063136113458
Feature: [0.47], Label: [0.45288629]
Output:  0.45503755361169734
Feature: [0.34], Label: [0.33348709]
Output:  0.32277501384993096
Feature: [0.69], Label: [0.63653718]
Output:  0.6561528458678751
Feature: [0.83], Label: [0.73793137]
Output:  0.7479753441864303
Epoch: 2000 RMSE = 0.02310377543680707
Epoch: 2100 RMSE = 0.02296912180225883
Epoch: 2200 RMSE = 0.022818386109133847
Epoch: 2300 RMSE = 0.022785894086482062
Epoch: 2400 RMSE = 0.022705715559151414
Epoch: 2500 RMSE = 0.02269614382539823
Epoch: 2600 RMSE = 0.022717360755577686
Epoch: 2700 RMSE = 0.02274198920647129
Epoch: 2800 RMSE = 0.022761918066754233
Epoch: 2900 RMSE = 0.022787468990294345
Feature: [0.48], Label: [0.46177918]
Output:  0.4588719596910902
Feature: [0.69], Label: [0.63653718]
Output:  0.6603597048654979
Feature: [0.8], Label: [0.71735609]
Output:  0.7391046570966636
Feature: [1.46], Label: [0.99386836]
Output:  0.929572417239927
Feature: [0.49], Label: [0.47062589]
Output:  0.4694174393232242
Feature: [0.44], Label: [0.42593947]
Output:  0.4160490726848947
Feature: [0.39], Label: [0.38018842]
Output:  0.36291916973087984
Feature: [0.21], Label: [0.2084599]
Output:  0.19467892107090012
Feature: [0.47], Label: [0.45288629]
Output:  0.44824903408113215
Feature: [0.53], Label: [0.50553334]
Output:  0.5114413255118475
Feature: [0.66], Label: [0.61311685]
Output:  0.6353613813853822
Feature: [0.82], Label: [0.73114583]
Output:  0.7513225970304055
Feature: [1.48], Label: [0.99588084]
Output:  0.9316265306854504
Feature: [0.15], Label: [0.14943813]
Output:  0.1519092189099921
Feature: [1.1], Label: [0.89120736]
Output:  0.8673218844325111
Feature: [0.34], Label: [0.33348709]
Output:  0.31147924547747186
Feature: [0.08], Label: [0.07991469]
Output:  0.1116029222579099
Feature: [0.24], Label: [0.23770263]
Output:  0.21888199777778644
Feature: [1.36], Label: [0.9778646]
Output:  0.9177541766396323
Feature: [0.61], Label: [0.57286746]
Output:  0.590544122417015
Feature: [0.9], Label: [0.78332691]
Output:  0.7942093929877537
Feature: [1.2], Label: [0.93203909]
Output:  0.8910486058286031
Feature: [0.87], Label: [0.76432894]
Output:  0.7792593558671349
Feature: [0.17], Label: [0.16918235]
Output:  0.1653464415452784
Feature: [0.97], Label: [0.82488571]
Output:  0.8246453688846807
Feature: [0.54], Label: [0.51413599]
Output:  0.5217197251926591
Feature: [1.45], Label: [0.99271299]
Output:  0.9285603045300669
Feature: [0.56], Label: [0.5311862]
Output:  0.5420003293293824
Feature: [0.01], Label: [0.00999983]
Output:  0.08070315013697732
Feature: [0.83], Label: [0.73793137]
Output:  0.7572381142719186
Feature: [0.41], Label: [0.39860933]
Output:  0.38405006402970576
Epoch: 3000 RMSE = 0.022800129867803488
Epoch: 3100 RMSE = 0.022807565029320954
Epoch: 3200 RMSE = 0.02283469004250736
Epoch: 3300 RMSE = 0.022846885240311008
Epoch: 3400 RMSE = 0.02284907817080846
Epoch: 3500 RMSE = 0.022853343108617412
Epoch: 3600 RMSE = 0.022837811485748382
Epoch: 3700 RMSE = 0.022826923450240632
Epoch: 3800 RMSE = 0.022813676271148484
Epoch: 3900 RMSE = 0.022775469988213844
Feature: [1.46], Label: [0.99386836]
Output:  0.9347432642446969
Feature: [0.21], Label: [0.2084599]
Output:  0.1933928015135502
Feature: [0.01], Label: [0.00999983]
Output:  0.08082398731633848
Feature: [1.1], Label: [0.89120736]
Output:  0.8721160051292958
Feature: [0.53], Label: [0.50553334]
Output:  0.5092688311751393
Feature: [0.83], Label: [0.73793137]
Output:  0.759569562601318
Feature: [0.8], Label: [0.71735609]
Output:  0.7410182887409176
Feature: [1.48], Label: [0.99588084]
Output:  0.9367482701839971
Feature: [0.15], Label: [0.14943813]
Output:  0.15115688910281155
Feature: [0.9], Label: [0.78332691]
Output:  0.7973363938300562
Feature: [0.17], Label: [0.16918235]
Output:  0.16436470968530026
Feature: [0.56], Label: [0.5311862]
Output:  0.5399861899980274
Feature: [0.87], Label: [0.76432894]
Output:  0.7819495738558769
Feature: [0.08], Label: [0.07991469]
Output:  0.11131693009252215
Feature: [0.48], Label: [0.46177918]
Output:  0.4561306552132366
Feature: [1.45], Label: [0.99271299]
Output:  0.933659454207728
Feature: [0.82], Label: [0.73114583]
Output:  0.7534382434373309
Feature: [0.41], Label: [0.39860933]
Output:  0.3812241090796446
Feature: [0.97], Label: [0.82488571]
Output:  0.8284423398568854
Feature: [0.34], Label: [0.33348709]
Output:  0.3089400348499584
Feature: [0.39], Label: [0.38018842]
Output:  0.36022483955023
Feature: [0.61], Label: [0.57286746]
Output:  0.5892452998486198
Feature: [1.36], Label: [0.9778646]
Output:  0.922928137024309
Feature: [0.69], Label: [0.63653718]
Output:  0.6604461134428453
Feature: [0.24], Label: [0.23770263]
Output:  0.2172311582674285
Feature: [0.47], Label: [0.45288629]
Output:  0.4455599722985863
Feature: [1.2], Label: [0.93203909]
Output:  0.8961071308408487
Feature: [0.66], Label: [0.61311685]
Output:  0.6349666635308948
Feature: [0.49], Label: [0.47062589]
Output:  0.46694812117904055
Feature: [0.54], Label: [0.51413599]
Output:  0.5195541299440237
Feature: [0.44], Label: [0.42593947]
Output:  0.4133658727910196
Epoch: 4000 RMSE = 0.022760133430078742
Epoch: 4100 RMSE = 0.022741182614806805
Epoch: 4200 RMSE = 0.022707064098718324
Epoch: 4300 RMSE = 0.022670575722988216
Epoch: 4400 RMSE = 0.022641148061691773
Epoch: 4500 RMSE = 0.02260329714819246
Epoch: 4600 RMSE = 0.022572602797598176
Epoch: 4700 RMSE = 0.022523243938220344
Epoch: 4800 RMSE = 0.02249737829949818
Epoch: 4900 RMSE = 0.022462712112021135
Feature: [0.54], Label: [0.51413599]
Output:  0.5181203893689871
Feature: [1.46], Label: [0.99386836]
Output:  0.9378598141863579
Feature: [1.48], Label: [0.99588084]
Output:  0.9398936135639708
Feature: [0.66], Label: [0.61311685]
Output:  0.6340750998629816
Feature: [1.2], Label: [0.93203909]
Output:  0.8989418322805132
Feature: [0.34], Label: [0.33348709]
Output:  0.30865843928582476
Feature: [0.21], Label: [0.2084599]
Output:  0.19419283055399325
Feature: [0.41], Label: [0.39860933]
Output:  0.3804979783848812
Feature: [0.48], Label: [0.46177918]
Output:  0.45512198477064103
Feature: [0.61], Label: [0.57286746]
Output:  0.5882248425155221
Feature: [0.83], Label: [0.73793137]
Output:  0.7602606756952199
Feature: [0.82], Label: [0.73114583]
Output:  0.754105197078575
Feature: [0.97], Label: [0.82488571]
Output:  0.8302851000369927
Feature: [1.1], Label: [0.89120736]
Output:  0.8745941818727891
Feature: [0.47], Label: [0.45288629]
Output:  0.4442965810189273
Feature: [0.15], Label: [0.14943813]
Output:  0.1523625838373766
Feature: [0.56], Label: [0.5311862]
Output:  0.5387047811020795
Feature: [0.87], Label: [0.76432894]
Output:  0.7830176021541724
Feature: [0.17], Label: [0.16918235]
Output:  0.16544484622816905
Feature: [0.53], Label: [0.50553334]
Output:  0.5077426917316241
Feature: [0.44], Label: [0.42593947]
Output:  0.4121992589265714
Feature: [0.69], Label: [0.63653718]
Output:  0.6597788819600059
Feature: [1.45], Label: [0.99271299]
Output:  0.9368033381753049
Feature: [0.24], Label: [0.23770263]
Output:  0.21781036445441854
Feature: [0.39], Label: [0.38018842]
Output:  0.3594622797416809
Feature: [0.49], Label: [0.47062589]
Output:  0.46568603631519895
Feature: [0.9], Label: [0.78332691]
Output:  0.7986671366028596
Feature: [0.08], Label: [0.07991469]
Output:  0.11279900566936371
Feature: [0.8], Label: [0.71735609]
Output:  0.7413862384573322
Feature: [1.36], Label: [0.9778646]
Output:  0.926019122516255
Feature: [0.01], Label: [0.00999983]
Output:  0.08229142925369921
Epoch: 5000 RMSE = 0.022421560924806398
Epoch: 5100 RMSE = 0.022396557438763814
Epoch: 5200 RMSE = 0.02235687968133337
Epoch: 5300 RMSE = 0.02232734100204988
Epoch: 5400 RMSE = 0.022287973933569738
Epoch: 5500 RMSE = 0.022251707049167395
Epoch: 5600 RMSE = 0.02222198436365193
Epoch: 5700 RMSE = 0.022188878859441166
Epoch: 5800 RMSE = 0.022169717789650316
Epoch: 5900 RMSE = 0.02215213138899086
Feature: [0.56], Label: [0.5311862]
Output:  0.5375405136212826
Feature: [0.53], Label: [0.50553334]
Output:  0.5066501398290079
Feature: [0.15], Label: [0.14943813]
Output:  0.15352369652224182
Feature: [1.36], Label: [0.9778646]
Output:  0.9282001069557307
Feature: [0.44], Label: [0.42593947]
Output:  0.41148415240028174
Feature: [0.08], Label: [0.07991469]
Output:  0.1141525668195173
Feature: [1.1], Label: [0.89120736]
Output:  0.8762768068070299
Feature: [0.69], Label: [0.63653718]
Output:  0.6591161219222638
Feature: [0.41], Label: [0.39860933]
Output:  0.37980129790248024
Feature: [1.46], Label: [0.99386836]
Output:  0.9401065043223904
Feature: [0.87], Label: [0.76432894]
Output:  0.7835367155767777
Feature: [0.54], Label: [0.51413599]
Output:  0.5170806900947217
Feature: [0.48], Label: [0.46177918]
Output:  0.45401248947821093
Feature: [0.9], Label: [0.78332691]
Output:  0.7992943855975487
Feature: [0.82], Label: [0.73114583]
Output:  0.7541723237525456
Feature: [0.34], Label: [0.33348709]
Output:  0.30855473722121607
Feature: [0.83], Label: [0.73793137]
Output:  0.7603377314072175
Feature: [0.21], Label: [0.2084599]
Output:  0.19503548979200205
Feature: [0.49], Label: [0.47062589]
Output:  0.4645683701914145
Feature: [0.39], Label: [0.38018842]
Output:  0.35900029650240983
Feature: [0.8], Label: [0.71735609]
Output:  0.7413862638337612
Feature: [0.17], Label: [0.16918235]
Output:  0.16656668790710527
Feature: [0.01], Label: [0.00999983]
Output:  0.08366701391052445
Feature: [1.45], Label: [0.99271299]
Output:  0.9390266035358438
Feature: [0.97], Label: [0.82488571]
Output:  0.8313427987253347
Feature: [0.66], Label: [0.61311685]
Output:  0.6331178877730438
Feature: [1.2], Label: [0.93203909]
Output:  0.900850448529207
Feature: [0.47], Label: [0.45288629]
Output:  0.4432945489685614
Feature: [1.48], Label: [0.99588084]
Output:  0.9421135074094539
Feature: [0.61], Label: [0.57286746]
Output:  0.5869888455210251
Feature: [0.24], Label: [0.23770263]
Output:  0.21851432959839528
Epoch: 6000 RMSE = 0.022104211387186597
Epoch: 6100 RMSE = 0.022084742992053995
Epoch: 6200 RMSE = 0.022047312298607954
Epoch: 6300 RMSE = 0.02202369854583599
Epoch: 6400 RMSE = 0.02200192339596618
Epoch: 6500 RMSE = 0.021963240125746977
Epoch: 6600 RMSE = 0.021923575918903808
Epoch: 6700 RMSE = 0.02192378487020814
Epoch: 6800 RMSE = 0.021890299418598255
Epoch: 6900 RMSE = 0.02187796447737497
Feature: [0.83], Label: [0.73793137]
Output:  0.7604754277701035
Feature: [0.54], Label: [0.51413599]
Output:  0.5161581277460618
Feature: [0.8], Label: [0.71735609]
Output:  0.7412586172583616
Feature: [0.41], Label: [0.39860933]
Output:  0.3793064328173906
Feature: [0.48], Label: [0.46177918]
Output:  0.45321462778628774
Feature: [0.61], Label: [0.57286746]
Output:  0.5861237649245404
Feature: [1.46], Label: [0.99386836]
Output:  0.9418011101216679
Feature: [1.48], Label: [0.99588084]
Output:  0.9438396841070943
Feature: [0.47], Label: [0.45288629]
Output:  0.44268565453254455
Feature: [0.44], Label: [0.42593947]
Output:  0.41095567662169685
Feature: [0.87], Label: [0.76432894]
Output:  0.7838658945636169
Feature: [0.15], Label: [0.14943813]
Output:  0.15452549297926835
Feature: [0.34], Label: [0.33348709]
Output:  0.30864697879281633
Feature: [0.82], Label: [0.73114583]
Output:  0.7543112360176153
Feature: [0.97], Label: [0.82488571]
Output:  0.8321775773452252
Feature: [0.69], Label: [0.63653718]
Output:  0.6584805250503113
Feature: [0.9], Label: [0.78332691]
Output:  0.7996760338539313
Feature: [0.08], Label: [0.07991469]
Output:  0.1152184988908704
Feature: [0.01], Label: [0.00999983]
Output:  0.08475040221480236
Feature: [0.56], Label: [0.5311862]
Output:  0.5364785121578544
Feature: [0.66], Label: [0.61311685]
Output:  0.6322435894561972
Feature: [1.2], Label: [0.93203909]
Output:  0.902279566787711
Feature: [1.36], Label: [0.9778646]
Output:  0.9298291904977839
Feature: [1.1], Label: [0.89120736]
Output:  0.8774346588602211
Feature: [0.39], Label: [0.38018842]
Output:  0.3585701701525795
Feature: [0.17], Label: [0.16918235]
Output:  0.16743231535770425
Feature: [0.49], Label: [0.47062589]
Output:  0.4637604425646629
Feature: [0.53], Label: [0.50553334]
Output:  0.5057682914292684
Feature: [0.24], Label: [0.23770263]
Output:  0.219102443494156
Feature: [0.21], Label: [0.2084599]
Output:  0.19579723623128492
Feature: [1.45], Label: [0.99271299]
Output:  0.9407662036570921
Epoch: 7000 RMSE = 0.02183286564171091
Epoch: 7100 RMSE = 0.021817657465449284
Epoch: 7200 RMSE = 0.021800249258070663
Epoch: 7300 RMSE = 0.021766873082826464
Epoch: 7400 RMSE = 0.0217470570379079
Epoch: 7500 RMSE = 0.02173989823915038
Epoch: 7600 RMSE = 0.021706673080255427
Epoch: 7700 RMSE = 0.021691947768059987
Epoch: 7800 RMSE = 0.021686476136631213
Epoch: 7900 RMSE = 0.021666483974503253
Feature: [1.36], Label: [0.9778646]
Output:  0.9312825033524373
Feature: [0.9], Label: [0.78332691]
Output:  0.8002021162620285
Feature: [0.39], Label: [0.38018842]
Output:  0.3585264710732221
Feature: [1.48], Label: [0.99588084]
Output:  0.9452768813204656
Feature: [0.47], Label: [0.45288629]
Output:  0.4422943171294861
Feature: [0.66], Label: [0.61311685]
Output:  0.632124158229449
Feature: [0.61], Label: [0.57286746]
Output:  0.5856393900647022
Feature: [1.2], Label: [0.93203909]
Output:  0.9036479078757435
Feature: [0.69], Label: [0.63653718]
Output:  0.6581328380454322
Feature: [0.21], Label: [0.2084599]
Output:  0.19642550869100386
Feature: [1.46], Label: [0.99386836]
Output:  0.9432362066306866
Feature: [0.83], Label: [0.73793137]
Output:  0.7606364241893392
Feature: [0.8], Label: [0.71735609]
Output:  0.7412977362134424
Feature: [0.82], Label: [0.73114583]
Output:  0.7542377271477929
Feature: [0.48], Label: [0.46177918]
Output:  0.45258331174352995
Feature: [0.44], Label: [0.42593947]
Output:  0.4103883845310072
Feature: [0.41], Label: [0.39860933]
Output:  0.3790696371508232
Feature: [0.24], Label: [0.23770263]
Output:  0.21965018594890606
Feature: [0.15], Label: [0.14943813]
Output:  0.15531078002315307
Feature: [0.53], Label: [0.50553334]
Output:  0.5052415112531358
Feature: [0.34], Label: [0.33348709]
Output:  0.3086831230194169
Feature: [0.87], Label: [0.76432894]
Output:  0.7841578674694889
Feature: [1.1], Label: [0.89120736]
Output:  0.8785935899570432
Feature: [0.97], Label: [0.82488571]
Output:  0.8328776513149937
Feature: [0.01], Label: [0.00999983]
Output:  0.08567660993572335
Feature: [0.08], Label: [0.07991469]
Output:  0.11611966311360818
Feature: [0.49], Label: [0.47062589]
Output:  0.4632578921441314
Feature: [1.45], Label: [0.99271299]
Output:  0.9421725806841985
Feature: [0.56], Label: [0.5311862]
Output:  0.5360728816940165
Feature: [0.54], Label: [0.51413599]
Output:  0.5155768953772005
Feature: [0.17], Label: [0.16918235]
Output:  0.16821055001956992
Epoch: 8000 RMSE = 0.021655422405901983
Epoch: 8100 RMSE = 0.021629081040745568
Epoch: 8200 RMSE = 0.02162196070907265
Epoch: 8300 RMSE = 0.02160001887803217
Epoch: 8400 RMSE = 0.021586249992288503
Epoch: 8500 RMSE = 0.021568465923340736
Epoch: 8600 RMSE = 0.021578524146891175
Epoch: 8700 RMSE = 0.021547664436240333
Epoch: 8800 RMSE = 0.021528723916832547
Epoch: 8900 RMSE = 0.02152577774375596
Feature: [0.83], Label: [0.73793137]
Output:  0.7606557054326493
Feature: [0.87], Label: [0.76432894]
Output:  0.7842485037163157
Feature: [0.53], Label: [0.50553334]
Output:  0.5045159914132703
Feature: [0.97], Label: [0.82488571]
Output:  0.8333018238545647
Feature: [0.21], Label: [0.2084599]
Output:  0.19682769369063122
Feature: [0.69], Label: [0.63653718]
Output:  0.6575233921230633
Feature: [0.47], Label: [0.45288629]
Output:  0.4415056864050954
Feature: [0.15], Label: [0.14943813]
Output:  0.15584824773716005
Feature: [0.24], Label: [0.23770263]
Output:  0.21993019409056552
Feature: [1.1], Label: [0.89120736]
Output:  0.8793658134690546
Feature: [0.82], Label: [0.73114583]
Output:  0.754245717694518
Feature: [0.17], Label: [0.16918235]
Output:  0.16871687429962498
Feature: [0.56], Label: [0.5311862]
Output:  0.5352597775230356
Feature: [1.48], Label: [0.99588084]
Output:  0.9463727223415135
Feature: [0.44], Label: [0.42593947]
Output:  0.40997130556234296
Feature: [1.45], Label: [0.99271299]
Output:  0.9433087777146678
Feature: [0.39], Label: [0.38018842]
Output:  0.3582591931020659
Feature: [0.49], Label: [0.47062589]
Output:  0.46280489530112995
Feature: [0.61], Label: [0.57286746]
Output:  0.5850309565496143
Feature: [0.8], Label: [0.71735609]
Output:  0.7412533810525751
Feature: [0.48], Label: [0.46177918]
Output:  0.45216784381084757
Feature: [0.08], Label: [0.07991469]
Output:  0.11681861917793429
Feature: [0.41], Label: [0.39860933]
Output:  0.3787692627384083
Feature: [1.2], Label: [0.93203909]
Output:  0.9046323591375912
Feature: [0.66], Label: [0.61311685]
Output:  0.6315039339683854
Feature: [0.9], Label: [0.78332691]
Output:  0.8004297914431558
Feature: [1.36], Label: [0.9778646]
Output:  0.9323859540879359
Feature: [1.46], Label: [0.99386836]
Output:  0.9443792530673172
Feature: [0.01], Label: [0.00999983]
Output:  0.08637448283363416
Feature: [0.34], Label: [0.33348709]
Output:  0.3085969509653225
Feature: [0.54], Label: [0.51413599]
Output:  0.5150074814796883
Epoch: 9000 RMSE = 0.02150925681988088
Epoch: 9100 RMSE = 0.021491744759018425
Epoch: 9200 RMSE = 0.021489843837147866
Epoch: 9300 RMSE = 0.021473869035797923
Epoch: 9400 RMSE = 0.02145721527851281
Epoch: 9500 RMSE = 0.02143928327471637
Epoch: 9600 RMSE = 0.021436220238918793
Epoch: 9700 RMSE = 0.021425162212601035
Epoch: 9800 RMSE = 0.02140476221445595
Epoch: 9900 RMSE = 0.021404194472575074
Feature: [1.2], Label: [0.93203909]
Output:  0.9055358410441652
Feature: [0.48], Label: [0.46177918]
Output:  0.45194875443021415
Feature: [0.01], Label: [0.00999983]
Output:  0.08699088942339955
Feature: [1.48], Label: [0.99588084]
Output:  0.947434435063004
Feature: [1.1], Label: [0.89120736]
Output:  0.8802479536866277
Feature: [0.66], Label: [0.61311685]
Output:  0.6312600699311368
Feature: [0.34], Label: [0.33348709]
Output:  0.3086836172525503
Feature: [0.17], Label: [0.16918235]
Output:  0.16931229634503173
Feature: [0.53], Label: [0.50553334]
Output:  0.5043372483551863
Feature: [0.97], Label: [0.82488571]
Output:  0.83396462689476
Feature: [0.15], Label: [0.14943813]
Output:  0.1564536239655818
Feature: [1.46], Label: [0.99386836]
Output:  0.9454134713062701
Feature: [0.56], Label: [0.5311862]
Output:  0.5351531338070559
Feature: [0.82], Label: [0.73114583]
Output:  0.7545267018139434
Feature: [1.45], Label: [0.99271299]
Output:  0.9443454368228764
Feature: [0.44], Label: [0.42593947]
Output:  0.40990728373070173
Feature: [0.83], Label: [0.73793137]
Output:  0.7608768566723734
Feature: [0.41], Label: [0.39860933]
Output:  0.3786919327439235
Feature: [0.8], Label: [0.71735609]
Output:  0.7413989499695868
Feature: [0.69], Label: [0.63653718]
Output:  0.6574145635665607
Feature: [0.24], Label: [0.23770263]
Output:  0.22032919292916506
Feature: [0.47], Label: [0.45288629]
Output:  0.4413575651149588
Feature: [0.61], Label: [0.57286746]
Output:  0.5846167622250423
Feature: [0.49], Label: [0.47062589]
Output:  0.46240322707296305
Feature: [0.21], Label: [0.2084599]
Output:  0.19731988985214477
Feature: [1.36], Label: [0.9778646]
Output:  0.9334133239470034
Feature: [0.87], Label: [0.76432894]
Output:  0.7846040399452966
Feature: [0.39], Label: [0.38018842]
Output:  0.35819570937520845
Feature: [0.54], Label: [0.51413599]
Output:  0.5146669181103466
Feature: [0.08], Label: [0.07991469]
Output:  0.11744877084530514
Feature: [0.9], Label: [0.78332691]
Output:  0.8008351123946017
Epoch: 10000 RMSE = 0.021399666228273086
Training finished.
 Final Training RMSE = 0.021399666228273086 

----- starting test
input_value: 0.0
output_value: 0.08325826588468632
expected_value: 0.0
input_value: 0.02
output_value: 0.09084785960634838
expected_value: 0.0199986666933331
input_value: 0.03
output_value: 0.09487072016900548
expected_value: 0.0299955002024957
input_value: 0.04
output_value: 0.09905096958142885
expected_value: 0.0399893341866342
input_value: 0.05
output_value: 0.1033925153369237
expected_value: 0.0499791692706783
input_value: 0.06
output_value: 0.10789915979962435
expected_value: 0.0599640064794446
input_value: 0.07
output_value: 0.11257457960642982
expected_value: 0.0699428473375328
input_value: 0.09
output_value: 0.12244569301633097
expected_value: 0.089878549198011
input_value: 0.1
output_value: 0.12764791308338308
expected_value: 0.0998334166468282
input_value: 0.11
output_value: 0.13303191437223646
expected_value: 0.109778300837175
input_value: 0.12
output_value: 0.13860040580063093
expected_value: 0.119712207288919
input_value: 0.13
output_value: 0.1443558303744266
expected_value: 0.129634142619695
input_value: 0.14
output_value: 0.1503003401867481
expected_value: 0.139543114644236
input_value: 0.16
output_value: 0.16276361926415978
expected_value: 0.159318206614246
input_value: 0.18
output_value: 0.1760006958394235
expected_value: 0.179029573425824
input_value: 0.19
output_value: 0.18291099381163736
expected_value: 0.188858894976501
input_value: 0.2
output_value: 0.1900158020679578
expected_value: 0.198669330795061
input_value: 0.22
output_value: 0.20480623398399933
expected_value: 0.218229623080869
input_value: 0.23
output_value: 0.2124892986163323
expected_value: 0.227977523535188
input_value: 0.25
output_value: 0.22842096007981916
expected_value: 0.247403959254523
input_value: 0.26
output_value: 0.2366639316230704
expected_value: 0.257080551892155
input_value: 0.27
output_value: 0.2450870266187443
expected_value: 0.266731436688831
input_value: 0.28
output_value: 0.25368609472371734
expected_value: 0.276355648564114
input_value: 0.29
output_value: 0.26245644618477737
expected_value: 0.285952225104836
input_value: 0.3
output_value: 0.2713928546371715
expected_value: 0.29552020666134
input_value: 0.31
output_value: 0.2804895634321932
expected_value: 0.305058636443443
input_value: 0.32
output_value: 0.2897402955735678
expected_value: 0.314566560616118
input_value: 0.33
output_value: 0.2991382673022471
expected_value: 0.324043028394868
input_value: 0.35
output_value: 0.3183463676509155
expected_value: 0.342897807455451
input_value: 0.36
output_value: 0.32814056790896096
expected_value: 0.35227423327509
input_value: 0.37
output_value: 0.338050203065791
expected_value: 0.361615431964962
input_value: 0.38
output_value: 0.348066284304158
expected_value: 0.370920469412983
input_value: 0.4
output_value: 0.36838010661676845
expected_value: 0.389418342308651
input_value: 0.42
output_value: 0.3890037597182955
expected_value: 0.40776045305957
input_value: 0.43
output_value: 0.39940624810044617
expected_value: 0.416870802429211
input_value: 0.45
output_value: 0.42034004497248567
expected_value: 0.43496553411123
input_value: 0.46
output_value: 0.43085006774214823
expected_value: 0.44394810696552
input_value: 0.5
output_value: 0.4729291239406373
expected_value: 0.479425538604203
input_value: 0.51
output_value: 0.4834061308783026
expected_value: 0.488177246882907
input_value: 0.52
output_value: 0.49384556943899355
expected_value: 0.496880137843737
input_value: 0.55
output_value: 0.5248413382989433
expected_value: 0.522687228930659
input_value: 0.57
output_value: 0.5451446206421086
expected_value: 0.539632048733969
input_value: 0.58
output_value: 0.5551624114576138
expected_value: 0.548023936791874
input_value: 0.59
output_value: 0.565080468122431
expected_value: 0.556361022912784
input_value: 0.6
output_value: 0.5748914434795335
expected_value: 0.564642473395035
input_value: 0.62
output_value: 0.5941649735979032
expected_value: 0.581035160537305
input_value: 0.63
output_value: 0.6036150756342515
expected_value: 0.58914475794227
input_value: 0.64
output_value: 0.6129332034795839
expected_value: 0.597195441362392
input_value: 0.65
output_value: 0.6221142894945692
expected_value: 0.60518640573604
input_value: 0.67
output_value: 0.6400473855347524
expected_value: 0.62098598703656
input_value: 0.68
output_value: 0.648791567619007
expected_value: 0.628793024018469
input_value: 0.7
output_value: 0.6658189955950834
expected_value: 0.644217687237691
input_value: 0.71
output_value: 0.6740970641249965
expected_value: 0.651833771021537
input_value: 0.72
output_value: 0.6822152800736819
expected_value: 0.659384671971473
input_value: 0.73
output_value: 0.6901720773184135
expected_value: 0.666869635003698
input_value: 0.74
output_value: 0.697966271401135
expected_value: 0.674287911628145
input_value: 0.75
output_value: 0.7055970427202768
expected_value: 0.681638760023334
input_value: 0.76
output_value: 0.7130639189673919
expected_value: 0.688921445110551
input_value: 0.77
output_value: 0.7203667569917966
expected_value: 0.696135238627357
input_value: 0.78
output_value: 0.7275057242655708
expected_value: 0.70327941920041
input_value: 0.79
output_value: 0.7344812801094655
expected_value: 0.710353272417608
input_value: 0.81
output_value: 0.7479453408872557
expected_value: 0.724287174370143
input_value: 0.84
output_value: 0.7669420244821815
expected_value: 0.744643119970859
input_value: 0.85
output_value: 0.7729607393290587
expected_value: 0.751280405140293
input_value: 0.86
output_value: 0.7788258649095969
expected_value: 0.757842562895277
input_value: 0.88
output_value: 0.790104010160019
expected_value: 0.770738878898969
input_value: 0.89
output_value: 0.7955216763274154
expected_value: 0.777071747526824
input_value: 0.91
output_value: 0.8059266046282989
expected_value: 0.78950373968995
input_value: 0.92
output_value: 0.8109190897825082
expected_value: 0.795601620036366
input_value: 0.93
output_value: 0.8157751853957927
expected_value: 0.801619940883777
input_value: 0.94
output_value: 0.8204976570272734
expected_value: 0.807558100405114
input_value: 0.95
output_value: 0.8250893117486662
expected_value: 0.813415504789374
input_value: 0.96
output_value: 0.8295529881073521
expected_value: 0.819191568300998
input_value: 0.98
output_value: 0.8381078620331411
expected_value: 0.83049737049197
input_value: 0.99
output_value: 0.8422048135657625
expected_value: 0.836025978600521
input_value: 1.0
output_value: 0.8461852793835196
expected_value: 0.841470984807897
input_value: 1.01
output_value: 0.8500521290062057
expected_value: 0.846831844618015
input_value: 1.02
output_value: 0.8538082173855899
expected_value: 0.852108021949363
input_value: 1.03
output_value: 0.857456379371289
expected_value: 0.857298989188603
input_value: 1.04
output_value: 0.8609994247155297
expected_value: 0.862404227243338
input_value: 1.05
output_value: 0.8644401335880882
expected_value: 0.867423225594017
input_value: 1.06
output_value: 0.8677812525726505
expected_value: 0.872355482344986
input_value: 1.07
output_value: 0.8710254911160028
expected_value: 0.877200504274682
input_value: 1.08
output_value: 0.874175518401865
expected_value: 0.881957806884948
input_value: 1.09
output_value: 0.8772339606217271
expected_value: 0.886626914449487
input_value: 1.11
output_value: 0.8830863658576933
expected_value: 0.895698685680048
input_value: 1.12
output_value: 0.8858853467584574
expected_value: 0.900100442176505
input_value: 1.13
output_value: 0.8886027752643926
expected_value: 0.904412189378826
input_value: 1.14
output_value: 0.8912410337268466
expected_value: 0.908633496115883
input_value: 1.15
output_value: 0.8938024520210751
expected_value: 0.912763940260521
input_value: 1.16
output_value: 0.8962893068934501
expected_value: 0.916803108771767
input_value: 1.17
output_value: 0.8987038215170926
expected_value: 0.920750597736136
input_value: 1.18
output_value: 0.9010481652371501
expected_value: 0.92460601240802
input_value: 1.19
output_value: 0.903324453488041
expected_value: 0.928368967249167
input_value: 1.21
output_value: 0.907681056341783
expected_value: 0.935616001553386
input_value: 1.22
output_value: 0.9097653335977919
expected_value: 0.939099356319068
input_value: 1.23
output_value: 0.9117894814781016
expected_value: 0.942488801931697
input_value: 1.24
output_value: 0.9137553495367877
expected_value: 0.945783999449539
input_value: 1.25
output_value: 0.9156647356740955
expected_value: 0.948984619355586
input_value: 1.26
output_value: 0.9175193868492478
expected_value: 0.952090341590516
input_value: 1.27
output_value: 0.9193209998599828
expected_value: 0.955100855584692
input_value: 1.28
output_value: 0.92107122217964
expected_value: 0.958015860289225
input_value: 1.29
output_value: 0.9227716528433589
expected_value: 0.960835064206073
input_value: 1.3
output_value: 0.9244238433756614
expected_value: 0.963558185417193
input_value: 1.31
output_value: 0.9260292987523397
expected_value: 0.966184951612734
input_value: 1.32
output_value: 0.9275894783902077
expected_value: 0.968715100118265
input_value: 1.33
output_value: 0.9291057971588377
expected_value: 0.971148377921045
input_value: 1.34
output_value: 0.9305796264089627
expected_value: 0.973484541695319
input_value: 1.35
output_value: 0.9320122950127199
expected_value: 0.975723357826659
input_value: 1.37
output_value: 0.9347592596666929
expected_value: 0.979908061398614
input_value: 1.38
output_value: 0.9360760105122178
expected_value: 0.98185353037236
input_value: 1.39
output_value: 0.9373565124017086
expected_value: 0.983700814811277
input_value: 1.4
output_value: 0.9386018975515676
expected_value: 0.98544972998846
input_value: 1.41
output_value: 0.9398132619750169
expected_value: 0.98710010101385
input_value: 1.42
output_value: 0.9409916665057749
expected_value: 0.98865176285172
input_value: 1.43
output_value: 0.9421381378093373
expected_value: 0.990104560337178
input_value: 1.44
output_value: 0.9432536693802036
expected_value: 0.991458348191686
input_value: 1.47
output_value: 0.9464240835751216
expected_value: 0.994924349777581
input_value: 1.49
output_value: 0.9483998038407545
expected_value: 0.996737752043143
input_value: 1.5
output_value: 0.9493488243355469
expected_value: 0.997494986604054
input_value: 1.51
output_value: 0.9502730110137401
expected_value: 0.998152472497548
input_value: 1.52
output_value: 0.9511731258294427
expected_value: 0.998710143975583
input_value: 1.53
output_value: 0.9520499057318592
expected_value: 0.999167945271476
input_value: 1.54
output_value: 0.9529040634716165
expected_value: 0.999525830605479
input_value: 1.55
output_value: 0.9537362883859609
expected_value: 0.999783764189357
input_value: 1.56
output_value: 0.9545472471628459
expected_value: 0.999941720229966
input_value: 1.57
output_value: 0.9553375845839837
expected_value: 0.999999682931835
Final Testing RMSE = 0.025150294163710566

Process finished with exit code 0

"""