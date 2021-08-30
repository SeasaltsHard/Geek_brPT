def param_str(name, s_name, bd_year, cty, email, phone):
    return f"Вас зовут: {s_name} {name}. Вы родились в {bd_year} году и проживаете в г. {cty}. " \
           f"Адрес электронной почты и телефон: {email} и {phone}"


print(param_str(name='', s_name='', bd_year='', cty='', email='', phone=''))
