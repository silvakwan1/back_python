from app.database import conn, cursor

def promocoes(dateStart, dateEnd, title, image, link, cupom, description, categoria, latitude, longitude):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Promocoes (
        id INT AUTO_INCREMENT PRIMARY KEY, -- ID único para cada promoção
        dateStart DATE NOT NULL, -- Data de início
        dateEnd DATE NOT NULL, -- Data de fim
        title VARCHAR(255) NOT NULL, -- Título
        image VARCHAR(500) NOT NULL, -- URL da imagem
        link VARCHAR(500) DEFAULT '', -- Link
        cupom VARCHAR(255) DEFAULT '', -- Cupom
        description TEXT NOT NULL, -- Descrição
        categoria VARCHAR(255) NOT NULL, -- Categoria
        latitude DECIMAL(10, 8) NOT NULL, -- Latitude
        longitude DECIMAL(11, 8) NOT NULL, -- Longitude
        createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Data de criação
    )
    """)
    
    sql = """
    INSERT INTO Promocoes (dateStart, dateEnd, title, image, link, cupom, description, categoria, latitude, longitude) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (dateStart, dateEnd, title, image, link, cupom, description, categoria, latitude, longitude)

    cursor.execute(sql, values)
    conn.commit()
    print(f"{cursor.rowcount} registro(s) inserido(s).")

    return cursor.lastrowid


def vip_user(nome, whatsApp, email):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS VipUsers (
        id INT AUTO_INCREMENT PRIMARY KEY, -- ID único para cada usuário
        nome VARCHAR(255) NOT NULL, -- Nome do usuário
        whatsApp VARCHAR(20) NOT NULL, -- WhatsApp do usuário
        email VARCHAR(255) NOT NULL -- Email do usuário
    )
    """)
    
    sql = """
    INSERT INTO VipUsers (nome, whatsApp, email)
    VALUES (%s, %s, %s)
    """
    values = (nome, whatsApp, email)
    cursor.execute(sql, values)
    conn.commit()
    print(f"{cursor.rowcount} registro(s) inserido(s).")
    
    return cursor.lastrowid


def close():
    cursor.close()
    conn.close()
