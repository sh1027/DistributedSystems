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
Thread-0: Transaction Completed. | before:  1,000 | amount:    -96 | after:    904 |
Thread-1: Transaction Completed. | before:    904 | amount:    -11 | after:    893 |
Thread-2: Transaction Completed. | before:    893 | amount:    -90 | after:    803 |
Thread-3: Transaction Completed. | before:    803 | amount:     11 | after:    814 |
Thread-4: Transaction Completed. | before:    814 | amount:     57 | after:    871 |
Thread-5: Transaction Completed. | before:    871 | amount:    -42 | after:    829 |
Thread-6: Transaction Completed. | before:    829 | amount:     19 | after:    848 |
Thread-7: Transaction Completed. | before:    848 | amount:     52 | after:    900 |
Thread-8: Transaction Completed. | before:    900 | amount:     13 | after:    913 |
Thread-9: Transaction Completed. | before:    913 | amount:    -33 | after:    880 |
```