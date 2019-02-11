SELECT 
DISTINCT msgs.id AS id, 
msgs.discord_user_id,
msgs.content, 
COALESCE(LEAD(msgs.id) OVER (ORDER BY msgs.created_at)
,FIRST_VALUE(msgs.id)  OVER (ORDER BY msgs.created_at ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)) AS nextitemid,
COALESCE(LAG(msgs.id)  OVER (ORDER BY msgs.created_at)
,LAST_VALUE(msgs.id)   OVER (ORDER BY msgs.created_at ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)) AS previtemid,
COALESCE(LEAD(msgs.id) OVER (PARTITION BY msgs.discord_user_id ORDER BY msgs.created_at)
,FIRST_VALUE(msgs.id)  OVER (PARTITION BY msgs.discord_user_id ORDER BY msgs.created_at ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)) AS nextuseritemid,
COALESCE(LAG(msgs.id)  OVER (PARTITION BY msgs.discord_user_id ORDER BY msgs.created_at)
,LAST_VALUE(msgs.id)   OVER (PARTITION BY msgs.discord_user_id ORDER BY msgs.created_at ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)) AS prevuseritemid
FROM discord_messages AS msgs
WHERE msgs.discord_channel_id = '524592892627517450'
