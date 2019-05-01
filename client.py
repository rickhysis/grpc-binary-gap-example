from concurrent import futures
import time

import grpc
import binary_gap_pb2
import binary_gap_pb2_grpc


def main():

    # Create channel and stub to server's address and port.
    channel = grpc.insecure_channel('localhost:50051')
    stub = binary_gap_pb2_grpc.BinaryGapServiceStub(channel)

    # Exception handling.
    try:
        response = stub.BinaryGap(binary_gap_pb2.BinaryGapRequest(number=529))
        print(response)

    # Catch any raised errors by grpc.
    except grpc.RpcError as e:
        print("Error raised: " + e.details())


if __name__ == '__main__':
    main()