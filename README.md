# Working with Kafka Connect

1. Run `bin/connect-standalone.sh config/connect-standalone.properties config/connect-console-source.properties`
2. Then use this snippet:

```bash
 curl -i -X POST -H "Accept:application/json" \
    -H "Content-Type:application/json" http://localhost:8083/connectors/ \
    -d '{
        "name" : "my_spool_dir",
        "config": {
            "topic":"my-topic",
            "connector.class":"com.github.jcustenborder.kafka.connect.spooldir.SpoolDirLineDelimitedSourceConnector",
            "input.path":"/tmp/input/",
            "error.path":"/tmp/errors/",
            "finished.path":"/tmp/finished/",
            "input.file.pattern":".*"
        }
    }'
```
