from aircraft import Aircraft


if __name__ == '__main__':
    aircraft = Aircraft('turboprop', 1000)
    aircraft.increase_rotation = 10
    aircraft.increase_rotation = 10
    aircraft.increase_rotation = 10
    aircraft.increase_speed = 150
    aircraft.increase_speed = 150
    aircraft.increase_altitude = 1000
    aircraft.increase_altitude = 1000
    aircraft.increase_altitude = 1000
    print(aircraft.startup_engines())
    print(aircraft.take_off())
    aircraft.touching_ground()
    print(aircraft.land())
