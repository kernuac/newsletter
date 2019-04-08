from newsletter.models.model import Model
from newsletter.models.drivers.sqlite_driver import SqliteDriver
from newsletter.models.drivers.mysql_driver import MysqlDriver
from newsletter.etc.conf import DevelopConfig

sqlitedb = SqliteDriver()
sqlitedb.set_filedb( DevelopConfig.SQLITEFILE )
sqlitemodel = Model()
sqlitemodel.set_driver( sqlitedb )

print ( DevelopConfig.SQLITEFILE )