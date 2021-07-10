from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient

client = FaunaClient(secret="fnAEJBZC5VACCjyVg5qEQQq1ZJjFbBynys8KF3Xj")

indexes = client.query(q.paginate(q.indexes()))

print(indexes)