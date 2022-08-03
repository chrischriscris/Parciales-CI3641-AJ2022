OCC = gcc
OFLAGS = `gnustep-config --objc-flags` -lgnustep-base -lobjc  -fopenmp

all: count_files vecmult

count_files: count_files.m
	$(OCC) count_files.m $(OFLAGS) -o count_files

vecmult: vecmult.m
	$(OCC) vecmult.m $(OFLAGS) -o vecmult

clean:
	rm -rf *.o *.d count_files vecmult