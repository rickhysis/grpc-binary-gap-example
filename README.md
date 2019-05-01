# gRPC Binary Gap example - Python

A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 contains a binary gap of length 2. The number 529 has binary representation 10 0001 0001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 1 0100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.

Find the length of binary gap/s for a given number. If the number has more than one binary gap, then output all lengths of binary gaps. If the number has no binary gap, then output 0.

## Input Format:
The first line of input is an integer T indicating the number of input lines. T lines follow. For each line of input contains only an integer N.

## Output Format:
For each line of input, output all lengths of binary gaps. If there is no binary gap, output 0.

## How To Run
```
# First, install the grpcio and grpcio-tools package
pip install grpcio grpcio-tools

# Use the following command to generate the Python code 
python -m grpc_tools.protoc -I=./ --python_out=. --grpc_python_out=. ./binary_gap.proto

# run server
python server.py

# run client
python client.py

```