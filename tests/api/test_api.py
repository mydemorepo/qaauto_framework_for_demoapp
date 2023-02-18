import pytest
import csv


@pytest.mark.test    
def test_exist_tables (database, client):
    
    response = client.get_content('/api/json')
    tables_list = database.get_tables()
    
    for resp_table, db_table in zip(response['tables'], tables_list):
        for resp_table_name, db_table_name in zip(resp_table, db_table):   
            assert resp_table[resp_table_name] == db_table[db_table_name]
        
@pytest.mark.test    
def test_check_tables_content (database, client):
    tables_list = client.get_content('/api/json')
    
    for table in tables_list['tables']:
        for table_name in table:
           
            name = table[table_name]
            response = client.get_content(f'/api/json/{name}')
            resp_table_content = response[f'{name}']
            query_string = None
            
            for cookie in client.get_cookies():
                query_string = cookie.value
            
            db_table_content = database.get_result(query_string[1:-1])
            
            for resp_row, db_row in zip(resp_table_content, db_table_content):
                for resp_cell, db_cell in zip(resp_row, db_row):
                    assert str(resp_row[resp_cell]) == str(db_row[db_cell])
               
@pytest.mark.test                    
def test_check_column_selection (database, client):        
    name = 'offices'
    request_data = {'city': 'on', 'country': 'on'}
    
    response = client.post_content(f'/api/json/{name}', request_data)
    resp_table_content = response[f'{name}']
    query_string = None
            
    for cookie in client.get_cookies():
        query_string = cookie.value
                
    db_table_content = database.get_result(query_string[1:-1].replace('\\054', ','))
            
    for resp_row, db_row in zip(resp_table_content, db_table_content):
        for resp_cell, db_cell in zip(resp_row, db_row):
            assert str(resp_row[resp_cell]) == str(db_row[db_cell])

@pytest.mark.test                    
def test_download_csv_file (database, client):
    name = 'offices'
    request_data = {'city': 'on', 'country': 'on'}
    
    response = client.post_content(f'/api/json/{name}', request_data)   
    #response = client.get_content(f'/api/json/{name}')
    
    cookies  = client.get_cookies()
    
    csv_file = client.get_file(f'/download/{name}',  cookies)
    
    frecord = open(client.get_headers()['Content-Disposition'][21:], 'wt', newline='')
    frecord.write(csv_file.text)
    frecord.close()
    
    with open(client.get_headers()['Content-Disposition'][21:], 'rt') as freading:
        creading = csv.DictReader(freading)
        
        query_string = None
        for cookie in cookies:
            query_string = cookie.value
                
        db_table_content = database.get_result(query_string[1:-1].replace('\\054', ','))
        
        for file_row, db_row in zip(creading, db_table_content):
            for file_row_cell, db_row_cell in zip(file_row, db_row):
                assert file_row[file_row_cell] == db_row[db_row_cell] 
