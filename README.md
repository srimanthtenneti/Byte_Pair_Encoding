# Byte_Pair_Encoding
This is a tokenization scheme typically used in modern day LLMs. The following implementation builds this scheme from scratch using basic python libraries. 

### Approach 1

This encoding style is very simple. We pick each unique character in a text corpus and assign an integer to it. This greatly simplifies the encode and decode process maintaining a very small vocabulary. But, it results in large sequences of numbers and sometimes fails to capture certain key patterns in the data. 

<img width="1121" alt="Simple_Encode" src="https://github.com/srimanthtenneti/Byte_Pair_Encoding/assets/40752683/19998f15-2701-4a29-95a7-6ce986f27990">


### Approach 2 

This encoding style implements the Byte Pair Encoding scheme (BPE) which starts with the same base character vocabulary from the text corpus but builds higher level tokens by aggregating the base tokens based on frequency of token pairs. My implementation uses the following dataset from kaggle and runs bpe for 500 iterations. The aforementioned reduction in sequence length is depicted via the image below. 

<img width="1121" alt="BPE" src="https://github.com/srimanthtenneti/Byte_Pair_Encoding/assets/40752683/875e02d3-2f9c-4f96-bfb0-ab295328ce2a">

#### Note !!! 

I have uploaded a pickled rule deck for the dataset I ran BPE on for reference. 

Kaggle Dataset : https://www.kaggle.com/datasets/thedevastator/nlp-mental-health-conversations
