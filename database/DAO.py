from database.DB_connect import DBConnect


class DAO:
    def __init__(self):
        pass

    @staticmethod
    def get_all_localizations():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct c.Localization from classification c order by c.Localization """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row['Localization'])
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_edge_double_loop(l1, l2):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select c.Localization l1, c2.Localization l2, count(distinct i.Type) peso
from classification c , classification c2 , interactions i 
where (i.GeneID1 = c.GeneId and i.GeneID2 = c2.GeneID) or (i.GeneID1 = c2.GeneId and i.GeneID2 = c.GeneID) 
and c.Localization = %s and c2.Localization = %s
group by c.Localization , c2.Localization """
        cursor.execute(query, (l1, l2))
        result = []
        for row in cursor:
            result.append((row['l1'], row['l2'], row['peso']))
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def get_edges():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select c.Localization l1, c2.Localization l2, count(distinct i.type) peso
                    from interactions i , classification c , classification c2 
                    where (i.GeneId1 = c.GeneId and i.GeneId2 = c2.GeneId) or 
                    (i.GeneId2 = c.GeneId and i.GeneId1 = c2.GeneId) and c.Localization != c2.Localization 
                    group by l1, l2"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append((row['l1'], row['l2'], row['peso']))
        cursor.close()
        cnx.close()
        return result
