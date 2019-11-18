from data.dbserver.data_manager import data_manager

class Data(object):
    Base = data_manager()

    @staticmethod
    def create(table, colums):
        return Data.Base.create(table, colums)

    @staticmethod
    def insert(table, params, is_commit=True):
        return Data.Base.insert(table, params, is_commit)

    @staticmethod
    def find(table, conditions, fields='*', order=None):
        return Data.Base.find(table, conditions, fields, order)

    @staticmethod
    def select(table, conditions, fields='*', order=None):
        return Data.Base.select(table, conditions, fields, order)

    @staticmethod
    def update(table, conditions, params, is_commit=True):
        return Data.Base.update(table, conditions, params, is_commit)

    @staticmethod
    def delete(table, conditions, is_commit=True):
        return  Data.Base.delete(table, conditions, is_commit)

    @staticmethod
    def find_last(table, conditions, info, limit):
        return Data.Base.find_last(table, conditions, info, limit)

    @staticmethod
    def query(sql):
        return Data.Base.query(sql)




