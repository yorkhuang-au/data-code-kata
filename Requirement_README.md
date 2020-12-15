# data-code-kata

## problem 1

Work is in prob1/ folder.

In the prob1/ folder,

build docker: 
```{sh}
./build_docker.sh
```

test:
```
./test.sh
```

run:
```
./run.sh
```

Data are all in the data/ folder.


## problem 2

Work is in prob2/ folder.

In the prob2/ folder,

build docker:
```
./build_docker.sh
```

create 20G file:
```
./create.sh
```

process 20G file:
```
./process.sh
```

With Spark, it can procss large file by setting proper partition. Also it is good to tune number of workers and memory.



