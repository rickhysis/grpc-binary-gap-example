from concurrent import futures
import time

import grpc
import binary_gap_pb2
import binary_gap_pb2_grpc

_TIME = 60 * 60 * 24

class BinaryGapServicer (binary_gap_pb2_grpc.BinaryGapServiceServicer):
    def BinaryGap(self, request, context):
        response = binary_gap_pb2.BinaryGapResponse()
        binary = bin(request.number)
        finalMax = 0
        currentMax = 0

        for i in range(len(binary)) :
            currentMax = 0
            while binary[i] == '0': 
                currentMax += 1 
                i += 1
            finalMax = max(finalMax, currentMax)
        
        response.message = finalMax
        return response

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    binary_gap_pb2_grpc.add_BinaryGapServiceServicer_to_server(
    BinaryGapServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_TIME)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    main()