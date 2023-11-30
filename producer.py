from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers = "localhost:9092" )


producer.send("sample", b"Hello, CSYE72445!")
producer.send("sample", key=b"message-two", value=b"kafka in use!")
producer.flush()
