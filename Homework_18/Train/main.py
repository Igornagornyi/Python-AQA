from train_car import TrainCar
from train import Train


if __name__ == "__main__":
    traincar1 = TrainCar('1')
    traincar3 = TrainCar('3')
    traincar5 = TrainCar('5')
    print(traincar3)
    traincar1.add_passenger("Mike")
    traincar3.add_passengers(['John', 'Julia', 'Smith'])
    tr = Train()
    tr.add_traincar(traincar5)
    tr.add_traincars([traincar1, traincar3, traincar5])
    print(tr.len())
    print(traincar1.len())
