# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# DO NOT EDIT. THIS FILE WAS AUTOGENERATED FROM INSTRUMENTATION PACKAGES.
# RUN `python scripts/generate_instrumentation_bootstrap.py` TO REGENERATE.

libraries = [
    {
        "library": "aio_pika >= 7.2.0, < 10.0.0",
        "instrumentation": "opentelemetry-instrumentation-aio-pika==0.49b0",
    },
    {
        "library": "aiohttp ~= 3.0",
        "instrumentation": "opentelemetry-instrumentation-aiohttp-client==0.49b0",
    },
    {
        "library": "aiohttp ~= 3.0",
        "instrumentation": "opentelemetry-instrumentation-aiohttp-server==0.49b0",
    },
    {
        "library": "aiokafka >= 0.8, < 1.0",
        "instrumentation": "opentelemetry-instrumentation-aiokafka==0.49b0",
    },
    {
        "library": "aiopg >= 0.13.0, < 2.0.0",
        "instrumentation": "opentelemetry-instrumentation-aiopg==0.49b0",
    },
    {
        "library": "asgiref ~= 3.0",
        "instrumentation": "opentelemetry-instrumentation-asgi==0.49b0",
    },
    {
        "library": "asyncpg >= 0.12.0",
        "instrumentation": "opentelemetry-instrumentation-asyncpg==0.49b0",
    },
    {
        "library": "boto~=2.0",
        "instrumentation": "opentelemetry-instrumentation-boto==0.49b0",
    },
    {
        "library": "boto3 ~= 1.0",
        "instrumentation": "opentelemetry-instrumentation-boto3sqs==0.49b0",
    },
    {
        "library": "botocore ~= 1.0",
        "instrumentation": "opentelemetry-instrumentation-botocore==0.49b0",
    },
    {
        "library": "cassandra-driver ~= 3.25",
        "instrumentation": "opentelemetry-instrumentation-cassandra==0.49b0",
    },
    {
        "library": "scylla-driver ~= 3.25",
        "instrumentation": "opentelemetry-instrumentation-cassandra==0.49b0",
    },
    {
        "library": "celery >= 4.0, < 6.0",
        "instrumentation": "opentelemetry-instrumentation-celery==0.49b0",
    },
    {
        "library": "confluent-kafka >= 1.8.2, <= 2.4.0",
        "instrumentation": "opentelemetry-instrumentation-confluent-kafka==0.49b0",
    },
    {
        "library": "django >= 1.10",
        "instrumentation": "opentelemetry-instrumentation-django==0.49b0",
    },
    {
        "library": "elasticsearch >= 6.0",
        "instrumentation": "opentelemetry-instrumentation-elasticsearch==0.49b0",
    },
    {
        "library": "falcon >= 1.4.1, < 3.1.2",
        "instrumentation": "opentelemetry-instrumentation-falcon==0.49b0",
    },
    {
        "library": "fastapi ~= 0.58",
        "instrumentation": "opentelemetry-instrumentation-fastapi==0.49b0",
    },
    {
        "library": "flask >= 1.0",
        "instrumentation": "opentelemetry-instrumentation-flask==0.49b0",
    },
    {
        "library": "grpcio >= 1.42.0",
        "instrumentation": "opentelemetry-instrumentation-grpc==0.49b0",
    },
    {
        "library": "httpx >= 0.18.0",
        "instrumentation": "opentelemetry-instrumentation-httpx==0.49b0",
    },
    {
        "library": "jinja2 >= 2.7, < 4.0",
        "instrumentation": "opentelemetry-instrumentation-jinja2==0.49b0",
    },
    {
        "library": "kafka-python >= 2.0, < 3.0",
        "instrumentation": "opentelemetry-instrumentation-kafka-python==0.49b0",
    },
    {
        "library": "kafka-python-ng >= 2.0, < 3.0",
        "instrumentation": "opentelemetry-instrumentation-kafka-python==0.49b0",
    },
    {
        "library": "mysql-connector-python >= 8.0, < 10.0",
        "instrumentation": "opentelemetry-instrumentation-mysql==0.49b0",
    },
    {
        "library": "mysqlclient < 3",
        "instrumentation": "opentelemetry-instrumentation-mysqlclient==0.49b0",
    },
    {
        "library": "pika >= 0.12.0",
        "instrumentation": "opentelemetry-instrumentation-pika==0.49b0",
    },
    {
        "library": "psycopg >= 3.1.0",
        "instrumentation": "opentelemetry-instrumentation-psycopg==0.49b0",
    },
    {
        "library": "psycopg2 >= 2.7.3.1",
        "instrumentation": "opentelemetry-instrumentation-psycopg2==0.49b0",
    },
    {
        "library": "pymemcache >= 1.3.5, < 5",
        "instrumentation": "opentelemetry-instrumentation-pymemcache==0.49b0",
    },
    {
        "library": "pymongo >= 3.1, < 5.0",
        "instrumentation": "opentelemetry-instrumentation-pymongo==0.49b0",
    },
    {
        "library": "PyMySQL < 2",
        "instrumentation": "opentelemetry-instrumentation-pymysql==0.49b0",
    },
    {
        "library": "pyramid >= 1.7",
        "instrumentation": "opentelemetry-instrumentation-pyramid==0.49b0",
    },
    {
        "library": "redis >= 2.6",
        "instrumentation": "opentelemetry-instrumentation-redis==0.49b0",
    },
    {
        "library": "remoulade >= 0.50",
        "instrumentation": "opentelemetry-instrumentation-remoulade==0.49b0",
    },
    {
        "library": "requests ~= 2.0",
        "instrumentation": "opentelemetry-instrumentation-requests==0.49b0",
    },
    {
        "library": "sqlalchemy >= 1.0.0, < 2.1.0",
        "instrumentation": "opentelemetry-instrumentation-sqlalchemy==0.49b0",
    },
    {
        "library": "starlette ~= 0.13.0",
        "instrumentation": "opentelemetry-instrumentation-starlette==0.49b0",
    },
    {
        "library": "psutil >= 5",
        "instrumentation": "opentelemetry-instrumentation-system-metrics==0.49b0",
    },
    {
        "library": "tornado >= 5.1.1",
        "instrumentation": "opentelemetry-instrumentation-tornado==0.49b0",
    },
    {
        "library": "tortoise-orm >= 0.17.0",
        "instrumentation": "opentelemetry-instrumentation-tortoiseorm==0.49b0",
    },
    {
        "library": "pydantic >= 1.10.2",
        "instrumentation": "opentelemetry-instrumentation-tortoiseorm==0.49b0",
    },
    {
        "library": "urllib3 >= 1.0.0, < 3.0.0",
        "instrumentation": "opentelemetry-instrumentation-urllib3==0.49b0",
    },
]
default_instrumentations = [
    "opentelemetry-instrumentation-asyncio==0.49b0",
    "opentelemetry-instrumentation-dbapi==0.49b0",
    "opentelemetry-instrumentation-logging==0.49b0",
    "opentelemetry-instrumentation-sqlite3==0.49b0",
    "opentelemetry-instrumentation-threading==0.49b0",
    "opentelemetry-instrumentation-urllib==0.49b0",
    "opentelemetry-instrumentation-wsgi==0.49b0",
]
