from data_base import init_db
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)
app.debug = True

default_query = '''
{
    allStudents{edges{
    node{
    id,
    name,
    student_name{
    id,name
    },
    courses{
    id,
    name
                }
            }
        }
    }
}'''.strip()

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    init_db()
    app.run()
