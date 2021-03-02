from __main__ import app, mysql

def insert_post(title, shor_description, content, id_user=1):
    query = "INSERT INTO post (id_user, title, short_description, content) VALUES (%s, %s, %s, %s)"
    values = (id_user, title, shor_description, content)
    cur = mysql.connection.cursor()
    cur.execute(query, values)
    mysql.connection.commit()

# Method that get all the posts
def get_all_posts():
    query = "SELECT p.id_post, p.title, p.short_description, p.content, p.on_update_dt, u.id_user, u.username " \
            "FROM post p JOIN user u on u.id_user = p.id_user ORDER BY p.on_update_dt DESC"
    print("Estoy buscando los posts")

    cursor = mysql.connection.cursor()
    cursor.execute(query)
    posts = cursor.fetchall()
    cursor.close()

    print(posts)
    return posts


# Method that get a specific post
def get_post(id_post):
    query = "SELECT p.id_post, p.title, p.short_description, p.content, p.on_update_dt, u.id_user, u.username " \
            "FROM post p JOIN user u on u.id_user = p.id_user WHERE p.id_post = %s"
    value = (id_post,)
    print("Estoy buscando un post")

    cursor = mysql.connection.cursor()
    cursor.execute(query, value)
    post = cursor.fetchone()
    cursor.close()

    if post is None:
        abort(404)

    print(post)
    return post
