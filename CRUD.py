import os
import typer
import re



app = typer.Typer()

@app.command()
def crud(name: str):

    #Checking the file is already exists    
    is_exist = os.path.exists(os.path.join(os.getcwd(), f'{name}.py'))
    if is_exist:
        #if its existing

        #opening the file
        file = open(f'{name}.py', 'a')

        #getting all lines
        with open(f'{name}.py','r') as file_check:
            linesStr = file_check.read()
        
        #getting that the given already exsits into a list
        x = re.findall(f'class {name[0].upper()+name[1:]}',linesStr)

        #giving the name a number(like name_1) if its already exists
        name = name + '_' + str(len(x)+1) if len(x) > 0 else name
        
    else:
        
        #if the file not exists create one
        os.system(f'touch {name}.py')
        file = open(f'{name}.py', 'w')

    #opening resources file
    resources = open('resources.py','r')
    #making names first letter CapitalCase
    name = name[0].upper()+name[1:]
    
    #getting each lines from resourse and replace new name
    for each in resources:

        each = each.replace('class name(Resource):',f'class {name}(Resource):')
        each = each.replace('class Singlename(Resource):',f'class Single{name}(Resource):')
        each = each.replace('data = db.session.query(TableName).all()',f'data = db.session.query({name}Table).all()')
        each = each.replace('data = db.session.query(TableName).filter_by(TableName.id=id).first()',f'data = db.session.query({name}Table).filter_by({name}Table.id=id).first()')

        #writing each lines
        file.write(each)
    
    #closing all opened files
    resources.close()
    file.close()
    print ('success')



if __name__ == "__main__":
    app()