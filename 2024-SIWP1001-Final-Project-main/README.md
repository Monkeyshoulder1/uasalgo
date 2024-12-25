# 2024-SIWP1001-Final-Project

## Prerequiste

## Usage Guideline

### Structure of the project:
> overall of the project structure will be like this

```
├── arrays/
│   ├── kadane.py
│   ├── floyd.py
│   ├── kmp.py
│   ├── quick_select.py
│   └── boyer_moore.py
├── basic/
│   ├── euclidian.py
│   ├── huffman.py
│   └── union_find.py
├── docs
│   └── README.md
├── graphs/
│   ├── kruskal.py
│   ├── dijkstra.py
│   ├── bellman_ford.py
│   ├── floyd_warshall.py
│   ├── topological_sort.py
│   ├── flood_fill.py
│   └── lee.py
├── searching/
│   ├── binary.py
│   ├── linear.py
│   ├── depth_first.py
│   └── breadth_first.py
├── sorting/
│   ├── insertion_sort.py
│   ├── selection_sort.py
│   ├── heap_sort.py
│   ├── merge_sort.py
│   ├── quick_sort.py
│   └── counting_sort.py
├── main.py
├── utils.py
├── requirements.txt
├── README.md
└── tests/
    ├── test_basic.py
    ├── test_searching.py
    ├── test_sorting.py
    ├── test_arrays.py
    └── test_graphs.py
```

> add any required pip package if any inside requirements.txt

> add new algorithms inside the folder, named with algorithms name

> make a unit test of each algorithms in folder tests, see the test_searching.py example 


## Usage

```
python main.py --category searching --algorithm depth_first --params "{1: [2, 3], 2: [4], 3: [4], 4: []}" 1

```
