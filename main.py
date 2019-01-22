import gflags
import grpc
import logging

from RPi import GPIO

from google.apputils import app
from google.protobuf import text_format
from time import sleep

import SimProxy_pb2
import SimProxy_pb2_grpc
import config_pb2

from common import pattern
from hal import encoder
from hal import switch

FLAGS = gflags.FLAGS

gflags.DEFINE_string('uri', None,
                     'Hostname and port of SimConnectServer, such as "192.168.1.1:50051".')
gflags.DEFINE_string('config', None, 'Path to configuration file.')


class App(pattern.Logger):
  def __init__(self, sim_proxy_uri, config_path, *args, **kwargs):
    super(App, self).__init__(*args, **kwargs)
    if sim_proxy_uri:
      channel = grpc.insecure_channel(sim_proxy_uri)
      self._sim_proxy = SimProxy_pb2_grpc.SimProxyServiceStub(channel)
    else:
      self._sim_proxy = None

    self._controls = list(self._init_controls(config_path))

  def _init_controls(self, config_path):
    config_proto = config_pb2.Config()
    with open(config_path, 'r') as f:
      text_format.Merge(f.read(), config_proto)

    for control_proto in config_proto.controls:
      if control_proto.HasField('tactile_switch'):
        proto = control_proto.tactile_switch
        self.logger.info('Initialize tactile switch {0}...'.format(proto.name))
        control = switch.TactileSwitch(name=proto.name, pin=proto.pin)
        control.on('push', self._create_trigger(proto.push_event_id))
        yield control
      elif control_proto.HasField('rotary_encoder'):
        proto = control_proto.rotary_encoder
        print proto
        self.logger.info('Initialize rotary encoder {0}...'.format(proto.name))
        control = encoder.RotaryEncoder(
            name=proto.name,
            clk_pin=proto.clk_pin,
            dt_pin=proto.dt_pin,
            sw_pin=proto.sw_pin)
        control.on('clockwise', self._create_trigger(proto.increase_event_id))
        control.on('counterclockwise',
                   self._create_trigger(proto.decrease_event_id))
        control.on('push', self._create_trigger(proto.push_event_id))
        yield control
      elif control_proto.HasField('dual_rotary_encoder'):
        proto = control_proto.dual_rotary_encoder
        self.logger.info('Initialize dual rotary encoder {0}...'.format(proto.name))
        control = encoder.DualRotaryEncoder(
            name=proto.name,
            large_clk_pin=proto.large_clk_pin,
            large_dt_pin=proto.large_dt_pin,
            small_clk_pin=proto.small_clk_pin,
            small_dt_pin=proto.small_dt_pin,
            sw_pin=proto.sw_pin)
        control.on('large_clockwise',
                   self._create_trigger(proto.large_increase_event_id))
        control.on('large_counterclockwise',
                   self._create_trigger(proto.large_decrease_event_id))
        control.on('small_clockwise',
                   self._create_trigger(proto.small_increase_event_id))
        control.on('small_counterclockwise',
                   self._create_trigger(proto.small_decrease_event_id))
        control.on('push', self._create_trigger(proto.push_event_id))
        yield control

  def _create_trigger(self, event_id):
    def _trigger():
      if self._sim_proxy:
        self.logger.info('Triggering event {0:02X}...'.format(event_id))
        try:
          self._sim_proxy.TriggerEvent(SimProxy_pb2.EventDefinition(id=event_id))
        except:
          self.logger.error('Failed to send event.')
    return _trigger

  def run(self):
    self.logger.info('Running...')
    try:
      while True:
        sleep(1)
    finally:
      GPIO.cleanup()


def main(argv):
  logging.basicConfig(level=logging.DEBUG)
  App(sim_proxy_uri=FLAGS.uri, config_path=FLAGS.config).run()


if __name__ == '__main__':
  app.run()
