select article.owner_id, owner.owner_name, count(distinct category_article_mapping.category_id) as different_category_count
FROM article 
INNER JOIN category_article_mapping
ON article.article_id = category_article_mapping.article_id
INNER JOIN owner
ON article.owner_id = owner.owner_id
GROUP BY article.owner_id 
ORDER BY count(distinct category_article_mapping.category_id) DESC;