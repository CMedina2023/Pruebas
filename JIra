from jira import JIRA

# Configurar credenciales de Jira
jira_url = 'https://carlosprueba.atlassian.net'
jira_user = 'carlosmarsh@hotmail.com'
jira_token = 'ATATT3xFfGF07d8fddMMTUZOnJhzXXLG40txpySkvjsDJaXyI6TmvzqDlOxK8dOQpls_iS9YyFs9oLqQ6D4PRr2oxXkCMpU7Xnbzd1FMUuT3cSQA9jnwjG0v6mG8bJ6soSnwU2PIPn7GD1zdDvDTIlKks79MhIQDrNV-Qtn6FY8wdojpCkba0Wk=ABE9E89C'

# Conectar a Jira
jira = JIRA(jira_url, basic_auth=(jira_user, jira_token))

# ID de la tarea de Jira (por ejemplo, "PROY-123")
issue_id = 'PROY-123'

# Agregar un comentario en la tarea cuando la prueba se complete
comentario = 'La prueba automatizada main.py se ha ejecutado correctamente.'

# Actualizar la tarea en Jira
jira.add_comment(issue_id, comentario)
print(f'Se ha actualizado la tarea {issue_id} en Jira.')
