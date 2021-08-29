import os
import typer
import re



app = typer.Typer()

@app.command()
def crud(name: str):
    
    is_exist = os.path.exists(os.path.join(os.getcwd(), f'{name}.py'))
    if is_exist:
        file = open(f'{name}.py', 'a')
        with open(f'{name}.py','r') as file_check:
            countriesStr = file_check.read()
        
        x = re.findall(f'class {name[0].upper()+name[1:]}',countriesStr)
    
        name = name + '_' + str(len(x)+1) if len(x) > 0 else name
        
    else:
        
        os.system(f'touch {name}.py')
        file = open(f'{name}.py', 'w')


    resources = open('resources.py','r')
    name = name[0].upper()+name[1:]
    for each in resources:

        each = each.replace('class name(Resource):',f'class {name}(Resource):')
        each = each.replace('class Singlename(Resource):',f'class Single{name}(Resource):')
        each = each.replace('data = db.session.query(TableName).all()',f'data = db.session.query({name}Table).all()')
        each = each.replace('data = db.session.query(TableName).filter_by(TableName.id=id).first()',f'data = db.session.query({name}Table).filter_by({name}Table.id=id).first()')

        file.write(each)
    file.close()
    print ('success')



if __name__ == "__main__":
    app()