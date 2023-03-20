import sys
from database import Session
import models

def consume_sql_action(action: str, table: str, data):
    '''Perform specific SQL query based on the action and table provided. Data should be set in context to the action provided.'''
    
    model_class = get_model(table)

    with Session() as db:
        
        if action == 'create':
            model = model_class(**data)
            db.add(model)

        elif action == 'update':
            # get the id column name from concatinating (without the 's'), the table name with '_id'
            id_name = table[0:-1] + "_id"
            (db
                .query(model_class)
                .filter(getattr(model_class, id_name) == data[id_name])
                .update(data[table[0:-1]])
            )

        elif action == 'delete':
            # get the id column name from concatinating (without the 's'), the table name with '_id'
            id_name = table[0:-1] + '_id'
            (db
                .query(model_class)
                .filter(getattr(model_class, id_name) == data)
                .delete()
            )

        else:
            print('Invalid action provided: ' + action)
            raise Exception('Invalid action provided: ' + table)
        
        db.commit()
        print('Model ' + action + 'd!')

def get_model(table: str):
    '''Returns a SQLAlchemy model class based off the provided table.'''
    
    if table == 'playlists':
        return models.Playlist
    elif table == 'songs':
        return models.Song
    elif table == 'connections':
        return models.Connection
    else:
        print('Invalid table provided: ' + table)
        raise Exception('Invalid table provided: ' + table)