from train_car import TrainCar
from train import Train


if __name__ == "__main__":
    traincar1 = TrainCar(1)
    traincar3 = TrainCar(3)
    traincar5 = TrainCar(5)
    traincar6 = TrainCar(6)
    traincar8 = TrainCar(8)
    print(traincar3.number)
    traincar1.add_passenger("Mike")
    traincar3.add_passengers(['John', 'Julia', 'Smith'])
    train = Train()
    train.add_traincar([traincar8])
    train.add_traincars([[traincar1], [traincar3], [traincar5], [traincar6]])
    print(train.__len__())
    print(traincar1.__len__())
    print(traincar3)
    print(train)
