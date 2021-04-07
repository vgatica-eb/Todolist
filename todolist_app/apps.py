from django.apps import AppConfig
import posthog


class TodolistAppConfig(AppConfig):
    name = 'todolist_app'

    def ready(self):
        posthog.api_key = 'BpG7r7gKmXRAv4t7KzhBdWXJQf0cSGKY4eYs8LGQq24'
        posthog.host = 'https://app.posthog.com'
