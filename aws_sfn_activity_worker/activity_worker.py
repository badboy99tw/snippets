import asyncio
import json
import os

import boto3


class ActivityWorker:
    HEARTBEAT_INTERVAL = 2

    def __init__(self, activity_arn, worker_name):
        self.activity_arn = activity_arn
        self.worker_name = worker_name
        self.client = boto3.client("stepfunctions")

    def get_task(self):
        self.task = self.client.get_activity_task(
            activityArn=self.activity_arn, workerName=self.worker_name
        )
        self.task_token = self.task["taskToken"]

    async def heartbeat(self, heartbeat_interval):
        while True:
            self.client.send_task_heartbeat(taskToken=self.task_token)
            await asyncio.sleep(heartbeat_interval)

    async def start(self):
        self.get_task()

        asyncio.create_task(self.heartbeat(self.HEARTBEAT_INTERVAL))

        output = await self.run()

        self.client.send_task_success(
            taskToken=self.task_token,
            output=json.dumps({"output": output}),
        )

    async def run(self):
        print("Start processing")
        await asyncio.sleep(10)
        print("Stop processing")
        return "result"


if __name__ == "__main__":
    activity_arn = (
        f"arn:aws:states:{os.environ['AWS_REGION']}:{os.environ['AWS_ACCOUNT']}:activity:MyActivity",
    )
    worker_name = "worker_name"

    worker = ActivityWorker(activity_arn, worker_name)
    asyncio.run(worker.start())
