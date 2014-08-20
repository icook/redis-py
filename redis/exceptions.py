"Core exceptions raised by the Redis client"
from redis._compat import unicode


class RedisError(Exception):
    pass


# python 2.5 doesn't implement Exception.__unicode__. Add it here to all
# our exception types
if not hasattr(RedisError, '__unicode__'):
    def __unicode__(self):
        if isinstance(self.args[0], unicode):
            return self.args[0]
        return unicode(self.args[0])
    RedisError.__unicode__ = __unicode__


class AuthenticationError(RedisError):
    pass


class ConnectionError(RedisError):
    pass


class TimeoutError(RedisError):
    pass


class BusyLoadingError(ConnectionError):
    "raised when the Redis server is starting up and not accepting commands yet"
    pass


class InvalidResponse(RedisError):
    "Failed to parse Redis RESP protocol response"
    pass


class ResponseError(RedisError):
    """ Wraps RESP type errors. See http://redis.io/topics/protocol. Subclasses
    are specific RESP error types while this wraps generic ERR """
    pass


class DataError(RedisError):
    "Raised when invalid arguments are passed to Redis commands"
    pass


class PubSubError(RedisError):
    pass


class WatchError(RedisError):
    pass


class NoScriptError(ResponseError):
    pass


class ExecAbortError(ResponseError):
    pass


class ReadOnlyError(ResponseError):
    pass


class LockError(RedisError, ValueError):
    "Errors acquiring or releasing a lock"
    # NOTE: For backwards compatability, this class derives from ValueError.
    # This was originally chosen to behave like threading.Lock.
    pass
