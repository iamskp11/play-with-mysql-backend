from abc import abstractmethod
from mysql.connector import MySQLConnection, Error


class Executor:

    @abstractmethod
    def execute(self, query: str) -> list:
        raise NotImplementedError("Please Implement this before invocation")


class MySQLExecutor(Executor):

    def execute(self, query: str) -> list:
        # {time_taken : 0.7287s , count_of_rows: 5, data: [[]]}
        connection = MySQLConnection(
            database='notes_app',
            user='root',
            password='root_1234',
            host='localhost'
        )
        cursor = connection.cursor()
        cursor.execute(query)

        result = []
        rows = cursor.fetchall()
        for row in rows:
            result.append(row)

        return result
