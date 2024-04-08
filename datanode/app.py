import argparse
import variables
import grpc
from concurrent import futures
from src.crons.cron import run_cron
import threading
from src.services.file_service import FileService
import config_pb2_grpc

def server(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    config_pb2_grpc.add_FileServiceServicer_to_server(FileService(), server)
    server.add_insecure_port(f'localhost:{port}')
    server.start()
    print(f"GRPC RUNNING on localhost:{port}")
    server.wait_for_termination()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Servidor gRPC")
    parser.add_argument("--port", type=int, default=variables.port_grpc, help="Puerto a utilizar")
    args = parser.parse_args()

    print(f"datanode run on {args.port}")
    server(args.port)

    cron_thread = threading.Thread(target=run_cron)
    cron_thread.start()
