from query.execute import MySQLExecutor


class QueryHandler:

    language_instances = {
        'mysql': MySQLExecutor
    }

    def get_instance(self, query_language):
        if query_language not in self.language_instances:
            raise NotImplementedError(f"{query_language} not implemented")
        return self.language_instances.get(query_language)()
