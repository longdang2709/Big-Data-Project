
from mrjob.job import MRJob

class MRMinTemperature(MRJob):


    def mapper(self, _, line):
        (StateCode, Division, YearMonth, tavg, tmin, tmax, pcp, pdsi, phdi, zndx, pmdi,cdd, hdd, sp01, sp02, sp03, sp06, sp09, sp12, sp24) = line.split(",")
        yield YearMonth, tmax        
    def reducer(self, YearMonth, tmax):
        yield YearMonth, max(tmax)


if __name__ == '__main__':
    MRMinTemperature.run()
