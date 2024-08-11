from vidstream import StreamingServer

client = StreamingServer('127.0.0.1', 9999)

client.start_stream()
