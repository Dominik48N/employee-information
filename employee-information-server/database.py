import pymysql
import config


def execute_sql(sql):
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()


def fetch_sql(sql):
    try:
        cursor.execute(sql)
        results = cursor.fetchall()

        return results
    except:

        print("Error: unable to fetch data")


def disconnect_mysql():
    print("Disconnect database...")
    db.close()


def create_tables():
    execute_sql("CREATE TABLE IF NOT EXISTS employee("
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
    execute_sql("CREATE TABLE IF NOT EXISTS users(`name` VARCHAR(36), `rank` INT(2));")
    execute_sql("CREATE TABLE IF NOT EXISTS log(`type` VARCHAR(128), `note` TEXT, `date` VARCHAR(256));")


db = pymysql.connect(
    host=config.mysql["host"],
    user=config.mysql["user"],
    password=config.mysql["password"],
    database=config.mysql["database"],
    port=3306
)
cursor = db.cursor()
create_tables()
