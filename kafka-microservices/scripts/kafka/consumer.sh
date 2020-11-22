#!/bin/bash

docker exec -it kafka-broker kafka-console-consumer.sh --topic quickstart-events --from-beginning