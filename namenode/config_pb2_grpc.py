# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import config_pb2 as config__pb2


class FileServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getFile = channel.unary_unary(
                '/FileService/getFile',
                request_serializer=config__pb2.GetFileRequest.SerializeToString,
                response_deserializer=config__pb2.GetFileResponse.FromString,
                )
        self.saveFile = channel.unary_unary(
                '/FileService/saveFile',
                request_serializer=config__pb2.SaveFileRequest.SerializeToString,
                response_deserializer=config__pb2.SaveFileResponse.FromString,
                )
        self.cloneFile = channel.unary_unary(
                '/FileService/cloneFile',
                request_serializer=config__pb2.CloneFileRequest.SerializeToString,
                response_deserializer=config__pb2.CloneFileResponse.FromString,
                )
        self.ReplicateFile = channel.unary_unary(
                '/FileService/ReplicateFile',
                request_serializer=config__pb2.ReplicateFileRequest.SerializeToString,
                response_deserializer=config__pb2.ReplicateFileResponse.FromString,
                )


class FileServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def saveFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def cloneFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReplicateFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getFile': grpc.unary_unary_rpc_method_handler(
                    servicer.getFile,
                    request_deserializer=config__pb2.GetFileRequest.FromString,
                    response_serializer=config__pb2.GetFileResponse.SerializeToString,
            ),
            'saveFile': grpc.unary_unary_rpc_method_handler(
                    servicer.saveFile,
                    request_deserializer=config__pb2.SaveFileRequest.FromString,
                    response_serializer=config__pb2.SaveFileResponse.SerializeToString,
            ),
            'cloneFile': grpc.unary_unary_rpc_method_handler(
                    servicer.cloneFile,
                    request_deserializer=config__pb2.CloneFileRequest.FromString,
                    response_serializer=config__pb2.CloneFileResponse.SerializeToString,
            ),
            'ReplicateFile': grpc.unary_unary_rpc_method_handler(
                    servicer.ReplicateFile,
                    request_deserializer=config__pb2.ReplicateFileRequest.FromString,
                    response_serializer=config__pb2.ReplicateFileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FileService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FileService/getFile',
            config__pb2.GetFileRequest.SerializeToString,
            config__pb2.GetFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def saveFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FileService/saveFile',
            config__pb2.SaveFileRequest.SerializeToString,
            config__pb2.SaveFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def cloneFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FileService/cloneFile',
            config__pb2.CloneFileRequest.SerializeToString,
            config__pb2.CloneFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReplicateFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FileService/ReplicateFile',
            config__pb2.ReplicateFileRequest.SerializeToString,
            config__pb2.ReplicateFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
