from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from user import User as db
from status_codes import STATUS_CODES


# Database URL
DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"

# Create an engine
engine = create_engine(DATABASE_URL)

# Create the database tables
db.metadata.create_all(bind=engine)

# Create a new session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

def insert_entry(ip: str, JSON: str) -> int:

    try:
        new_entry = db(ip=ip, JSON=JSON)
        session.add(new_entry)
        # session.query(db).delete()
        session.commit()

    except Exception:
        return STATUS_CODES.ERROR

    return STATUS_CODES.OK

def update_JSON(ip: str, JSON: dict) -> int: # do update field (not JSON specificly)
    try:
        result = session.query(db).filter(db.ip==ip).first()
        result.JSON = JSON

        session.commit()
    except Exception:
        return STATUS_CODES.ERROR

    return STATUS_CODES.OK


def query_table() -> tuple[int, str]:
    output = ''
    try: 
        result = session.query(db)
        for r in result:
            output+=f'|id: {r.id:^10}| ip: {r.ip:^10}| JSON: {r.JSON:^10}| \n'
    except Exception as ex:
        print(ex)
        return STATUS_CODES.ERROR, output

    return STATUS_CODES.OK, output

def query_JSON(ip: str) -> tuple[int, str]: # do query specific field
    output = ''
    try: 
        result = session.query(db).filter(db.ip==ip).first()
        
        output+=f'|id: {result.id:^5}| ip: {result.ip:^10}| JSON: {result.JSON:^10}| \n'
    except Exception:
        return STATUS_CODES.ERROR, output

    return STATUS_CODES.OK, output

    
if __name__ == '__main__':
    insert_entry(ip='0.0.0.0', JSON='{}')
    # update_JSON(ip='0.0.0.0', JSON='{1:!}')
    print(query_table())