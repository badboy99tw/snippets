# AWS Step Functions Activity Worker

## Setup State Machine

* AWS Console -> Step Functions
* 註冊一個 Activity，假設叫做 `MyActivity`
* Create state machine 如下（記得要把 aws_region、aws_account 換掉）：

```
{
  "Comment": "MyJob",
  "StartAt": "MyTask",
  "States": {
    "MyTask": {
      "Type": "Task",
      "Resource": "arn:aws:states:<aws_region>:<aws_account>:activity:MyActivity",
      "InputPath": "$",
      "HeartbeatSecondsPath": "$.heartbeat",
      "ResultPath": "$.result",
      "End": true
    }
  }
}
```

## Run

* Start execution

透過 input 設定 heartbeat，這邊用 5 秒當例子。

```
{
    "heartbeat": 5
}
```

* Start worker

```
export AWS_REGION=<your_aws_region>
export AWS_ACCOUNT=<your_aws_account>
python3 activity_worker.py
```
