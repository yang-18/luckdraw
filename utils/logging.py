# import traceback
# import sys
# import os
# import json
# import logging
# import logging.handlers
# import socket
# import uuid
# from logging import handlers, Logger
# # from measure.models import Logs
# import datetime
# logging.basicConfig(level=logging.DEBUG)


# def error2msg(error):
#     error_msg = traceback.format_exc()
#     if sys.platform == ('win32'):
#         return error_msg.replace("'", '"')
#     else:
#         replace_error_msg = error_msg.replace('"', " ")
#         return replace_error_msg.replace("'", " ")


# """
# 日志级别
# debug 调试的时候用
# info 正常输出，方便观察
# warn 输出报警错误，不影响正常运行
# error 用来打印错误信息，已经影响到了程序的运行

# """


# class JFMLogging(object):
#     log = None
#     level_relations = {
#         "DEBUG": logging.DEBUG,
#         "INFO": logging.INFO,
#         "WARN": logging.WARN,
#         "ERROR": logging.ERROR,
#     }

#     def __init__(self, file_name, level):
#         hostname = socket.gethostname()
#         ip = socket.gethostbyname(hostname)
#         env = None
#         id = uuid.uuid1()

#         '''
#         type 日志类型{0:system,1:business};
#         version 日志版本;
#         environment     环境;
#         level       日志级别    debug/info/warn/error/trace;
#         id      唯一标识;
#         message    日志内容;
#         message_parameters    日志参数;
#         project_name     项目名称;
#         poject_version    项目版本;
#         class_name   项目类;
#         file_name    文件名;
#         file_number    文件行;
#         record_ip    主机ip;
#         record_thread_thread_id    进程编号;
#         request_id    发送机器;
#         user_id    用户编号;
#         user_name    用户名;
#         request_url    请求方式;
#         request_query   请求条件;
#         date    时间    YYYYMMDDhhmmss
#         '''
#         format = json.dumps({"type": "0",
#                              "version": '1',
#                              "environment": str(env),
#                              "date": "%(asctime)s",
#                              "level": str(level),
#                              "id": str(id),
#                              "record_hostname": str(hostname),
#                              "record_ip": str(ip),
#                              "file_name": "%(module)s.py",
#                              "project_version": "1.0",
#                              "message": "%(message)s"
#                              })
#         datefmt = "YYYYMMDDhhmmss"
#         logging.basicConfig(level=logging.DEBUG, format=format,
#                             datefmt=datefmt, filemode="a")
#         if sys.platform == "win32":
#             log_dir = os.path.join(os.getcwd(), "logs")
#             filename = os.path.join(log_dir, file_name + ".log")
#         elif sys.platform == 'linux':
#             log_dir = os.path.join(os.path.abspath(
#                 os.path.dirname(os.getcwd())), "logs")
#             # filename = os.path.join(log_dir, file_name + ".log")
#             filename = os.path.join(log_dir, file_name + ".log")
#         if not os.path.exists(log_dir):
#             os.makedirs(log_dir)

#         self.logger = logging.getLogger(filename)
#         formatter = logging.Formatter(format)
#         self.logger.setLevel(self.level_relations.get(level))
#         th = handlers.TimedRotatingFileHandler(
#             filename=filename, backupCount=3, encoding="utf-8")
#         th.setFormatter(formatter)
#         self.logger.addHandler(th)

#         def getLogger(self):
#             return self.logger


# class Logger(object):
#     logger = None

#     @staticmethod
#     def get_logger():
#         if Logger.logger is None:
#             Logger.logger = JFMLogging(file_name='all', level="DEBUG").logger
#         return Logger.logger

#     @staticmethod
#     def debug(content):
#         return Logger.get_logger().critical(content)

#     @staticmethod
#     def info(content):
#         return Logger.get_logger().critical(content)

#     @staticmethod
#     def warn(content):
#         return Logger.get_logger().critical(content)

#     @staticmethod
#     def error(content):
#         return Logger.get_logger().critical(content)


# def write_database_logs(request_id, api_name, initial_time, message, end_time=None):
#     log = Logs()
#     log.request_id = request_id
#     log.api_name = api_name
#     log.initial_time = initial_time
#     log.write_time = datetime.datetime.now()
#     log.message = message
#     log.end_time = end_time
#     log.save()
