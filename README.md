## Bitcask Python Key-Value Store

This is an implementation of the Bitcask key-value store. It is a log-structured 
hash table storage system meant for fast key-value data with high write and read performance.

You can read the paper here: [Bitcask: A Log-Structured Hash Table for Fast Key/Value Data](https://riak.com/assets/bitcask-intro.pdf)

I created a fork of `py-caskdb`, but this a new repo focusing on working further on what's next after the basic implementation

## Why and Why Python?
- I'm interested in databases and distributed systems and the bitcask paper looks friendly
- I'm porting to Golang as I'm making use of this opportunity to get better at Golang