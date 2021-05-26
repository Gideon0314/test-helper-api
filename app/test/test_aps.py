# -*- coding: UTF-8 -*-
"""
添加data类型定时任务
{
	"task_id": "2",
	"run_time": "2020-8-12 12:03:00",
	"trigger_type": "date"
}
添加interval类型定时任务
{
	"task_id": "5",
	"interval_time": 10,
	"trigger_type": "interval"
}
添加cron类型定时任务
{
	"task_id": "5",
	"run_time": {
		"day_of_week": "2",
		"hour": "16",
		"minute": "19",
		"second": "00"
	},
	"trigger_type": "cron"
}
"""

data = {
    "task_id": "2",
    "task_name": "定时任务名称",
    "remark": "定时任务描述",

}
