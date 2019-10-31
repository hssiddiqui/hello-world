alert_system='console'
error_sensitivity='critical'
error_message='OMG! Something terrible has happened!'
if alert_system=='console':
    print(error_message)
elif alert_system == 'email':
    if error_sensitivity == 'critical':
        send_email('admin@example.com', error_message)
    elif error_sensitivity == 'medium':
        send_email('support.1@example.com', error_message)
    else:
        send_email('support.2@example.com, error_message)
