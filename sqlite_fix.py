import sys
import sqlite3
import platform

# Remplacer sqlite3 par pysqlite3 si nécessaire
if sqlite3.sqlite_version_info < (3, 35, 0):
    try:
        import pysqlite3
        sys.modules['sqlite3'] = pysqlite3
    except ImportError:
        pass