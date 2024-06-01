from influxdb import InfluxDBClient

json_body = [
    {
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": "2009-11-10T23:00:00Z",
        "fields": {
            "value": 0.64
        }
    }
]

client = InfluxDBClient('localhost', 8086, database='db2')

client.write_points(json_body)

result_db2 = client.query('select value from cpu_load_short;')
print(f'Data in db2: {result_db2}')

client.switch_database('db1')

result_db1 = client.query('select value from cpu_load_short;')
print(f'Data in db1: {result_db1}')



