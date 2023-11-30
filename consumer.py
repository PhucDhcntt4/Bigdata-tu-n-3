from kafka import KafkaConsumer

consumer = KafkaConsumer("sample", auto_offset_reset='earliest', group_id=None)

print('Starting kafka Consumer')

for message in consumer:
    print(message)
