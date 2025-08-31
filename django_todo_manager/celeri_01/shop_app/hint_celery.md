celery --app celeri_01.shop_app.celery_app worker --pool threads --loglevel=INFO  (start)

celery --app celeri_01.shop_app.celery_app flower   (start flower)


celery --app django_todo_manager worker --pool threads --loglevel=INFO  (start)
