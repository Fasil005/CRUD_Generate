# CRUD_Generate

This is a python file to create a new file with Flask_restful CRUD operations.


## Installation of Requirments

```bash
pip install -r requirements.txt
```

### Running the app

```bash
python CRUD.py {name}
```

### This is the CRUD Code. This will recreate into your file.

```python
class name(Resource):


    def post(self):

        try:

            pass

        except Exception as e:
            print(e)



    def get(self):

        try:

            data = db.session.query(TableName).all()

            return make_response(jsonify(data=data,msg='success'),200)
            
        except Exception as e:
            print(e)




class Singlename(Resource):


    def get(self,id):

        try:

            data = db.session.query(TableName).filter_by(TableName.id=id).first()

            return make_response(jsonify(data=dict(data),msg='success'),200)

        except Exception as e:
            print(e)


    def put(self,id):
        try:

            pass

        except Exception as e:
            print(e)


    def delete(self,id):
        try:

            data = db.session.query(TableName).filter_by(TableName.id=id).first()

            db.session.delete(data)
            db.session.commit()

            return make_response(jsonify(msg='success'),200)
            
        except Exception as e:
            print(e)

```
