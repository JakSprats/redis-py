import redis

### This test demonstrates that the commands get correctly passed to the server

r = redis.Redis(host='localhost', port=6379, db=0)
x = r.exists("python")
if x:
    print r.dropTable("python")
print r.createTable("python", "id INT, val INT, more INT")
print r.createIndex("ind_python_val", "python", "val");
print r.desc("python")
print r.insert("python", "1,11,111")
print r.insert("python", "2,22,222")
print r.insert("python", "3,33,333")
print r.insert_ret_size("python", "4,44,444")
print r.dumpToMysql("python", "")
print r.dumpToFile("python", "/tmp/python.sql")
print r.sqlSelect("*", "python", "id = 3")
print r.sqlSelect("*", "python", "id BETWEEN 1 AND 2")
print r.scanSelect("*", "python", "more BETWEEN 200 AND 300")
print r.update("python", "more=999", "id = 3")
print r.scanSelect("*", "python", "")
print r.delete("python", "id = 2")
print r.lua("return client('SCANSELECT','*', 'FROM', 'python');")

