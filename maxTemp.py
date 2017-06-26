
from mrjob.job import MRJob
from mrjob.step import MRStep

class maxTemp(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                 reducer=self.reducer_count_ratings),
           MRStep(mapper=self.mapper_passthrough,
                 reducer = self.reducer_find_max)
        ]

    def mapper_get_ratings(self, _, line):
        (StateCode, Division, YearMonth, tavg, tmin, tmax, pcp, pdsi, phdi, zndx, pmdi,cdd, hdd, sp01, sp02, sp03, sp06, sp09, sp12, sp24) = line.split(",")
        yield YearMonth,float(tmax)
              
    def mapper_passthrough(self, key, values):
        yield key, values    
    
    def reducer_count_ratings(self, key, values):
        yield None, (max(values), key)
        
    def reducer_find_max(self, key, values):
        yield  max(values)
    
if __name__ == '__main__':
    maxTemp.run()