import pymysql
from django.db.backends.base.base import BaseDatabaseWrapper
from django.db.backends.mysql.features import DatabaseFeatures

# 1. تفعيل PyMySQL كبديل لـ MySQLdb
pymysql.install_as_MySQLdb()

# 2. تعطيل فحص إصدار MariaDB لتجاوز شرط (10.5+)
BaseDatabaseWrapper.check_database_version_supported = lambda self: None

# 3. تعطيل خاصية RETURNING غير المدعومة في MariaDB 10.4
DatabaseFeatures.can_return_columns_from_insert = False