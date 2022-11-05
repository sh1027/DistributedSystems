# Multithread demo
## Contents
### `lock.py`:
銀行口座の入出金をイメージした，lockの機能を確認するためのデモプログラム

## Usage
### lockなしの場合
```sh 
python lock.py
```
### lockありの場合
```sh 
python lock.py --lock
```

## Output examples
### lockなしの場合
```sh
MainThread: Account created. Initial balance:  1,000
Thread-0: Transaction Completed. | before:  1,000 | amount:    -47 | after:    953 |
Thread-2: Transaction Completed. | before:    953 | amount:    -75 | after:    878 |
Thread-3: Transaction Completed. | before:    953 | amount:     53 | after:  1,006 |
Thread-4: Transaction Completed. | before:  1,006 | amount:     93 | after:  1,099 |
Thread-1: Transaction Completed. | before:  1,000 | amount:     33 | after:  1,033 |
Thread-6: Transaction Completed. | before:  1,033 | amount:    -39 | after:    994 |
Thread-5: Transaction Completed. | before:  1,099 | amount:     23 | after:  1,122 |
Thread-7: Transaction Completed. | before:    994 | amount:     81 | after:  1,075 |
Thread-9: Transaction Completed. | before:    994 | amount:    -98 | after:    896 |
Thread-8: Transaction Completed. | before:    994 | amount:    -45 | after:    949 |
```
### lockありの場合
```sh
MainThread: Account created. Initial balance:  1,000
Thread-1: Transaction Completed. | before:  1,000 | amount:     89 | after:  1,089 |
Thread-0: Transaction Completed. | before:  1,000 | amount:    -56 | after:    944 |
Thread-2: Transaction Completed. | before:  1,000 | amount:     97 | after:  1,097 |
Thread-5: Transaction Completed. | before:  1,097 | amount:    -11 | after:  1,086 |
Thread-4: Transaction Completed. | before:  1,097 | amount:    -90 | after:  1,007 |
Thread-3: Transaction Completed. | before:  1,089 | amount:    -11 | after:  1,078 |
Thread-8: Transaction Completed. | before:  1,078 | amount:     74 | after:  1,152 |
Thread-7: Transaction Completed. | before:  1,007 | amount:     23 | after:  1,030 |
Thread-6: Transaction Completed. | before:  1,007 | amount:     82 | after:  1,089 |
Thread-9: Transaction Completed. | before:  1,152 | amount:    -88 | after:  1,064 |
Thread-3: Transaction Completed. | before:  1,083 | amount:     88 | after:  1,171 |
Thread-4: Transaction Completed. | before:  1,171 | amount:     86 | after:  1,257 |
Thread-5: Transaction Completed. | before:  1,257 | amount:    -44 | after:  1,213 |
Thread-6: Transaction Completed. | before:  1,213 | amount:     -7 | after:  1,206 |
Thread-7: Transaction Completed. | before:  1,206 | amount:     66 | after:  1,272 |
Thread-8: Transaction Completed. | before:  1,272 | amount:     26 | after:  1,298 |
Thread-9: Transaction Completed. | before:  1,298 | amount:     31 | after:  1,329 |