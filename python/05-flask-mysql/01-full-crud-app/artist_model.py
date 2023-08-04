from mysqlconnection import connectToMySQL
class Artist :

    def __init__(self,data_dict):
        self.id  = data_dict['id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.nationality = data_dict['nationality']
        self.rate = data_dict['rate']
        self.image = data_dict['image']
        self.is_dead = data_dict['is_dead']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
    
    # EVERY QUERY MUST BE CLASSMETHOD CURD 

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM artists;"
        results = connectToMySQL("artists_schema").query_db(query)
        all_artists = []
        # print("🔥"*10,results,"🔥"*10)
        for row in results:
            artist = cls(row)
            # artist = Artist(row)
            # artist  =  Artist()
            all_artists.append(artist)
        # print("🎈"*10, all_artists,"🎈"*10)
        return all_artists
    
    @classmethod
    def create_artist(cls,data_dict):
        query = """
                    INSERT INTO artists (first_name, last_name, nationality, rate, image, is_dead)
                    VALUES (%(first_name)s, %(last_name)s, %(nationality)s, %(rate)s, %(image)s, %(is_dead)s);
                """
        result = connectToMySQL("artists_schema").query_db(query, data_dict)
        return result
    
    @classmethod
    def get_one_by_id(cls,data_dict):
        query = " SELECT * FROM artists WHERE id= %(id)s;"
        # query = " SELECT * FROM artists WHERE id= 4;"
        results = connectToMySQL("artists_schema").query_db(query, data_dict)
        # results = connectToMySQL("artists_schema").query_db(query)
        # print("🎈"*20,results, "🎈"*20)
        artist  = cls(results[0])
        return artist
    
    @classmethod
    def update(cls, data_dict):
        query = """
                    UPDATE artists SET first_name  = %(first_name)s, last_name = %(last_name)s,
                    nationality= %(nationality)s,rate= %(rate)s, image=%(image)s, is_dead=%(is_dead)s
                    WHERE id= %(id)s;
                """
        return connectToMySQL("artists_schema").query_db(query, data_dict)

    @classmethod
    def delete(cls, data_dict):
        query = "DELETE FROM artists WHERE id = %(id)s;"
        result  = connectToMySQL("artists_schema").query_db(query, data_dict)
        print(result)
        return None