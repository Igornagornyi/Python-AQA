from turboprop import TurbopropAircraft
from jetaircraft import JetAircraft


if __name__ == '__main__':
    turboprop = TurbopropAircraft('Cessna', altitude=0, speed=0, rotation=0, rate_climb=0)
    jetaircraft = JetAircraft('Boeing', altitude=5000, speed=500, rotation=100, rate_climb=0)
    print(jetaircraft.fly())
    print(turboprop.startup_engines())
    print(turboprop.take_off())
    print(turboprop.fly())
    print(turboprop.land())
