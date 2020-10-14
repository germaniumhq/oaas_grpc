import abc
from typing import TypeVar, Any, Dict

T = TypeVar('T')


class ProxyInstanceHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def initial_instance(self): ...

    @abc.abstractmethod
    def call_error(self, oaas_grpc_proxy, oaas_grpc_exception, *args, **kw): ...

    @abc.abstractmethod
    def call_success(self): ...


class GrpcCallProxyMethod:
    """
    Proxies method calls to the actual gRPC implementation of the
    method. Notifies the instance handler on the status of the
    last operation.
    """
    def __init__(self,
                 *,
                 oaas_grpc_proxy: 'GrpcCallProxy',
                 instance_handler: ProxyInstanceHandler,
                 method_name: str,
                 delegate_method) -> None:
        self._method_name = method_name
        self._proxy = oaas_grpc_proxy
        self._method = delegate_method
        self._instance_handler = instance_handler

    def __call__(self, *args, **kw) -> Any:
        try:
            result = self._method(*args, **kw)
            self._instance_handler.call_success()
            return result
        except Exception as e:
            proxy = self._instance_handler.call_error(
                self._proxy,
                e,
                *args,
                **kw
            )
            return getattr(proxy, self._method_name)(*args, **kw)


class GrpcCallProxy():
    def __init__(self,
                 *,
                 instance_handler: ProxyInstanceHandler) -> None:
        #self._grpc_type = grpc_type
        #self._grpc_channel = channel

        #self._delegate = self._grpc_type(channel=channel)  # type: ignore
        self.__delegate = instance_handler.initial_instance()
        self._instance_handler = instance_handler
        self._proxy_methods: Dict[str, GrpcCallProxyMethod] = dict()

    @property
    def _delegate(self):
        return self.__delegate

    @_delegate.setter
    def _delegate(self, value) -> None:
        self._proxy_methods.clear()
        self.__delegate = value

    def __getattr__(self, name: str):
        result = self._proxy_methods.get(name, None)

        if result:
            return result

        result = GrpcCallProxyMethod(
            oaas_grpc_proxy=self,
            method_name=name,
            instance_handler=self._instance_handler,
            delegate_method=getattr(self._delegate, name),
        )

        self._proxy_methods[name] = result

        return result
