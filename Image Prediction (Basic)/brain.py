from imageai.Classification import ImageClassification
import os

exec_path = os.getcwd()

prediction = ImageClassification()
prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath('/Users/taruntp7/PycharmProjects/pythonProject/mobilenet_v2-b0353104.pth')
prediction.loadModel()
#MobileNetV is for now the latest faster and smaller predicting model, specifically the torch compatibel version

predictions, probabilities = prediction.classifyImage(os.path.join(exec_path, 'book.jpg'), result_count=5)
for eachPred, eachProb in zip(predictions, probabilities):
    print(f'{eachPred} : {eachProb}')


