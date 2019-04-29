from newsletter.models.model import Model

from newsletter.models.drivers.sqlite_driver import SqliteDriver
from newsletter.models.drivers.mysql_driver import MysqlDriver
from newsletter.models.drivers.odbc_driver import OdbcDriver

from newsletter.etc.conf import DevelopConfig

sqlitedb = SqliteDriver()
sqlitedb.set_filedb( DevelopConfig.SQLITEFILE )
sqlitemodel = Model()
sqlitemodel.set_driver( sqlitedb )

mssqldb = OdbcDriver()
mssqldb.set_rdn( DevelopConfig.MSSQLRDN )
mssqldb.set_user( DevelopConfig.MSSQLUSR )
mssqldb.set_passwd( DevelopConfig.MSSQLPWD )

mysqldb = MysqlDriver()