# Pod
Pod is the smallest unit in the kubernetes system.

## Get pods in a namespace
```bash
kubectl [--namespace <namespace> | -n <namespace>] get pods
```

## Get pod logs
```bash
kubectl logs <pod-name> -n <namespace>
```

## Get container logs running on a pod
```bash
kubectl logs <pod-name> <container-name> -n <namespace>
```

## Continually Streaming Logs
The plain logs command emits the currently stored Pod logs and then exits. Add the `-f` or `--follow` flag to the command to follow the logs and live stream them to your terminal.

Kubectl will emit each new log line into your terminal until you stop the command with Ctrl+C. This is equivalent to using `tail -f` with a local log file in a non-containerized environment.

## Get pod details as formatted JSON
```
kubectl get pods <pod-name> -n <namespace> --output jsonpath='{}' | jq
```
Make sure the tool `jq` is installed in your system.

> **Note**: If you select the `namespace` as your default one, then there is no need of the `-n` option with each command.

# References
- [https://www.howtogeek.com/devops/how-to-view-kubernetes-pod-logs-with-kubectl/](https://www.howtogeek.com/devops/how-to-view-kubernetes-pod-logs-with-kubectl/)
