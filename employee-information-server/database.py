import pymysql
import config


def executeSQL(sql):
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


def disconnect_mysql():
    print("Disconnect database...")
    db.close()


def createTables():
    executeSQL("CREATE TABLE IF NOT EXISTS employee("
               "`id` INT(11), "
               "`first_name` VARCHAR(36), "
               "`last_name` VARCHAR(36), "
               "`age` INT(3), "
               "`gender` VARCHAR(64), "
               "`salary` INT(11), "
               "`note` TEXT, "
               "`job` VARCHAR(128), "
               "`joined_at` VARCHAR(256), "
               "`state` INT(1)"
               ");")
    executeSQL("CREATE TABLE IF NOT EXISTS users(`name` VARCHAR(36), `rank` INT(2));")
    executeSQL("CREATE TABLE IF NOT EXISTS log(`type` VARCHAR(128), `note` TEXT, `date` VARCHAR(256));")


db = pymysql.connect(
    host=config.mysql["host"],
    user=config.mysql["user"],
    password=config.mysql["password"],
    database=config.mysql["database"],
    port=3306
)
cursor = db.cursor()
createTables()
