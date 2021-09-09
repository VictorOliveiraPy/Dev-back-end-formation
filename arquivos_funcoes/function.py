def capital(text: str) -> str:
    return text.upper()


msg = 'victor hugo'


# result = capital(text=msg)


def extract_email_provider(email: str) -> (str, str):
    separate_email = email.split(sep='@')
    user = separate_email[0]
    provider = separate_email[1]
    return user, provider


email = 'victorblog@gmail.com'


# user, provider = extract_email_provider(email=email)


def write_file_csv(name: str, header: str, contents: list) -> bool:
    try:
        with open(file=name, mode='w', encoding='utf8') as f:
            line = header + '\n'
            f.write(line)
            for content in contents:
                line = str(content) + '\n'
                f.write(line)

    except Exception as exc:

        print(exc)
        return False
    return True


name = 'ages.function.csv'
header = 'ages'
contents = [30, 20, 31, 22, 93, 82, 100, 120]
result = write_file_csv(name=name, header=header, contents=contents)


def annual_compound_interest(initial_value: float, annual_interest_rate: float, years: int) -> float:
    final_value = initial_value
    for year in range(1, years + 1):
        final_value = final_value * (1 + annual_interest_rate)
    final_value = round(final_value, 2)
    print(
        f'Para um valor inicial de R$ {initial_value} e uma taxa de juros anual de {annual_interest_rate},'
        f' em {years} anos voce tera R$ {final_value}'
    )
    return final_value


initial_value, annual_interest_rate, years = 1000.00, 0.05, 10
final_value = annual_compound_interest(initial_value=initial_value, annual_interest_rate=annual_interest_rate, years=years)
