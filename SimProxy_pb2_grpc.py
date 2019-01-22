# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import SimProxy_pb2 as SimProxy__pb2


class SimProxyServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.TriggerEvent = channel.unary_unary(
        '/flightlab.SimProxyService/TriggerEvent',
        request_serializer=SimProxy__pb2.EventDefinition.SerializeToString,
        response_deserializer=SimProxy__pb2.GeneralResponse.FromString,
        )
    self.GetDatum = channel.unary_unary(
        '/flightlab.SimProxyService/GetDatum',
        request_serializer=SimProxy__pb2.DatumDefinitions.SerializeToString,
        response_deserializer=SimProxy__pb2.DatumValues.FromString,
        )
    self.SetDatum = channel.unary_unary(
        '/flightlab.SimProxyService/SetDatum',
        request_serializer=SimProxy__pb2.DatumDefinitionValue.SerializeToString,
        response_deserializer=SimProxy__pb2.GeneralResponse.FromString,
        )
    self.CreateAircraft = channel.unary_unary(
        '/flightlab.SimProxyService/CreateAircraft',
        request_serializer=SimProxy__pb2.CreateAircraftRequest.SerializeToString,
        response_deserializer=SimProxy__pb2.CreateAircraftResponse.FromString,
        )
    self.SlewAircraft = channel.unary_unary(
        '/flightlab.SimProxyService/SlewAircraft',
        request_serializer=SimProxy__pb2.SlewAircraftRequest.SerializeToString,
        response_deserializer=SimProxy__pb2.SlewAircraftResponse.FromString,
        )
    self.RemoveAircraft = channel.unary_unary(
        '/flightlab.SimProxyService/RemoveAircraft',
        request_serializer=SimProxy__pb2.RemoveAircraftRequest.SerializeToString,
        response_deserializer=SimProxy__pb2.RemoveAircraftResponse.FromString,
        )
    self.TrackAircraft = channel.unary_unary(
        '/flightlab.SimProxyService/TrackAircraft',
        request_serializer=SimProxy__pb2.TrackAircraftRequest.SerializeToString,
        response_deserializer=SimProxy__pb2.TrackAircraftResponse.FromString,
        )


class SimProxyServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def TriggerEvent(self, request, context):
    """Trigger a specified event, such as press of a G1000 button.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDatum(self, request, context):
    """Get current value of specified datum.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetDatum(self, request, context):
    """Set value for specified daum.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateAircraft(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SlewAircraft(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RemoveAircraft(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TrackAircraft(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SimProxyServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'TriggerEvent': grpc.unary_unary_rpc_method_handler(
          servicer.TriggerEvent,
          request_deserializer=SimProxy__pb2.EventDefinition.FromString,
          response_serializer=SimProxy__pb2.GeneralResponse.SerializeToString,
      ),
      'GetDatum': grpc.unary_unary_rpc_method_handler(
          servicer.GetDatum,
          request_deserializer=SimProxy__pb2.DatumDefinitions.FromString,
          response_serializer=SimProxy__pb2.DatumValues.SerializeToString,
      ),
      'SetDatum': grpc.unary_unary_rpc_method_handler(
          servicer.SetDatum,
          request_deserializer=SimProxy__pb2.DatumDefinitionValue.FromString,
          response_serializer=SimProxy__pb2.GeneralResponse.SerializeToString,
      ),
      'CreateAircraft': grpc.unary_unary_rpc_method_handler(
          servicer.CreateAircraft,
          request_deserializer=SimProxy__pb2.CreateAircraftRequest.FromString,
          response_serializer=SimProxy__pb2.CreateAircraftResponse.SerializeToString,
      ),
      'SlewAircraft': grpc.unary_unary_rpc_method_handler(
          servicer.SlewAircraft,
          request_deserializer=SimProxy__pb2.SlewAircraftRequest.FromString,
          response_serializer=SimProxy__pb2.SlewAircraftResponse.SerializeToString,
      ),
      'RemoveAircraft': grpc.unary_unary_rpc_method_handler(
          servicer.RemoveAircraft,
          request_deserializer=SimProxy__pb2.RemoveAircraftRequest.FromString,
          response_serializer=SimProxy__pb2.RemoveAircraftResponse.SerializeToString,
      ),
      'TrackAircraft': grpc.unary_unary_rpc_method_handler(
          servicer.TrackAircraft,
          request_deserializer=SimProxy__pb2.TrackAircraftRequest.FromString,
          response_serializer=SimProxy__pb2.TrackAircraftResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'flightlab.SimProxyService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))