from train_car import TrainCar
from train import Train


if __name__ == "__main__":
    traincar = TrainCar()
    traincar2 = TrainCar()
    traincar3 = TrainCar()
    traincar.add_passenger("Mike")
    tr = Train()
    tr.add_traincars([traincar, traincar2, traincar3])
    print(tr.len())
    print(traincar.len())
