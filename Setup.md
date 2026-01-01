
docker-compose down -v
docker-compose up -d

# ✅ Verify installation
docker exec kafka ls /usr/bin | findstr kafka

# ✅ Create a topic (note: NO .sh)
docker exec kafka kafka-topics --create --topic test --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1

# ✅ List topics
docker exec kafka kafka-topics --list --bootstrap-server localhost:9092

# ✅ Produce a message
docker exec -it kafka kafka-console-producer --topic test --bootstrap-server localhost:9092

<Then type your message, and exit>

# ✅ Consume messages
docker exec kafka kafka-console-consumer --topic test --from-beginning --bootstrap-server localhost:9092 --timeout-ms 5000