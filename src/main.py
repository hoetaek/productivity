from todoist import get_tasks_list, create_task_comments
from datetime import datetime


tasks = get_tasks_list()

for task in tasks:
    created_at = datetime.strptime(task["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
    days_difference = (datetime.now() - created_at).days

    if days_difference > 0 and days_difference % 5 == 0:
        print(task["content"])
        print(days_difference)
        create_task_comments(task["id"], f"만들어진지 {days_difference}일 지났습니다.")
