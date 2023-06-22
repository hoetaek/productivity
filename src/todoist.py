import json
import uuid

import requests

from constants import token


def get_all_projects():
    result = requests.get(
        "https://api.todoist.com/rest/v2/projects",
        headers={"Authorization": "Bearer " + token},
    ).json()
    return result


def get_project_tasks(project_id):
    result = requests.get(
        "https://api.todoist.com/rest/v2/tasks",
        params={"project_id": project_id},
        headers={"Authorization": "Bearer " + token},
    ).json()
    return result


def get_tasks_list():
    result = requests.get(
        "https://api.todoist.com/rest/v2/tasks",
        params={
            "filter": "no date & !#inbox  & !#관리함 & !#obsidian & !#routine & !#pending"
        },
        headers={"Authorization": "Bearer " + token},
    ).json()
    return result


def get_task(task_id):
    result = requests.get(
        f"https://api.todoist.com/rest/v2/tasks/{task_id}",
        headers={"Authorization": "Bearer " + token},
    ).json()
    return result


def update_task(task_id, update_data: dict):
    requests.post(
        "https://api.todoist.com/rest/v2/tasks/" + str(task_id),
        data=json.dumps(update_data),
        headers={
            "Content-Type": "application/json",
            "X-Request-Id": str(uuid.uuid4()),
            "Authorization": "Bearer " + token,
        },
    )


def delete_task(task_id):
    requests.delete(
        f"https://api.todoist.com/rest/v2/tasks/{task_id}",
        headers={"Authorization": "Bearer " + token},
    )


def close_task(task_id):
    requests.post(
        f"https://api.todoist.com/rest/v2/tasks/{task_id}/close",
        headers={"Authorization": "Bearer " + token},
    )


def reopen_task(task_id):
    requests.post(
        f"https://api.todoist.com/rest/v2/tasks/{task_id}/reopen",
        headers={"Authorization": "Bearer " + token},
    )


def get_task_comments(task_id):
    requests.post(
        f"https://api.todoist.com/rest/v2/comments/",
        params={"task_id": task_id},
        headers={"Authorization": "Bearer " + token},
    )


def create_task_comments(task_id, content):
    data = {"task_id": task_id, "content": content}
    res = requests.post(
        f"https://api.todoist.com/rest/v2/comments/",
        data=json.dumps(data),
        headers={
            "Content-Type": "application/json",
            "X-Request-Id": str(uuid.uuid4()),
            "Authorization": "Bearer " + token,
        },
    )
    print(res)


def get_labels():
    labels = requests.get(
        "https://api.todoist.com/rest/v2/labels",
        headers={"Authorization": "Bearer " + token},
    ).json()
    return labels


def create_label(label_name, color_id):
    result = requests.post(
        "https://api.todoist.com/rest/v2/labels",
        data=json.dumps({"name": label_name, "color": color_id}),
        headers={
            "Content-Type": "application/json",
            "X-Request-Id": str(uuid.uuid4()),
            "Authorization": "Bearer " + token,
        },
    ).json()
    return result


def delete_label(label_id):
    requests.delete(
        f"https://api.todoist.com/rest/v2/labels/{label_id}",
        headers={"Authorization": "Bearer " + token},
    )


# def create_date_next_action_task(page_id, title, label_ids, date, priority):
#     task_data = {
#         "content": title,
#         "project_id": date_next_action_project_id,
#         "description": page_id,
#         "label_ids": label_ids,
#         "priority": 5 - priority,
#     }
#     # if date:
#     #     task_data["due_datetime"] = date
#     if date:
#         if len(date) == 10:
#             task_data["due_date"] = date
#         else:
#             task_data["due_datetime"] = datetime.strptime(
#                 date, "%Y-%m-%dT%H:%M:%S.%f+09:00"
#             ).isoformat()

#     result = requests.post(
#         "https://api.todoist.com/rest/v2/tasks",
#         data=json.dumps(task_data),
#         headers={
#             "Content-Type": "application/json",
#             "X-Request-Id": str(uuid.uuid4()),
#             "Authorization": "Bearer " + token,
#         },
#     ).json()
#     return result


# def update_date_next_action_task(task_id, title, label_ids, date, priority):
#     task_data = {
#         "content": title,
#         "label_ids": label_ids,
#         "priority": 5 - priority,
#     }
#     if not date:
#         task_data["due_string"] = "no date"
#     elif len(date) == 10:
#         task_data["due_date"] = date
#     else:
#         task_data["due_datetime"] = datetime.strptime(
#             date, "%Y-%m-%dT%H:%M:%S.%f+09:00"
#         ).isoformat()

#     requests.post(
#         "https://api.todoist.com/rest/v2/tasks/" + str(task_id),
#         data=json.dumps(task_data),
#         headers={
#             "Content-Type": "application/json",
#             "X-Request-Id": str(uuid.uuid4()),
#             "Authorization": "Bearer " + token,
#         },
#     )
