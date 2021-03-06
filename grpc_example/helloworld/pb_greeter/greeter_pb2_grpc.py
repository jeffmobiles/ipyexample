# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from grpc_example.helloworld.pb_greeter import greeter_pb2 as grpc__example_dot_helloworld_dot_pb__greeter_dot_greeter__pb2


class GreeterStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SayHello = channel.unary_unary(
        '/pb_greeter.Greeter/SayHello',
        request_serializer=grpc__example_dot_helloworld_dot_pb__greeter_dot_greeter__pb2.HelloRequest.SerializeToString,
        response_deserializer=grpc__example_dot_helloworld_dot_pb__greeter_dot_greeter__pb2.HelloReply.FromString,
        )


class GreeterServicer(object):
  """The greeting service definition.
  """

  def SayHello(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SayHello': grpc.unary_unary_rpc_method_handler(
          servicer.SayHello,
          request_deserializer=grpc__example_dot_helloworld_dot_pb__greeter_dot_greeter__pb2.HelloRequest.FromString,
          response_serializer=grpc__example_dot_helloworld_dot_pb__greeter_dot_greeter__pb2.HelloReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'pb_greeter.Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
